from os.path import isfile
import sqlite3

db_path = "main.db"


def db_create(db_path="main.db"):
  """Check that the database doesn't exist, create the database, create the tables, finally connect to the database.
  
  Use os.path.isfile() on the database path to check if the file exists.
  Connect to the database. Set the conn.isolation_level to None.
  If the database doesn't exist create the tables leaderboard and score with the columns username, date; and leaderboard_id, and score.
  Else connect to the database
  """
  db_exists = isFile(db_path)
  conn = sqlite3.connect(db_path)
  conn.isolation_level = None
  c = conn.cursor()
  if not db_exists
    create_table()

if __name__ == "__main__":
    db_create(db_path)
