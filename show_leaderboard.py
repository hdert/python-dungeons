"""See show_leaderboard.__doc__."""
from out_of_range_error import out_of_range_error
from user_binary_choice import user_binary_choice


def show_leaderboard(c):
    """DooDoo.

    Args:
        c:
            The cursor object.
    """
    if user_binary_choice("Do you want to search by username"):
        while True:
            user_input = input("""
    Please enter the username: """)
            if len(user_input) > 15:
                input("""
    The username is too long. The username needs to be under 15 characters""")
            elif len(user_input) < 1:
                input("""
    The username is too short. The username needs to be more than 0
    characters""")
            elif user_input.isalpha():
                break
            else:
                input("""
    The username doesn't contain any characters. Please use characters""")
        user_input = f"%{user_input}%"
        c.execute(
            """SELECT * FROM `leaderboard`
            WHERE `username` LIKE ?
            ORDER BY `scoreavg`, `username` ASC""", [user_input])
    else:
        c.execute("""SELECT * FROM `leaderboard`
            ORDER BY `scoreavg`, `username` ASC""")
    print(c.fetchall())


if __name__ == "__main__":
    from db_create3 import db_create
    show_leaderboard(db_create())
