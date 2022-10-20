import sys, os
# from interface1 import Tui
# import curses
from vendor import Vendor
from art import *


def menu():
    t = input(
        f'---------------------------\nWhat do you want ?\n 1 - Buy can $1.5 (type: 1)\n 2 - Buy peanut $1.0 (type: 2)\n 3 - Maintenance (type: 2)\n 4 - Quit the machine (type: q)\n---------------------------\n>>> '
    )
    return t


def admin_menu():
    t = input(
        f'---------------------------\nWhat do you do ?\n 1 - Display vendor state (type: 1)\n 2 - Add products (type: 2)\n 3 - Take money (type: 3)\n 4 - Quit admin menu (type: 4)\n---------------------------\n>>> '
    )
    return t

def clear_term():
    return print("\033[H\033[J", end="")

def main():
    v = Vendor()
    print(v.is_admin())

    launch = True
    clear_term()
    while launch == True:
        # print('Admin :', v.is_admin())
        art_2 = text2art("MICHI-MACHINE",font='small',chr_ignore=True)
        print(art_2)
        if v.is_admin() == True:
            t = admin_menu()
            if t == 'q':
                launch = False
            elif t == '1':
                print(v)
            elif t == '2':
                amount = input('\n\nHow much cans to add ?\n\n')
                v.add_cans(int(amount))
            elif t == '4':
                v.log_out()
            else:
                print('\n\nI don\'t undestand your request\n\n')
        else:
            t = menu()
            if t == 'q':
                launch = False
            elif t == '1':
                money = input(
                    '\n\nHow much money do you put in the machine ?\n\n')
                v.order(money=float(money), product=1)
            elif t == '2':
                money = input(
                    '\n\nHow much money do you put in the machine ?\n\n')
                v.order(money=float(money), product=2)
            elif t == '3':
                v.auth()
            else:
                print('\n\nI don\'t undestand your request\n\n')
        print('\n\n\n\n')

if __name__ == "__main__":
    main()
