"""See clear_line.__doc__."""
from shutil import get_terminal_size


def clear_line():
    """Clear the line."""
    print('\033[A' + ' ' * get_terminal_size().columns, end='\033[A ')


if __name__ == "__main__":
    clear_line()
