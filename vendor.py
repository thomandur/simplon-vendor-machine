from data import Data
from art import *


class Vendor():

    def __init__(self, can_count = 100, can_price = 1.5, peanut_count = 100, peanut_price = 1.0, change = 11.5, password = 'azerty'):
        self.can_count = can_count
        self.can_price = can_price
        self.peanut_count = peanut_count
        self.peanut_price = peanut_price
        self.change = change
        self.password = password
        self.admin = False

        self.data = Data([self.can_count, self.can_price, self.peanut_count, self.peanut_price, self.change])

    def __str__(self):
        return f'---------------------------------------------\n\n\n{self.can_count} cans, Can = {self.can_price}$ \n{self.peanut_count} cans, Peanuts = {self.peanut_price}$ \n{self.change}$ change\n\n\n---------------------------------------------'

    def post(self):
        self.data.post([self.can_count, self.can_price, self.peanut_count, self.peanut_price, self.change])

    def get(self):
        return self.data.get()

    def order(self, money=0, product=1):
        if product == 1:
            product = {'name': 'can', 'count': self.can_count, 'price': self.can_price}
        elif product == 2:
            product = {'name': 'peanut', 'count': self.peanut_count, 'price': self.peanut_price}

        if product['count'] > 0 and money - product['price'] <= self.change:
            if money >= product['price']:
                self.change += product['price']
                product['count'] -= 1
                money_back = 'Money back : $' + str(money - product['price'])  if money > product['price'] else ''
                self.post()
                print(f'One {product["name"]} for you guy !\n{money_back}')
            else:
                print('Not enough money for a can')
        else:
            print('You can\'t buy can, please contact the number on the side.')

        return product['count']

    def add_product(self, product):
        if product == '1':
            amount = input('How many cans ?\n')
            self.add_cans(int(amount))
        elif product == '2':
            amount = input('How many peanuts ?\n')
            self.add_cans(int(amount))
        else:
            print('ERROR : product does not exist')

    def add_cans(self, amount):
        self.can_count += amount
        self.post()

    def add_peanuts(self, amount):
        self.peanut_count += amount
        self.post()

    def auth(self):
        password = input('Password :')
        if self.admin == False:
            if password == self.password:
                self.admin = True
            else:
                print('Wrong password')
        else:
            return True
        return self.admin

    def log_out(self):
        self.admin = False
        return self.admin

    def take_change(self):
        self.change = 0
        self.post()

    def is_admin(self):
        return self.admin
