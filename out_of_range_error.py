"""See out_of_range_error.__doc__."""


def out_range_error(length):
    numbers = []
    for i in range(length):
        numbers.append(i + 1)
    input("""
    When prompted, enter one of the numbers {}.
    Each number corresponds to an action printed on screen""".format(
        ", ".join(numbers)))


if __name__ == "__main__":
    print(out_range_error(input()))
