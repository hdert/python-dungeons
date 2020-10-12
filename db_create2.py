"""See db_create.__doc__."""
from os.path import isfile
import sqlite3
from datetime import date


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
        The connection object and the cursor object.
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
            scorethree tinyint(2) NOT NULL
        )
        """)
        current_date = date.today()
        users = [['Billy', current_date, 5, 7, 15],
                 ['Eilish', current_date, 15, 15, 14],
                 ['Joel', current_date, 2, 7, 13]]
        c.executemany(
            """
        INSERT INTO leaderboard
        (username, date, scoreone, scoretwo, scorethree)
        VALUES (?,?,?,?,?);
        """, users)
    return conn, c


if __name__ == "__main__":
    db_create()
