from os import system, name
from os.path import isfile
import sqlite3
from datetime import date
from random import randint as rand
from shutil import get_terminal_size
def clear_screen():
    if name == 'nt':
        system('cls')
    else:
        system('clear')
def db_create(db_path="main.db"):  # noqa: D205, D400
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
    c.execute("INSERT INTO leaderboard VALUES (?, ?, ?, ?, ?, ?)", [get_username(), date.today(), score[0], score[1], score[2], sum(score)])
    input("""
    Your score, username and the date of completion have been entered into the
    leaderboard""")
def main():
    user_wants_to_play = True
    while user_wants_to_play:
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
                        user_wants_to_play = False
                        break
            else:
                if location != 0:
                    input("""
    You've done this room.""")
            location = navigate(location)
def navigate(location=0):  # noqa: D205
    room = ["Crypt Entrance", "Math Room", "English Room", "NCEA Headquaters", "Fancy Wall"]
    relations = [[2, 4, 4, 4], [4, 4, 0, 4], [3, 0, 4, 4], [1, 4, 4, 0]]
    desc = ["A dull enclosed space with three doors", "A dull enclosed space with one door", "A dull enclosed space with one door", "A dull enclosed space with one door"]
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
    numbers = []
    for i in range(length):
        numbers.append(str(i + 1))
    input("""
    When prompted, enter one of the numbers {}.
    Each number corresponds to an action printed on screen.""".format(
        ", ".join(numbers)))
def quiz_check(location, score):
    if ((location == 1 and score[0] is not None)
            or (location == 2 and score[1] is not None)
            or (location == 3 and score[2] is not None)):
        return False
    if (location == 0):
        return False
    return True
def quiz(location, score):
    quiz_questions = [
        [
            "The answer is Example:", """Finish the lyrics:
Boom clap I'm in me mom's *"""], ["What part of speech is the word jump?", """What language feature is this:
    Go clean your room right now this instance you naughty little
    devil child!""", """What type of poem is this:
    Go clean your room right
    now this instance you naughty
    little devil child!"""], ["How many credits does a Year 11 student in 2020 need:"]]
    quiz_answers = [[["Example", "None", "wasd", "Not Example", 0], ["car", "room", "house", "town", 0]], [["Noun", "Verb", "Adjective", "Adverb", 1], ["Hyperbole", "Rhetoric", "Imperative", "Sonnet", 2], ["Sonnet", "Haiku", "Limerick", "Free verse", 1]], [["80", "60", "72", "70", 3]]]
    current_questions = quiz_questions[location - 1]
    current_answers = quiz_answers[location - 1]
    score[location - 1] = 0
    while len(current_questions) > 0:
        rand_choice = rand(0, len(current_questions) - 1)
        answer = current_answers[rand_choice][4]
        answer_text = current_answers[rand_choice][answer]
        try:
            user_input = int(
                input(f"""
    {current_questions.pop(rand_choice)}
    1) {current_answers[rand_choice].pop(0)}
    2) {current_answers[rand_choice].pop(0)}
    3) {current_answers[rand_choice].pop(0)}
    4) {current_answers[rand_choice].pop(0)}
    [1-4]: """))
        except ValueError:
            out_of_range_error(4)
            user_input = None
        current_answers.pop(rand_choice)
        if user_input in (1, 2, 3, 4):
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
    if user_binary_choice("Do you want to search by username"):
        username = f"%{get_username()}%"
        c.execute(
            """SELECT * FROM `leaderboard`
            WHERE `username` LIKE ?
            ORDER BY `scoretotal` DESC, `username` ASC""", [username])
    else:
        c.execute("""SELECT * FROM `leaderboard`
            ORDER BY `scoretotal`, `username` ASC""")
    clear_screen()
    results = c.fetchall()
    lines = 0
    while lines < len(results):
        print('/' + "¯" * 89 + '\\')
        print(
            f"| {'Username':15} | {'Date':10} | {'Overall Score':13} | {'Maths Score':11} | {'English Score':13} | {'NCEA Score':10} |"
        )
        for x in range(get_terminal_size().lines - 3):
            line = x + lines
            print(
                f"| {results[line][0]:15} | {results[line][1]:10} | {results[line][5]:13} | {results[line][2]:11} | {results[line][3]:13} | {results[line][4]:10} |"
            )
            lines += 1
            if lines + x >= len(results):
                input("(enter to continue)")
                clear_screen()
                return
        while True:
            user_input = input("[q]uit, [n]ew page: ").lower()
            if user_input == 'q':
                clear_screen()
                return
            if user_input == 'n':
                clear_screen()
                break
            print('\033[A', end='')
def user_binary_choice(x):  # noqa: D400, D205
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