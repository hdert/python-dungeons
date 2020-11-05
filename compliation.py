"""A complilation of all of the components."""
from os.path import isfile
import sqlite3
from datetime import date
from random import randint as rand
import curses


def db_create(db_path="main.db"):  # noqa: D205, D400
    """Check that the database doesn't exist, create the database, create the
        tables, finally connect to the database.

    Use os.path.isfile() on the database path to check if the file exists.
    Connect to the database. Set the conn.isolation_level to None.
    If the database doesn't exist create the tables leaderboard and score with
    the columns username, date; and leaderboard_id, and score.
    Else connect to the database.

    Args:
        db_path:
            Optional; The path to the database file, defaults to main.db.

    Returns:
        The cursor object.
    """
    db_exists = isfile(db_path)
    conn = sqlite3.connect(db_path)
    conn.isolation_level = None
    c = conn.cursor()
    if not db_exists:
        c.execute("""
        CREATE TABLE leaderboard(
            username varchar(15) NOT NULL,
            date date NOT NULL,
            scoreone tinyint(2) NOT NULL,
            scoretwo tinyint(2) NOT NULL,
            scorethree tinyint(2) NOT NULL,
            scoretotal tinyint(2) NOT NULL
        )
        """)
    return c


def get_username():
    """Ask the user for their username, validate it and return it.

    Return:
        A string with the validated username.
    """
    while True:
        user_input = input("""
    Please enter the username: """)
        if len(user_input) > 15:
            input("""
    The username is too long. The username needs to be under 15 characters""")
        elif len(user_input) < 1:
            input("""
    The username is too short. The username needs to be more than 0
    characters""")
        elif user_input.isalnum() and not user_input.isnumeric():
            return user_input
        else:
            input("""
    The username doesn't contain any characters. Please use characters""")


def introduction():  # noqa: D205, D400
    """Interactively explain the game's input mechanism.

    Tell the user to input a number between 1 and 4 corresponding to the
    action on screen that they want to take. Give an interactive example of
    this by using an example navigation system where the user has to navigate
    to the cheese room. Once this is completed recommend that the user gets
    some paper and a pen.
    """
    input("""
    Welcome to python-quiz, your source of NCEA knowledge quizzes.

    The only input in this game are the numbers 1 to 4. Each of these numbers
    will correspond to an action or answer.
    Try this example of navigation (press enter to continue)""")
    while True:
        user_input = input("""
    Navigation:
    1) North: Cheese Room;
    2) South: Exit;
    3) East: Blocked Door;
    4) West: Blocked Door;
    [1-4]: """)
        if user_input == "1":
            input("""
    You obviously know what you're doing.""")
            input("""
    These questions are supposed to be difficult, you should go grab something
    to write on.""")
            break
        if user_input == "2":
            input("""
    What? Escape? Why would you want to do that now?""")
        elif user_input in ("3", "4"):
            input("""
    You walk into the concrete of the blocked doorway""")
        else:
            out_of_range_error(4)


def leaderboard_entry(c, score):  # noqa: D400, D205
    """Insert the user's score, username and the date of completion into the
    leaderboard.

    Args:
        c:
            The cursor object.
        score:
            The score of the user.
    """
    c.execute("INSERT INTO leaderboard VALUES (?, ?, ?, ?, ?, ?)", [
        get_username(),
        date.today(), score[0], score[1], score[2],
        sum(score)
    ])
    input("""
    Your score, username and the date of completion have been entered into the
    leaderboard""")


def main():
    """Provide the background logic and link the components together."""
    while True:
        score = [None, None, None]
        introduction()
        location = navigate()
        while True:
            if quiz_check(location, score):
                score = quiz(location, score)
                if (score[0] is not None and score[1] is not None
                        and score[2] is not None):
                    if user_binary_choice(
                            "Do you want your score saved in the leaderboard"):
                        c = db_create()
                        leaderboard_entry(c, score)
                    if user_binary_choice(
                            "Do you want to see the leaderboard"):
                        show_leaderboard(c)
                    if not user_binary_choice("Do you want to play again"):
                        return
            else:
                if location != 0:
                    input("""
    You've done this room.""")
            location = navigate(location)


