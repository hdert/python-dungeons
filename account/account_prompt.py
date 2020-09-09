"""
Author: Justin
Description: see account_prompt.__doc__
"""


def account_prompt():
  """Ask the user if they have an account, return a boolean based off of this"""

  while True:
    user_input = input("Do you have an account [y/n]: ").lower()
    if user_input == 'y' or user_input == 'yes':
      return True
    if user_input == 'n' or user_input == 'no':
      return False
    print("Please reply with 'y' for yes or 'n' for no")


if __name__ == "__main__":
  account_prompt()
