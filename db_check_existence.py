"""
Author: Justin
Description: see db_check_existence.__doc__
"""
from os.path import isfile
from db_connect import db_connect
db_path = "main.db"


def db_check_existence(db_path):
    """Check if the db_path file exists and return the connection and cursor objects."""
    if not isfile(db_path):
        from db_table_create3 import db_table_create
        conn = db_connect()
        return conn, db_table_create(conn)
    else:
        conn = db_connect(db_path)
        return conn, conn.cursor()


if __name__ == "__main__":
    db_check_existence(db_path)