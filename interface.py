import curses

class Tui():
    def __init__(self) -> None:
        self.stdscr = curses.stdscr
        pass

    def render(self, page):
        curses.wrapper(page)

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
            vendor_art = '$$\    $$\                           $$\                    \n$$ |   $$ |                          $$ |                   \n$$ |   $$ | $$$$$$\  $$$$$$$\   $$$$$$$ | $$$$$$\   $$$$$$\ \n\$$\  $$  |$$  __$$\ $$  __$$\ $$  __$$ |$$  __$$\ $$  __$$\ \n\$$\$$  / $$$$$$$$ |$$ |  $$ |$$ /  $$ |$$ /  $$ |$$ |  \__|\n\$$$  /  $$   ____|$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |       \n\$  /   \$$$$$$$\ $$ |  $$ |\$$$$$$$ |\$$$$$$  |$$ |        \n    \_/     \_______|\__|  \__| \_______| \______/ \__|     \n'

            # start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
            # start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
            # start_x_keystr = int((width // 2) - (len(keystr) // 2) - len(keystr) % 2)
            # start_y = int((height // 2) - 2)

            center_art = int(width // 2) - (len(vendor_art.split('\n')[0]) //2)
            middle_art = int(height // 4)


            stdscr.attron(curses.color_pair(2))
            stdscr.addstr(0, 0, title)
            stdscr.addstr(0, len(title), " " * (width - len(title)))
            stdscr.attroff(curses.color_pair(2))

            stdscr.attron(curses.color_pair(1))
            art = vendor_art.split('\n')
            pos = 1
            for row in art:
                stdscr.addstr(middle_art + pos, center_art, row)
                pos += 1
                # print(row)
            # print(art)
            stdscr.attroff(curses.color_pair(1))

            stdscr.attron(curses.color_pair(3))
            stdscr.addstr('Can - $1.5')
            stdscr.attroff(curses.color_pair(3))

            stdscr.attron(curses.color_pair(2))
            stdscr.addstr(height - 1, 0, control)
            stdscr.addstr(height - 1, len(control), " " * (width - len(control) - 1))
            stdscr.attroff(curses.color_pair(2))

            key = stdscr.getch()
            stdscr.refresh()
