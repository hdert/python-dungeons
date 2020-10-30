"""See show_leaderboard.__doc__."""


def show_leaderboard(conn, c):
    """DooDoo.

    Args:
        c:
            The cursor object.
    """
    while True:
        try:
            user_input = int(
                input("""
    Do you want to search by username:
    1) Yes
    2) No
    [1-2]: """))
        except ValueError:
            input("""
    When prompted, enter one of the numbers 1, 2.
    Each number corresponds to an action printed on screen""")
            user_input = None
        if user_input in (1, 2):
            break
        input("""
    When prompted, enter one of the numbers 1, 2.
    Each number corresponds to an action printed on screen""")
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
        elif user_input.isalpha():
            break
        else:
            input("""
    The username doesn't contain any characters. Please use characters""")
    if user_input == 1:
        query = "SELECT * FROM `leaderboard` WHERE `name` LIKE ?"
        user_input = f"%{user_input}%"
    else:
        query = "SELECT * FROM `leaderboard`"


if __name__ == "__main__":
    from db_create2 import db_create
    show_leaderboard(db_create())
