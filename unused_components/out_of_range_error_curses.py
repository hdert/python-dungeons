"""See out_of_range_error.__doc__."""


def out_of_range_error(stdscr, length):  # noqa: D205, D400
    """Print and out of range error message with the list of numbers based on
    the integer length.

    Args:
        length:
            The length of the listing of valid integer inputs.
    """
    numbers = []
    for i in range(length):
        numbers.append(str(i + 1))
    stdscr.addstr("""
    When prompted, enter one of the numbers {}.
    Each number corresponds to an action printed on screen.""".format(
        ", ".join(numbers)))
    stdscr.getkey()


if __name__ == "__main__":
    import curses
    curses.wrapper(out_of_range_error, int(input()))
    curses.endwin()
