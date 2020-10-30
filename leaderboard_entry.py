"""See leaderboard_entry.__doc__."""
from datetime import date


def leaderboard_entry(c, score):
    """DooDoo.

    Args:
        c:
            The cursor object.
        score:
            The score of the user.
    """
    while True:
        user_input = input("""
    Please enter your username: """)
        if len(user_input) > 15:
            input("""
    Your username is too long. Your username needs to be under 15 characters"""
                  )
        elif len(user_input) < 1:
            input("""
    Your username is too short. Your username needs to be more than 0
    characters""")
        elif user_input.isalpha():
            break
        else:
            input("""
    Your username doesn't contain any characters. Please use characters""")
    c.execute("INSERT INTO leaderboard VALUES (?, ?, ?, ?, ?)", [
        user_input,
        date.today(), score[0], score[1], score[2],
        ((score[0] + score[1] + score[2]) / 3)
    ])


if __name__ == "__main__":
    from db_create3 import db_create
    leaderboard_entry(db_create(), [int(input()), int(input()), int(input())])
