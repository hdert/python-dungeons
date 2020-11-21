"""See get_username.__doc__."""


def get_username(stdsrc):
    """Ask the user for their username, validate it and return it.

    Return:
        A string with the validated username.
    """
    while True:
        stdsrc.addstr("""
    Please enter the username: """)
        if len(user_input) > 15:
            input("""
    The username is too long. The username needs to be under 15 characters""")
        elif len(user_input) < 1:
            input("""
    The username is too short. The username needs to be more than 0
    characters""")
        elif user_input.isalnum() and not user_input.isnumeric():
            return user_input
        else:
            input("""
    The username doesn't contain any characters. Please use characters""")


if __name__ == "__main__":
    import curses
    print(get_username(curses.initscr()))
