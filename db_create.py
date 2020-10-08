# noqa: D100
from os.path import isfile
import sqlite3
from datetime import date

db_path = "main.db"


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
    if not isfile(db_path):
        conn = sqlite3.connect(db_path)
        conn.isolation_level = None
        c = conn.cursor()
        c.execute("""
    CREATE TABLE leaderboard(
      username varchar(15) NOT NULL,
      date date NOT NULL
    );
    """)
        c.execute("""
    CREATE TABLE score(
      leaderboard_id REFERENCES leaderboard(rowid) NOT NULL,
      score tinyint(2) NOT NULL
    )
    """)
        current_date = date.today()
        users = [['Billy', current_date], ['Eilish', current_date],
                 ['Joel', current_date]]
        score = [[5, 7, 15], [15, 15, 14], [2, 7, 13]]
        for i in users:
            c.execute(
                """
      INSERT into leaderboard (username,date) VALUES (?,?);
      """, [i[0], i[1]])
            user_id = c.lastrowid
            for i in range(3):
                c.execute(
                    """
        INSERT into score (leaderboard_id,score) VALUES (?,?);
        """, [user_id, score[users.index(i)][i]])
    else:
        conn = sqlite3.connect(db_path)
        conn.isolation_level = None
        c = conn.cursor()
    return conn, c


if __name__ == "__main__":
    db_create(db_path)
