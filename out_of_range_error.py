"""See out_of_range_error.__doc__."""


def out_of_range_error(length):  # noqa: D205, D400
    """Print and out of range error message with the list of numbers based on
    the variable length.

    Args:
        length:
            The length of the listing of valid integer inputs.
    """
    numbers = []
    for i in range(length):
        numbers.append(str(i + 1))
    input("""
    When prompted, enter one of the numbers {}.
    Each number corresponds to an action printed on screen.""".format(
        ", ".join(numbers)))


if __name__ == "__main__":
    print(out_of_range_error(int(input())))
