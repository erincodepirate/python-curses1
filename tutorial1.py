import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(10, 10, "hello world", curses.A_UNDERLINE)
    stdscr.refresh()
    stdscr.getch()

wrapper(main)