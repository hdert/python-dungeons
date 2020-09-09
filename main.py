"""
Author: Justin
Description: to have a general testable flowchart of modules
"""
import sys
sys.path.insert(1, 'database/')
sys.path.insert(1, 'account/')
from db_wrapper import db_wrapper
from account_prompt import account_prompt
from account_sign_in import account_sign_in
from account_create import account_create


def main():
  conn, c = db_wrapper()
  if account_prompt():
    account_sign_in(c)
  else:
    account_create(c)


if __name__ == "__main__":
  main()