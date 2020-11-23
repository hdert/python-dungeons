"""A compilation of all of the components."""
from os.path import isfile
import sqlite3
from datetime import date
from random import randint as rand
try:  # check if the environment has module curses
    import curses
except ModuleNotFoundError:
    from traceback import print_exc
    from sys import exit as sys_exit
    print_exc()
    print("""
    You need to install windows-curses. You can do this through the
    command:
    `python -m pip install windows-curses`""")
    sys_exit()
try:  # check if the terminal supports cursor control
    curses.initscr()
    curses.endwin()
except AttributeError:
    from traceback import print_exc
    from sys import exit as sys_exit
    print_exc()
    print("""
    You need to run this program in one of: Windows Command Prompt or
    Linux/Mac VT100 equivalent terminal.""")
    sys_exit()
from sys import version_info
if version_info < (3, 6):  # Check if python version is less than 3.6.0
    from sys import exit as sys_exit
    print("""
    You need to use a version of python greater than or equal to python
    version 3.6.0""")
    sys_exit()


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
    # check if the database exists before the database is created
    conn = sqlite3.connect(db_path)
    conn.isolation_level = None
    # make it so that changes to the database are committed instantly
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


def fetch_results(c):
    """Get the leaderboard with optional filtering by username.

    Args:
        c:
            The cursor object.
    Returns:
        The results of the database query
    """
    if user_binary_choice("Do you want to search by username"):
        username = f"%{get_username()}%"
        # add wildcards around the username so that the user gets the most
        # results
        c.execute(
            """SELECT * FROM `leaderboard`
        WHERE `username` LIKE ?
        ORDER BY `scoretotal` DESC, `username` ASC""", [username])
        # select all results that have the variable username in them
        # order the results by the highest scoring, if there are conflicts
        # order them by username
    else:
        c.execute("""SELECT * FROM `leaderboard`
        ORDER BY `scoretotal` DESC, `username` ASC""")
        # if the user doesn't want to search by username give them all of the
        # results
    results = c.fetchall()
    if not results:
        # Give the user a message if there are no results
        input("""
    No results.""")
    return results


