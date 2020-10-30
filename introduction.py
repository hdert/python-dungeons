"""See introduction.__doc__."""


def introduction():  # noqa: D205, D400
    """Interactively explain the game's input mechanism and tell the backstory
    to the user.

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
            return
        elif user_input == "2":
            input("""
    What? Escape? Why would you want to do that now?""")
        elif user_input in ("3", "4"):
            input("""
    You walk into the concrete of the blocked doorway""")
        else:
            input("""
    When prompted, enter one of the numbers 1, 2, 3, 4.
    Each number corresponds to an action printed on screen""")


if __name__ == "__main__":
    introduction()
