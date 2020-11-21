"""See clear_screen.__doc__."""
from os import system, name


def clear_screen():
    """Clear the screen."""
    if name == 'nt':
        system('cls')
    else:
        system('clear')


if __name__ == "__main__":
    clear_screen()
