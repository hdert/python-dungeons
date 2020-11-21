"""See user_binary_choice.__doc__."""

from out_of_range_error_curses import out_of_range_error


def user_binary_choice(stdscr, x):  # noqa: D400, D205
    """Deduce whether the user wants x to happen

    Args:
        x:
            The thing that the program wants to find out if the user wants
    Return:
        A boolean value, True if the user wants x, False if they do not.
    """
    while True:
        try:
            print(f"""
    {x}:
    1) Yes
    2) No
    [1-2]: """)
            user_input = int(stdscr.getkey())
        except ValueError:
            out_of_range_error(stdscr, 2)
            return user_binary_choice(stdscr, x)
        if user_input in (1, 2):
            if user_input == 1:
                return True
            return False
        out_of_range_error(stdscr, 2)


if __name__ == "__main__":
    import curses
    print(curses.wrapper(user_binary_choice, input()))
    curses.endwin()
