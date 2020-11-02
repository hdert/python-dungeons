"""See clear_line.__doc__."""
from shutil import get_terminal_size


def clear_line():
    """Clear the screen."""
    print(' ' * get_terminal_size().columns, end='')


if __name__ == "__main__":
    clear_line()
