"""
Author: Justin
Description: see account_check_existence.__doc__
"""


def account_check_existence(c, username):
  """Check the existence of an account by username.
  
  Keyword arguments:
  c -- the database cursor object
  """

  c.execute("SELECT username FROM users WHERE username = '?'", username)


if __name__ == "__main__":
  import sys
  sys.path.insert(1, 'database/')
  from db_wrapper import db_wrapper
  conn, c = db_wrapper()
  account_check_existence(c, input("Username: "))
