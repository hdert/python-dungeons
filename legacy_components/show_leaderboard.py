"""See show_leaderboard.__doc__."""
from user_binary_choice import user_binary_choice
from get_username import get_username
from clear_screen import clear_screen
from shutil import get_terminal_size
from clear_line import clear_line


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
        c.execute("""SELECT * FROM `leaderboard`""")
    clear_screen()
    results = c.fetchall()
    lines = 0
    while lines < len(results):
        print('/' + "¯" * 89 + '\\')
        print("| {:15} | {:10} | {:13} | {:11} | {:13} | {:10} |".format(
            'Username', 'Date', 'Overall Score', 'Maths Score',
            'English Score', 'NCEA Score'))
        for x in range(get_terminal_size().lines - 3):
            print("| {:15} | {:10} | {:13} | {:11} | {:13} | {:10} |".format(
                results[lines][0], results[lines][1], results[lines][5],
                results[lines][2], results[lines][3], results[lines][4]))
            lines += 1
            if lines >= len(results):
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
            clear_line()


if __name__ == "__main__":
    from db_create3 import db_create
    show_leaderboard(db_create())