def navigate(location=0):  # noqa: D205
    """Show the user the options for navigation and give them a prompt.
    Check that the user has selected a valid target and move their
    location to that target.

    Show the user the options for navigation by getting their location and
    finding possible exits through the relations list. Find the names of the
    rooms on the other side of the exits by consulting the rooms list. Give
    the user a prompt where they answer the room they want to go to as a
    number 1-4 corresponding to the number beside the room shown in the prompt.
    Make sure the room value is not 4 and return the users updated location.

    Args:
        location:
            Optional; The room the user is currently in, defaults to 0.

    Returns:
        The location of the user as an int.
    """
    room = [
        "Crypt Entrance", "Math Room", "English Room", "NCEA Headquaters",
        "Fancy Wall"
    ]

    relations = [[2, 4, 4, 4], [4, 4, 0, 4], [3, 0, 4, 4], [1, 4, 4, 0]]

    try:
        user_input = int(
            input(f"""
    Navigation:
    1) North: {room[relations[0][location]]};
    2) South: {room[relations[1][location]]};
    3) East: {room[relations[2][location]]};
    4) West: {room[relations[3][location]]};
    [1-4]: """))
    except ValueError:
        out_of_range_error(4)
        return navigate(location)
    if user_input in (1, 2, 3, 4):
        if relations[user_input - 1][location] == 4:
            input("""
    That wall sure looks like a hidden entrance. You try and activate it,
    it doesn't react.""")
            return navigate(location)
        return relations[user_input - 1][location]
    out_of_range_error(4)
    return navigate(location)


def out_of_range_error(length):  # noqa: D205, D400
    """Print and out of range error message with the list of numbers based on
    the integer length.

    Args:
        length:
            The length of the listing of valid integer inputs.
    """
    numbers = []
    for i in range(length):
        numbers.append(str(i + 1))
    input("""
    When prompted, enter one of the numbers {}.
    Each number corresponds to an action printed on screen.""".format(
        ", ".join(numbers)))


def quiz_check(location, score):
    """Check if there is an unplayed quiz in the users current room.

    Args:
        location:
            The location of the user.
        score:
            The score of the user.
    Returns:
        A boolean value, True if there is a quiz, False if there is not.
    """
    if ((location == 1 and score[0] is not None)
            or (location == 2 and score[1] is not None)
            or (location == 3
                and score[2] is not None)):  # check if the room has a score
        # ∴ check if the room has been played
        return False
    if (
            location == 0
    ):  # check if the room is the entrace room ∴ the room doesn't have a quiz
        return False
    return True


def quiz(location, score):
    """Give the user an interactive quiz based on their location.

    Use the user's location find the correct set of quiz_questions and
    quiz_answers to use. Assign these questions and answers to
    current_questions and current_answers. Use the user's location to find and
    set the appropriate score to 0. While there are more than 0 questions do
    the following:
    1. Pick a random question in the range of questions left.
    2. Set the answer and answer text to answer and answer_text
    2. Give the user a prompt to type their answer, therein deleting the
    question from the question list. Convert this input to an integer
    3. Check that the user input matches answer
        3.1 If the answer was right, iterate the user score and display
        'You got it right'.
        3.2 If not display the correct answer using answer_text.
    If there are 0 questions left in the current location, return the user
    scores.

    Args:
        location:
            The location of the user.
        score:
            The score of the user.
    Returns:
        The score of the user.
    """
    # Initialize lists of answers and questions
    quiz_questions = [
        [
            """What is the correct formula to find the sum of the internal
            angles of a polygon:""",
            """What is the correct formula to find the sum of the external
            angles of a polygon:"""
        ],
        [
            "What part of speech is the word jump:",
            """What language feature is this:
    Go clean your room right now this instance you naughty little
    devil child!""", """What type of poem is this:
    Go clean your room right
    now this instance you naughty
    little devil child!"""
        ],
        [
            "How many credits does a Level 1 student in 2020 need:",
            "How many credits will a Level 2 student need next year:"
        ]
    ]
    quiz_answers = [[["n - 2 * 180", "(n - 2)180", "n - 2 * 60", "360", 1],
                     ["n * 60", "n + 3 * 180", "(n + 3)180", "360", 3]],
                    [["Noun", "Verb", "Adjective", "Adverb", 1],
                     ["Hyperbole", "Rhetoric", "Imperative", "Sonnet", 2],
                     ["Sonnet", "Haiku", "Limerick", "Free verse", 1]],
                    [["80", "60", "72", "70", 3], ["80", "60", "72", "52", 1]]]
    # get the question answer, and score values to use based on the users
    # location
    current_questions = quiz_questions[location - 1]
    current_answers = quiz_answers[location - 1]
    score[location - 1] = 0
    while len(current_questions) > 0:
        # Run while there are still questions left
        rand_choice = rand(0, len(current_questions) - 1)
        # pick a random question and answer
        answer = current_answers[rand_choice][
            4]  # get the integer that 'points' to the correct answer
        answer_text = current_answers[rand_choice][
            answer]  # feed this integer back in to get the text of the answer
        try:
            user_input = int(
                input(f"""
    {current_questions.pop(rand_choice)}
    1) {current_answers[rand_choice].pop(0)}
    2) {current_answers[rand_choice].pop(0)}
    3) {current_answers[rand_choice].pop(0)}
    4) {current_answers[rand_choice].pop(0)}
    [1-4]: """))  # give the user the randomly selected question and possible
            # answers
        except ValueError:  # if the user doesn't put in an interger, skip the
            # question and give them the error message
            out_of_range_error(4)
            user_input = None  # set user_input so the program doesn't break
        # delete the question from the master list, and take user input
        current_answers.pop(rand_choice)
        # get the answers to the randomly selected question
        if user_input in (1, 2, 3, 4):  # check if the users input is valid
            if user_input - 1 == answer:
                input("""
    You got it right""")
                score[location - 1] += 1
            else:
                input(f"""
    You got it wrong.
    The answer was:
    {answer_text}""")
    return score


