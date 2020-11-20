"""See main.__doc__."""
from db_create3 import db_create
from introduction import introduction
from navigate2 import navigate
from quiz_check3 import quiz_check
from quiz4 import quiz
from leaderboard_entry import leaderboard_entry
from show_leaderboard2 import show_leaderboard
from user_binary_choice import user_binary_choice


def main():
    """Provide the background logic and link the components together."""
    while True:
        score = [None, None, None]
        introduction()
        location = navigate()
        if quiz_check(location, score):
            score = quiz(location, score)
            if (score[0] is not None and score[1] is not None and
                    score[2] is not None):
                if user_binary_choice(
                        "Do you want your score saved in the leaderboard"):
                    c = db_create()
                    leaderboard_entry(c, score)
                if user_binary_choice("Do you want to see the leaderboard"):
                    if 'c' not in locals():
                        c = db_create()
                    show_leaderboard(c)
                if not user_binary_choice("Do you want to play again"):
                    return
        else:
            if location != 0:
                input("""
You've done this room.""")
        location = navigate(location)


if __name__ == "__main__":
    main()
