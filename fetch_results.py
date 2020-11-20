"""See fetch_results.__doc__."""
from user_binary_choice import user_binary_choice
from get_username import get_username


def fetch_results(c):
    """Get the leaderboard with optional filtering by username.

    Args:
        c:
            The cursor object.
    Returns:
        The results of the database query
    """
    if user_binary_choice("Do you want to search by username"):
        username = "%{}%".format(get_username())
        c.execute(
            """SELECT * FROM `leaderboard`
            WHERE `username` LIKE ?
            ORDER BY `scoretotal` DESC, `username` ASC""", [username])
    else:
        c.execute("""SELECT * FROM `leaderboard`
        ORDER BY `scoretotal` DESC, `username` ASC""")
    results = c.fetchall()
    if not results:
        input("""
    No results.""")
    return results


if __name__ == "__main__":
    from db_create3 import db_create
    print(fetch_results(db_create()))
