"""
Author: Justin
Description: see db_wrapper.__doc__
"""
from db_check_existence import db_check_existence
from db_connect import db_connect


def db_wrapper(db_path="main.db"):
  """Call db_check_existence with db_path and return the connection and cursor objects.

  Keyword arguments:
  db_path -- the path to the database to connect to (default main.db)
  """
  if db_check_existence(db_path):
    from db_table_create3 import db_table_create
    conn = db_connect(db_path)
    return conn, db_table_create(conn)
  else:
    conn = db_connect(db_path)
    return conn, conn.cursor()


if __name__ == "__main__":
  db_wrapper()
