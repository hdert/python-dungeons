"""
Author: Justin
Description: see account_sign_in.__doc__
"""
from account_get_stats import account_get_stats
import sys
sys.path.insert(1, 'database/')
from db_wrapper import db_wrapper
from account_check_existence import account_check_existence
from account_prompt import account_prompt


def account_sign_in(c):
  """Get the user's username and password, authenticate them, and return their stats and user_id

  Keyword arguments:
  c -- the database cursor object
  """
  for x in range(1, 3):
    username = input("Please enter your username: ").lower()
    if account_check_existence(c, username):
      
    elif x == 1:
      print("Not a valid username")
      if account_prompt():
        continue
      else:
        account_create()
        return
    else:
      print("Not a valid username")
  print("You've failed three times, please restart the program")
  sys.exit()


if __name__ == "__main__":
  account_sign_in()
