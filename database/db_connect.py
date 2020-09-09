"""
Author: Justin
Description: see db_connect.__doc__
"""
import sqlite3


def db_connect(db_path="main.db"):
  """Connect to a database, set the isolation level to None, and return the connection object.
    
  Keyword arguments:
  db_path -- the path to the database to connect to (default main.db)
  """
  conn = sqlite3.connect(db_path)
  conn.isolation_level = None
  return conn


if __name__ == "__main__":
  db_connect()
