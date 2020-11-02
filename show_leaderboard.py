"""See show_leaderboard.__doc__."""
from user_binary_choice import user_binary_choice
from get_username import get_username
from clear_screen import clear_screen
from shutil import get_terminal_size


def show_leaderboard(c):
    """Display the leaderboard with an optional username search function.

    Args:
        c:
            The cursor object.
    """
    if user_binary_choice("Do you want to search by username"):
        username = f"%{get_username()}%"
        c.execute(
            """SELECT * FROM `leaderboard`
            WHERE `username` LIKE ?
            ORDER BY `scoretotal` DESC, `username` ASC""", [username])
    else:
        c.execute("""SELECT * FROM `leaderboard`
            ORDER BY `scoretotal`, `username` ASC""")
    clear_screen()
    results = c.fetchall()
    lines = 0
    while lines < len(results):
        print('/' + "¯" * 89 + '\\')
        print(
            f"| {'Username':15} | {'Date':10} | {'Overall Score':13} | {'Maths Score':11} | {'English Score':13} | {'NCEA Score':10} |"
        )
        for x in range(get_terminal_size().lines - 3):
            line = x + lines
            print(
                f"| {results[line][0]:15} | {results[line][1]:10} | {results[line][5]:13} | {results[line][2]:11} | {results[line][3]:13} | {results[line][4]:10} |"
            )
            lines += 1
            if lines + x >= len(results):
                input("(enter to continue)")
                clear_screen()
                return
        while True:
            user_input = input("[q]uit, [n]ew page: ").lower()
            if user_input == 'q':
                clear_screen()
                return
            if user_input == 'n':
                clear_screen()
                break
            print('\033[A', end='')


if __name__ == "__main__":
    from db_create3 import db_create
    show_leaderboard(db_create())
