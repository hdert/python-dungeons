"""See get_username.__doc__."""


def get_username():
    """Ask the user for their username, validate it and return it.

    Return:
        A string with the validated username.
    """
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
            return user_input
        else:
            input("""
    The username doesn't contain any characters. Please use characters""")


if __name__ == "__main__":
    print(get_username())
