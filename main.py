# import curses
# from curses import wrapper
# from curses.textpad import Textbox, rectangle

# def main(stdscr):
#     # Clear screen
#     # stdscr.clear()
#     # jojo = 'Jojo suce'
#     # # This raises ZeroDivisionError when i == 10.
#     # t = 0
#     # for i in jojo:
#     #     stdscr.addstr(t, 10, str(i))
#     #     t += 1

#     # stdscr.refresh()
#     # stdscr.getkey()


#     stdscr.addstr(0, 0, "Enter IM message: (hit Ctrl-G to send)")

#     editwin = curses.newwin(5,30, 2,1)
#     rectangle(stdscr, 1,0, 1+5+1, 1+30+1)
#     stdscr.refresh()

#     box = Textbox(editwin)

#     # Let the user edit until Ctrl-G is struck.
#     box.edit()

#     # Get resulting contents
#     message = box.gather()

# wrapper(main)

import sys,os
from interface import Tui
import curses

def vendor_menu(stdscr):
    key = 0
    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()



    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    while (key != ord('q')):
        height, width = stdscr.getmaxyx() # get the height and width of the terminal

        title = 'Vendor machine v4.206.9'
        message = 'Price of a can : $1.5'
        control = 'Press m for maintenance - Press q to quit'
        vendor_art = f'$$\    $$\                           $$\                    \n$$ |   $$ |                          $$ |                   \n$$ |   $$ | $$$$$$\  $$$$$$$\   $$$$$$$ | $$$$$$\   $$$$$$\ \n\$$\  $$  |$$  __$$\ $$  __$$\ $$  __$$ |$$  __$$\ $$  __$$\ \n\$$\$$  / $$$$$$$$ |$$ |  $$ |$$ /  $$ |$$ /  $$ |$$ |  \__|\n\$$$  /  $$   ____|$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |       \n\$  /   \$$$$$$$\ $$ |  $$ |\$$$$$$$ |\$$$$$$  |$$ |        \n    \_/     \_______|\__|  \__| \_______| \______/ \__|     \n'
        menu = ['Buy', 'Quit']

        # start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        # start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        # start_x_keystr = int((width // 2) - (len(keystr) // 2) - len(keystr) % 2)
        # start_y = int((height // 2) - 2)

        center_art = int(width // 2) - (len(vendor_art.split('\n')[0]) //2)
        middle_art = int(height // 4)

        # statusbar
        stdscr.attron(curses.color_pair(2))
        stdscr.addstr(0, 0, title)
        stdscr.addstr(0, len(title), " " * (width - len(title)))
        stdscr.attroff(curses.color_pair(2))

        # Vendor art display
        stdscr.attron(curses.color_pair(1))
        art = vendor_art.split('\n')
        pos = 1
        for row in art:
            stdscr.addstr(middle_art + pos, center_art, row)
            pos += 1
        stdscr.attroff(curses.color_pair(1))

        # can info
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(middle_art + 10, center_art + len(message) , message, curses.A_BLINK)
        stdscr.attroff(curses.color_pair(3))

        # menu
        stdscr.attron(curses.color_pair(3))
        for i, x in enumerate(menu):
            stdscr.addstr(middle_art + 12, center_art + len(menu[0]) + i * 10, x)
        stdscr.attroff(curses.color_pair(3))

        # controlbar
        stdscr.attron(curses.color_pair(2))
        stdscr.addstr(height - 1, 0, control)
        stdscr.addstr(height - 1, len(control), " " * (width - len(control) - 1))
        stdscr.attroff(curses.color_pair(2))

        key = stdscr.getch()
        stdscr.refresh()


def draw_menu(stdscr):
    k = 0
    cursor_x = 0
    cursor_y = 0

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Loop where k is the last character pressed
    while (k != ord('q')):

        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        if k == curses.KEY_DOWN:
            cursor_y = cursor_y + 1
        elif k == curses.KEY_UP:
            cursor_y = cursor_y - 1
        elif k == curses.KEY_RIGHT:
            cursor_x = cursor_x + 1
        elif k == curses.KEY_LEFT:
            cursor_x = cursor_x - 1

        cursor_x = max(0, cursor_x)
        cursor_x = min(width-1, cursor_x)

        cursor_y = max(0, cursor_y)
        cursor_y = min(height-1, cursor_y)

        # Declaration of strings
        title = "Curses example"[:width-1]
        subtitle = "Written by Clay McLeod"[:width-1]
        keystr = "Last key pressed: {}".format(k)[:width-1]
        statusbarstr = "Press 'q' to exit | STATUS BAR | Pos: {}, {}".format(cursor_x, cursor_y)
        if k == 0:
            keystr = "No key press detected..."[:width-1]

        # Centering calculations
        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        start_x_keystr = int((width // 2) - (len(keystr) // 2) - len(keystr) % 2)
        start_y = int((height // 2) - 2)

        # Rendering some text
        whstr = "Width: {}, Height: {}".format(width, height)
        stdscr.addstr(0, 0, whstr, curses.color_pair(1))

        # Render status bar
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height-1, 0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))

        # Turning on attributes for title
        stdscr.attron(curses.color_pair(2))
        stdscr.attron(curses.A_BOLD)

        # Rendering title
        stdscr.addstr(start_y, start_x_title, title)

        # Turning off attributes for title
        stdscr.attroff(curses.color_pair(2))
        stdscr.attroff(curses.A_BOLD)

        # Print rest of text
        stdscr.addstr(start_y + 1, start_x_subtitle, subtitle)
        stdscr.addstr(start_y + 3, (width // 2) - 2, '-' * 4)
        stdscr.addstr(start_y + 5, start_x_keystr, keystr)
        stdscr.move(cursor_y, cursor_x)

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()

def main():
    curses.wrapper(vendor_menu)

if __name__ == "__main__":
    main()
