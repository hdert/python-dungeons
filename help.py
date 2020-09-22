# noqa: D100
def help():  # noqa: D205, D400
    """Interactively explain the game's input mechanism and tell the backstory
        to the user.

    Tell the user to input a number between 1 and 4 corresponding to the
    action on screen that they want to take. Give an interactive example of
    this by using an example navigation system where the user has to navigate
    to the cheese room. Once this is completed tell the backstory to the user
    and recommend the user navigates to the first quiz when prompted, as well
    as recommending that the user gets some paper and a pen.
    """
    input("""
    Welcome to python-quiz, your source of NCEA knowledge quizzes.

    The only input in this game are the numbers 1 to 4. Each of these numbers
    will correspond to an action or answer.
    Try this example of navigation (press enter to continue): """)
    for x in range(10):
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
            return
        elif user_input == "2":
            input("""
    What? Escape? Why would you want to do that now?""")
        elif user_input == "3" or user_input == "4":
            input("""
    You walked into the concrete of the blocked doorway,
    donked your head and lost your non-existent brain cells""")
        else:
            input("""
    When prompted, enter one of the numbers 1, 2, 3, 4.
    Each number corresponds to an action printed on screen""")
    print("""
    You've had ten attempts at getting the right user input
    and you've failed every time.""")


if __name__ == "__main__":
    help()
