"""See want_leaderboard_entry.__doc__."""

from out_of_range_error import out_of_range_error


def want_leaderboard_entry():  # noqa: D400, D205
    """Deduce whether the user wants their score
    inserted into the leaderboard.

    Return:
        A boolean value, True if the user wants their score insert in the
        leaderboard, False if they do not.
    """
    while True:
        try:
            user_input = int(
                input("""
    Do you want your score saved in the leaderboard:
    1) Yes
    2) No
    [1-2]: """))
        except ValueError:
            out_of_range_error(2)
            user_input = None
        if user_input in (1, 2):
            if user_input == 1:
                return True
            return False
        out_of_range_error(2)


if __name__ == "__main__":
    print(want_leaderboard_entry())