def get_username():
    """Ask the user for their username, validate it and return it.

    Return:
        A string with the validated username.
    """
    while True:
        # do this until the user enters a valid input
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
            # check if the user's input contains at least one letter or number
            # follow this up by checking if the user's input is entirely
            # numbers
            # if the user has at least one character then it passes
            # if the user has only numbers it fails
            # if the user has at least one char and some numbers it passes
            # it's this way so that mixed alpha numeric usernames work
            return user_input
        else:
            # give the user a message if their username doesn't have any
            # characters
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
        # get user input until they enter something valid
        user_input = input("""
    Navigation:
    1) North: Cheese Room;
    2) South: Exit;
    3) East: Blocked Door;
    4) West: Blocked Door;
    [1-4]: """)
        # this entire block can't be condensed in the manner of the component
        # navigation because of the custom error messages and success messages
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
        score = [None, None, None]  # set the list of scores to None
        introduction()
        location = navigate()
        while True:
            if quiz_check(location, score):
                # check if a user has played the quiz of the room they're in
                score = quiz(location, score)  # if so, play that quiz
                if (score[0] is not None and score[1] is not None and
                        score[2] is not None):
                    if user_binary_choice(
                            "Do you want your score saved in the leaderboard"):
                        c = db_create()
                        leaderboard_entry(c, score)
                    if user_binary_choice(
                            "Do you want to see the leaderboard"):
                        if 'c' not in locals():
                            # check if the variable c exists
                            # if it doesn't create it
                            c = db_create()
                        show_leaderboard(c)
                    if user_binary_choice("Do you want to play again"):
                        break  # reset vars to play again
                    else:
                        return  # exit the program
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
    # define room names
    room = [
        "Entrance", "Math Room", "English Room", "NCEA Headquaters",
        "Fancy Wall"
    ]

    # define a list of where rooms are relative to each other
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
        # if user input is non-numeric show an error message and re-run the
        # code
        out_of_range_error(4)
        return navigate(location)
    if user_input in (1, 2, 3, 4):
        # check that the user input is valid
        if relations[user_input - 1][location] == 4:
            # check if the user navigated towards a wall
            # if so, re-run the code
            input("""
    That wall sure looks like a hidden entrance. You try and activate it,
    it doesn't react.""")
            return navigate(location)
        # else return the index of the room
        return relations[user_input - 1][location]
    # else throw an error an re-run the code
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
        # Make a list of the possible inputs the user could make
        # This is so it's flexible and can be used in binary choice
        # and multiple choice prompts
        numbers.append(str(i + 1))
    input("""
    When prompted, enter one of the numbers {}.
    Each number corresponds to an action printed on screen.""".format(
        ", ".join(numbers)))
    # print out the list using the join() function to make it look pretty


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
    if (location == 0):
        # check if the room is the entrance room ∴ the room doesn't have a quiz
        return False
    if ((location == 1 and score[0] is not None) or
        (location == 2 and score[1] is not None) or
        (location == 3 and score[2] is not None)):
        # check if the room has a score ∴ checking if the room has been played
        input("""
    You've done this room.""")
        # give the user a message telling them they've played that room
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
    angles of a polygon:""",
            """Substitute u = 3 and t = 5 into the following equation:
    d = ut + 3t²""", "Solve the equation 10x² - 27x - 9 = 0",
            """What is (8x - 1)/(4) + (3x-5)/(3) as a simplified single
    fraction""", "What is (3x² + 9x)/(x² - 9) as a simplified single fraction",
            """fk² - 9c² = 4d² + 16gk², Give the equation for k in terms of c,
    d, f, and g.""", "What is 3 * 5", "5³",
            "What does SOH in SOH CAH TOA stand for",
            "What does CAH in SOH CAH TOA stand for",
            "What does TOA in SOH CAH TOA stand for",
            "Angles on a line add to", "Angles on a point add to",
            "Vertically opposite angles", "Angles in a Triangle",
            "Angles in a Square", "An exterior angle of a triangle equals",
            "In an isosceles triangle", "Co-Interior angles on parallel lines"
        ],
        [
            "What part of speech is the word jump:",
            """What language feature is this:
    Go clean your room right now this instance you naughty little
    devil child!""", """What type of poem is this:
    Go clean your room right
    now this instance you naughty
    little devil child!""",
            "Every name is called a * as field and fountain street and town",
            """In place of the noun the * stands as he and she can clap their
    hands""", "The * describes a thing as magic wand or bridal ring",
            """The * means action something done to read, to write, to jump,
    to run""",
            "How things are done the * tells as quickly, slowly, badly, well",
            "The * shows relation as in the street or at the station",
            "* join in many ways sentences, words, phrase, and phrase",
            "Three little words you often see are * a, an, and the",
            "The * cries out hark! We need an exclamation mark",
            "A type of exaggeration used in literature.",
            """A type of figurative imagery using like, as, or than to compare
    two separate items with one another""",
            "Saying something that is different from what you really mean",
            "Using words that end in the same sounds",
            "Repeating something to emphasize it",
            """A series of words, connected in meaning and image which
    emphasize a point""", "Using irony as a attack",
            "A command to the reader or listener"
        ],
        [
            "How many credits does a Level 1 student in 2020 need:",
            "How many credits will a Level 2 student need next year:",
            "The Great Depression started in", "Obsidian is a type of",
            "Hyperinflation is when", "The proper name of America is",
            "Woodrow Wilson was", "Team Fortress 2 is the", "Mein Kampf is",
            "The Great Depression was caused by", "Armistice is",
            """What are the three types of texts in the english external
    unfamiliar texts""", "a NSN is a what", "A 747 is a famous",
            "How much water should you drink in a day",
            "Angles on the same arc",
            """If the angle at the center of a circle is 180° the angle at the
    circumference equals""", "alternate angles on parallel lines",
            "corresponding angles on parallel lines",
            "Two radii in a circle will form what"
        ]
    ]
    quiz_answers = [
        [['n - 2 * 180', '(n - 2)180', 'n - 2 * 60', '360', 1],
         ['n * 60', 'n + 3 * 180', '(n + 3)180', '360', 3],
         ['15', '30', '100', '90', 3],
         ['x = (-3/10) OR x = 3', 'x = 7', 'x = 3', '(10x + 3)(x - 3) = 0', 0],
         [
             '(36x-23)/(12)', '(3(8x - 1) + 4(3x - 5))/(12)', '(3x)/(x-3)',
             '(24x - 3 + 12x - 20)/(12)', 0
         ],
         [
             '(36x-23)/(12)', '(3x(x + 3))/((x+3)(x - 3))', '(3x)/(x-3)',
             '(x - 3)/(3x)', 2
         ],
         [
             'k = √((4d² + 9c²)/(f - 16g))', 'k = (4d² + 9c²)/(f - 16g)',
             'k = √(4d² + 9c²)', 'k = 4d² + 9c² - f - 16g', 0
         ], ['15', '20', '12', '8', 0], ['15', '45', '75', '125', 3],
         [
             'Sin', 'Sine', 'Sine Over Hypotenuse', 'Sine Opposite Hypotenuse',
             3
         ],
         [
             'Cos', 'Cosine Adjacent Hypotenuse', 'Cosine',
             'Cosine Against Hypotenuse', 1
         ],
         [
             'Tan', 'Tangent Over Hypotenuse', 'Tangent Opposite Hypotenuse',
             'Tangent', 2
         ], ['120°', '180°', '360°', 'Three', 1],
         ['360°', '180°', '120°',
          'Five', 0],
         ['add to 180°', 'are equal', 'add to 360°', 'are not related', 1],
         ['Add to 180°', 'Equals 360°', 'Equals 180°', 'Add to 360°', 0],
         ['Add to 180°', 'Equals 360°', 'Equals 180°', 'Add to 360°', 3],
         [
             '120°', 'The sum of the two opposite angles',
             '180° - the opposite angles', '360° - the opposite angles', 1
         ],
         [
             'The base angles are equal', 'The base angles add to 180°',
             'The base angles - 360° equals 180°',
             'The base angles are in a romantic relationship', 0
         ],
         [
             'Are equal', 'Add to 120°', 'Have no relationship', 'Add to 180°',
             3
         ]],
        [['Noun', 'Verb', 'Adjective', 'Adverb', 1],
         ['Hyperbole', 'Rhetoric', 'Imperative', 'Sonnet', 2],
         ['Sonnet', 'Haiku', 'Limerick', 'Free verse',
          1],
         ['Verb', 'Adverb', 'Noun', 'Field',
          2], ['clap', 'Article', 'Adverb', 'Pronoun',
               3], ['Adjective', 'Magic', 'Conjunction', 'Pronoun', 0],
         ['Verb', 'Adverb', 'Noun', 'Read',
          0], ['Quickly', 'Verb', 'Adverb', 'Noun', 2],
         ['Conjunction', 'Street', 'Preposition', 'Adjective', 2],
         ['Conjunctions', 'Sentences', 'Prepositions', 'Adjectives', 0],
         ['Trains', 'Articles', 'Adverbs', 'Pronouns', 1],
         ['Conjunction', 'Mark', 'Interjection', 'Preposition', 2],
         ['Exaggeration', 'Hyperbole', 'Imagery', 'Metaphor', 1],
         ['Exaggeration', 'Imagery', 'Metaphor', 'Simile', 3],
         ['Irony', 'Innuendo', 'Humor', 'Metaphor', 0],
         ['Assonance', 'Rhythm', 'Rhyme', 'Repetition', 2],
         ['Emphasis', 'Listing', 'Repetition', 'Direct speech',
          2], ['Emphasis', 'Listing', 'Repetition', 'Direct speech', 1],
         ['Irony', 'Sarcasm', 'Humor', 'Metaphor', 1],
         ['Imperative', 'Direct address', 'Direct speech', 'Fart', 0]],
        [['80', '60', '72', '70', 3], ['80', '60', '72', '52', 1],
         ['1929', '1933', '1923', '1928', 0],
         [
             'Rock', 'Glass', 'Volcanic Glass',
             'Block used to make a nether portal', 2
         ],
         [
             'The value of a local currency quickly lowers',
             'The gas content of a stomach rapidly increases',
             "A country rapidly enlarges it's borders",
             "Too many people start to work at McDonald's™", 0
         ], ['The United States of America', 'We The People', 'USA', 'US', 0],
         [
             'A famous actor', 'A common name', 'A famous celebrity',
             'The president of The United States of America (POTUS)', 3
         ],
         [
             'Best game in existence', 'Has been in development for 19 years',
             'And is not dead', 'All of the above', 3
         ],
         [
             'German', 'A book written by Hitler',
             'A book written by Woodrow Wilson', 'A famous piece of paper', 1
         ],
         [
             'Hyperinflation', 'Mein Kampf', 'Hitler', 'The Wall Street Crash',
             3
         ],
         [
             'An agreement in a war to stop fighting',
             'A form of jointed club', 'A type of business deal',
             'The name for a yellow carrot', 0
         ],
         [
             'Story, poem and fiction',
             'Narrative prose, poetry and non-fiction',
             'fiction, poetry and non-fiction',
             'aggressive, assertive and passive', 1
         ],
         [
             'National Steward Number', 'iNternational Scalene Nonagon',
             'New South Nales', 'National Student Number', 3
         ], ['Boat', 'Airbus Plane', 'Boeing Plane', 'Rifle', 2],
         [
             '2 Liters', '1.5 Liters', "Enough so that you aren't thirsty",
             'How much your friends drink', 2
         ], ['are 180°', 'add to 180°', 'are equal', 'add to 120°', 2],
         ['80°', '50°', '180°', '90°', 3],
         [
             'Are equal', 'Add to 120°', 'Have no relationship', 'Add to 180°',
             0
         ],
         [
             'Are equal', 'Add to 120°', 'Have no relationship', 'Add to 180°',
             0
         ],
         [
             'A parallelogram', 'A polygon', 'A isosceles triangle',
             'A scalene triangle', 2
         ]]
    ]
    # get the question answer, and score values to use based on the users
    # location
    current_questions = quiz_questions[location - 1]
    current_answers = quiz_answers[location - 1]
    score[location - 1] = 0
    while len(current_questions) > 5:
        # Run while there are still questions left
        # we only want to give 15/20 questions to the user
        rand_choice = rand(0, len(current_questions) - 1)
        # pick a random question and answer
        user_input = None  # reset the user's input
        while user_input not in (1, 2, 3, 4):
            try:
                user_input = int(
                    input(f"""
    {current_questions[rand_choice]}
    1) {current_answers[rand_choice][0]}
    2) {current_answers[rand_choice][1]}
    3) {current_answers[rand_choice][2]}
    4) {current_answers[rand_choice][3]}
    [1-4]: """))  # give the user the randomly selected question and possible
                # answers
            except ValueError:  # if the user doesn't put in an interger, skip
                # the question and give them the error message
                user_input = None  # set user_input so the program doesn't
                # break
            if user_input not in (1, 2, 3, 4):
                out_of_range_error(4)
        if user_input - 1 == current_answers[rand_choice][4]:
            # shift user response to the left so it fits the list format and
            # compare it to the index of the answer in the answer's list
            input("""
    You got it right""")
            score[location - 1] += 1
        else:
            input(f"""
    You got it wrong.
    The answer was:
    {current_answers[rand_choice][current_answers[rand_choice][4]]}""")
        # show the user the correct answer for user feedback
        current_questions.pop(rand_choice)
        current_answers.pop(rand_choice)
        # delete the now used answer and question from their respective lists
    return score


def show_leaderboard(c):
    """Display the leaderboard.

    Args:
        c:
            The cursor object.
    """
    results = fetch_results(c)
    if not results:
        # end if there are no results
        return
    try:
        stdscr = curses.initscr()  # initialize the curses window
        curses.noecho()  # make user entered characters not appear
        curses.cbreak()  # make user input instant
        lines = 0  # the total of lines that have been displayed on screen
        while lines < len(results):
            stdscr.addstr(
                "| {:15} | {:10} | {:13} | {:11} | {:13} | {:10} |\n".format(
                    'Username', 'Date', 'Overall Score', 'Maths Score',
                    'English Score',
                    'NCEA Score'))  # print the centered header
            for _ in range(curses.LINES - 2):
                # do this as many times as the terminal's height - 1
                stdscr.addstr(
                    "| {:15} | {:10} | {:13} | {:11} | {:13} | {:10} |\n".
                    format(results[lines][0], results[lines][1],
                           results[lines][5], results[lines][2],
                           results[lines][3], results[lines][4]))
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
    except KeyboardInterrupt:
        # catch the KeyboardInterrupt, close the curses window, print the
        # traceback, then exit the program. This helps restore terminal
        # control back to the user if they unexpectedly end the program
        from traceback import print_exc
        from sys import exit as sys_exit
        curses.endwin()
        print_exc()
        sys_exit()


def user_binary_choice(x):  # noqa: D400, D205
    """Deduce whether the user wants x to happen

    Args:
        x:
            The thing that the program wants to find out if the user wants
    Return:
        A boolean value, True if the user wants x, False if they do not.
    """
    while True:
        # run until we get a valid input
        try:
            user_input = int(
                input(f"""
    {x}:
    1) Yes
    2) No
    [1-2]: """))
        except ValueError:
            # if the user enters a non-numeric character, show an error
            # message and re-run the program
            out_of_range_error(2)
            return user_binary_choice(x)
        if user_input in (1, 2):
            if user_input == 1:
                return True
            return False
        # print an error message if the user enters an invalid input
        out_of_range_error(2)


if __name__ == "__main__":
    main()
