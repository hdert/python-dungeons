"""See show_leaderboard.__doc__."""
try:
    import curses
except ModuleNotFoundError:
    from traceback import print_exc
    from sys import exit as sys_exit
    print_exc()
    print("""
    You need to install windows-curses. You can do this through the
    command:
    `python -m pip install windows-curses`""")
    sys_exit()
from fetch_results import fetch_results


def show_leaderboard(c):
    """Display the leaderboard.

    Args:
        c:
            The cursor object.
    """
    results = fetch_results(c)
    if not results:
        return
    try:
        stdscr = curses.initscr()  # initialize the curses window
        curses.noecho()  # make user entered characters not appear
        curses.cbreak()  # make user input instant
        lines = 0
        while lines < len(results):
            stdscr.addstr(
                "| {:15} | {:10} | {:13} | {:11} | {:13} | {:10} |\n".format(
                    'Username', 'Date', 'Overall Score', 'Maths Score',
                    'English Score',
                    'NCEA Score'))  # print the centered header
            for x in range(curses.LINES - 2):
                # do this as many times as the terminal's height - 1
                stdscr.addstr(
                    "| {:15} | {:10} | {:13} | {:11} | {:13} | {:10} |\n".
                    format(results[lines][0], results[lines][1],
                           results[lines][5], results[lines][2],
                           results[lines][3], results[lines][4]))
                # print the results spaced out, line by line
                lines += 1  # iterate the result line to print out
                if lines >= len(results):
                    # if you reach the end of the results, pause, and end the
                    # program
                    stdscr.addstr("(enter to continue)")
                    stdscr.getkey()  # equivalent of input() but for one char
                    curses.endwin()  # close the curses window
                    return
            stdscr.addstr("[q]uit, [n]ew page: ")
            # once the results span the terminal's height - 1 print this prompt
            stdscr.refresh()
            # get curses to display the buffered output
            while True:
                # get the user's input forever until they hit a valid key
                user_input = stdscr.getkey().lower()
                if user_input == 'q':
                    # close the program
                    curses.endwin()
                    return
                if user_input == 'n':
                    # clear the screen and then print a new screen of results
                    stdscr.clear()
                    break
    except KeyboardInterrupt:
        # catch the KeyboardInterrupt, close the curses window, print the
        # traceback, then exit the program. This helps restore terminal
        # control back to the user if they unexpectedly end the program
        from traceback import print_exc
        from sys import exit as sys_exit
        curses.endwin()
        print_exc()
        sys_exit()


if __name__ == "__main__":
    from db_create3 import db_create
    show_leaderboard(db_create())
