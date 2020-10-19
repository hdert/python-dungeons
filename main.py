"""See main.__doc__."""
from db_create2 import db_create
from introduction import introduction
from navigate import navigate
from quiz_check import quiz_check
from quiz import quiz
from want_leaderboard_entry import want_leaderboard_entry
from leaderboard_entry import leaderboard_entry
from show_leaderboard import show_leaderboard


def main():
    """Run through the entire game."""
    score_one = None
    score_two = None
    score_three = None
    introduction()
    location = navigate()
    while True:
        if quiz_check(location):
            quiz(location)
            if score_one is not None and score_two is not None and score_three is not None:
                if want_leaderboard_entry():
                    conn, c = db_create()
                    leaderboard_entry(conn, c)
                    show_leaderboard(conn, c)
                return
        else:
            input("""
    You've done this room.""")
        navigate(location)


if __name__ == "__main__":
    main()