def show_leaderboard(c):
    """Display the leaderboard with an optional username search function.

    Args:
        c:
            The cursor object.
    """
    if user_binary_choice("Do you want to search by username"):
        username = f"%{get_username()}%"
        c.execute(
            """SELECT * FROM `leaderboard`
            WHERE `username` LIKE ?
            ORDER BY `scoretotal` DESC, `username` ASC""", [username])
    else:
        c.execute("""SELECT * FROM `leaderboard`
        ORDER BY `scoretotal` DESC, `username` ASC""")
    stdscr = curses.initscr()  # initialize the curses window
    curses.noecho()  # make user entered characters not appear
    curses.cbreak()  # make user input instant
    results = c.fetchall()
    lines = 0
    while lines < len(results):
        stdscr.addstr(
            "| {:15} | {:10} | {:13} | {:11} | {:13} | {:10} |\n".format(
                'Username', 'Date', 'Overall Score', 'Maths Score',
                'English Score', 'NCEA Score'))  # print the centered header
        for x in range(curses.LINES - 2):
            # do this as many times as the terminal's height - 1
            stdscr.addstr(
                "| {:15} | {:10} | {:13} | {:11} | {:13} | {:10} |\n".format(
                    results[lines][0], results[lines][1], results[lines][5],
                    results[lines][2], results[lines][3], results[lines][4]))
            # print the results spaced out, line by line
            lines += 1  # iterate the result line to print out
            if lines >= len(results):
                # if you reach the end of the results, pause, and end the
                # program
                stdscr.addstr("(enter to continue)")
                stdscr.getkey()  # equivalent of input() but for one char
                curses.endwin()  # close the curses window
                return
        stdscr.addstr("[q]uit, [n]ew page: ")
        # once the results span the terminal's height - 1 print this prompt
        stdscr.refresh()
        # get curses to display the buffered output
        while True:
            # get the user's input forever until they hit a valid key
            user_input = stdscr.getkey().lower()
            if user_input == 'q':
                # close the program
                curses.endwin()
                return
            if user_input == 'n':
                # clear the screen and then print a new screen of results
                stdscr.clear()
                break


def user_binary_choice(x):  # noqa: D400, D205
    """Deduce whether the user wants x to happen

    Args:
        x:
            The thing that the program wants to find out if the user wants
    Return:
        A boolean value, True if the user wants x, False if they do not.
    """
    while True:
        try:
            user_input = int(
                input(f"""
    {x}:
    1) Yes
    2) No
    [1-2]: """))
        except ValueError:
            out_of_range_error(2)
            return user_binary_choice(x)
        if user_input in (1, 2):
            if user_input == 1:
                return True
            return False
        out_of_range_error(2)


if __name__ == "__main__":
    main()
