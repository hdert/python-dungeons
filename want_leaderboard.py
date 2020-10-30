"""See want_leaderboard.__doc__."""


def want_leaderboard():
    """Deduce whether the user wants to see the leaderboard.

    Return:
        A boolean value, True if the user wants to see the leaderboard, False
        if they do not.
    """
    while True:
        try:
            user_input = int(
                input("""
    Do you want to see the leaderboard:
    1) Yes
    2) No
    [1-2]: """))
        except ValueError:
            input("""
    When prompted, enter one of the numbers 1, 2.
    Each number corresponds to an action printed on screen""")
            user_input = None
        if user_input in (1, 2):
            if user_input == 1:
                return True
            return False
        else:
            input("""
    When prompted, enter one of the numbers 1, 2.
    Each number corresponds to an action printed on screen
    """)


if __name__ == "__main__":
    print(want_leaderboard())
