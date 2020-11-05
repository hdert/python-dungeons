"""See show_leaderboard.__doc__."""
from user_binary_choice import user_binary_choice
from get_username import get_username
import curses


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
        ORDER BY `scoretotal` DESC, `username` ASC""")
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    results = c.fetchall()
    lines = 0
    while lines < len(results):
        stdscr.addstr('/' + "¯" * 89 + '\\\n')
        stdscr.addstr(
            "| {:15} | {:10} | {:13} | {:11} | {:13} | {:10} |\n".format(
                'Username', 'Date', 'Overall Score', 'Maths Score',
                'English Score', 'NCEA Score'))
        for x in range(curses.LINES - 3):
            stdscr.addstr(
                "| {:15} | {:10} | {:13} | {:11} | {:13} | {:10} |\n".format(
                    results[lines][0], results[lines][1], results[lines][5],
                    results[lines][2], results[lines][3], results[lines][4]))
            lines += 1
            if lines >= len(results):
                stdscr.addstr("(enter to continue)")
                stdscr.getkey()
                curses.endwin()
                return
        stdscr.addstr("[q]uit, [n]ew page: ")
        while True:
            user_input = stdscr.getkey().lower()
            stdscr.refresh()
            if user_input == 'q':
                curses.endwin()
                return
            if user_input == 'n':
                stdscr.clear()
                break


if __name__ == "__main__":
    from db_create3 import db_create
    show_leaderboard(db_create())
