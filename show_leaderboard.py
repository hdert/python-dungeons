"""See show_leaderboard.__doc__."""
from user_binary_choice import user_binary_choice
from get_username import get_username


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
            ORDER BY `scoreavg`, `username` ASC""", [username])
    else:
        c.execute("""SELECT * FROM `leaderboard`
            ORDER BY `scoretotal`, `username` ASC""")
    print(c.fetchall())


if __name__ == "__main__":
    from db_create3 import db_create
    show_leaderboard(db_create())
