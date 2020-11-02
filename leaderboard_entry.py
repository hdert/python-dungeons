"""See leaderboard_entry.__doc__."""
from datetime import date
from get_username import get_username


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


if __name__ == "__main__":
    from db_create3 import db_create
    from random import randint as rand
    leaderboard_entry(db_create(), [int(input()), int(input()), int(input())])
