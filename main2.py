"""See main.__doc__."""
from db_create2 import db_create
from introduction import introduction
from navigate2 import navigate
from quiz_check3 import quiz_check
from quiz3 import quiz
from leaderboard_entry import leaderboard_entry
from show_leaderboard import show_leaderboard
from user_binary_choice import user_binary_choice


def main():
    """Run through the entire game."""
    score = [None, None, None]
    introduction()
    location = navigate()
    while True:
        if quiz_check(location, score):
            score = quiz(location, score)
            if (score[0] is not None and score[1] is not None
                    and score[2] is not None):
                if user_binary_choice(
                        "Do you want your score saved in the leaderboard"):
                    c = db_create()
                    leaderboard_entry(c, score)
                if user_binary_choice("Do you want to see the leaderboard"):
                    show_leaderboard(c)
                if user_binary_choice("Do you want to play again"):
                    return main()

        else:
            if location != 0:
                input("""
    You've done this room.""")
        location = navigate(location)


if __name__ == "__main__":
    main()
