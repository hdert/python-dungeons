"""
Author: Justin
Description: see db_table_create.__doc__
"""


def db_table_create(conn):
    """Create tables in a new database and return the cursor.
    
    Keyword arguments:
    conn -- the database connection object
    """
    c = conn.execute("""CREATE TABLE users(
        username varchar(15) NOT NULL,
        password varchar(15) NOT NULL,
        room tinyint(1) NOT NULL
    );
    """)
    c.execute("""CREATE TABLE questions(
        user_id REFERENCES users(rowid) NOT NULL,
        question varchar(30) NOT NULL,
        answer varchar(30) NOT NULL
    )
    """)
    c.execute("""CREATE TABLE leaderboard(
        user_id REFERENCES users(rowid) NOT NULL,
        date date NOT NULL
    );
    """)
    c.execute("""CREATE TABLE score(
        leaderboard_id REFERENCES leaderboard(rowid),
        user_id REFERENCES users(rowid),
        score tinyint(2) NOT NULL
    );
    """)
    return c


if __name__ == "__main__":
    from db_connect import db_connect
    conn = db_connect()
    c = db_table_create(conn)