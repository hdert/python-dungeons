"""
Author: Justin
Description: see db_check_existence.__doc__
"""
from os.path import isfile


def db_check_existence(db_path="main.db"):
  """Check if the db_path file exists
  
  Keyword arguments:
  db_path -- the path to the database file to check for (default main.db)
  """
  if not isfile(db_path):
    return True
  else:
    return False


if __name__ == "__main__":
  db_check_existence("../main.db")
