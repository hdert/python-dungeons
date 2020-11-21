"""See want_play_again.__doc__."""
from out_of_range_error import out_of_range_error


def want_play_again():
    """Deduce whether the user wants to play again.

    Return:
        A boolean value, True if the user wants to play again, False
        if they do not.
    """
    while True:
        try:
            user_input = int(
                input("""
    Do you want to play again:
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
    print(want_play_again())
