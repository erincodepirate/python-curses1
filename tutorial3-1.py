import curses
from curses import wrapper
import time

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_WHITE)
    BLUE_AND_YELLOW = curses.color_pair(1)
    GREEN_AND_BLACK = curses.color_pair(2)
    RED_AND_WHITE = curses.color_pair(3)
    
    counter_win = curses.newwin(1, 20, 10, 10)
    
    for i in range(100):
        counter_win.clear()
        color = BLUE_AND_YELLOW
        if i % 2 == 0:
            color = GREEN_AND_BLACK

        counter_win.addstr(f"Count: {i}", color)
        counter_win.refresh()
        time.sleep(0.1)
    stdscr.getch()

wrapper(main)