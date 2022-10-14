from data import Data

class Vendor():

    def __init__(self, can_count = 100, can_price = 1.5, change = 0.5, password = 'azerty'):
        self.can_count = can_count
        self.can_price = can_price
        self.change = change
        self.password = password
        self.admin = False

        self.data = Data([self.can_count, self.can_price, self.change])

        print(f'{self.can_count} cans, {self.change}$ change, 1 can = {self.can_price}$')

    def __str__(self):
        return f'{self.can_count} cans, {self.change}$ change, 1 can = {self.can_price}$'

    def post(self):
        self.data.post([self.can_count, self.can_price, self.change])

    def get(self):
        return self.data.get()

    def order_can(self, money = 0):
        if self.can_count > 0 and money - self.can_price <= self.change:
            if money >= 1.5:
                self.change += self.can_price
                self.can_count -= 1
                money_back = 'Money back : $' + str(money - self.can_price)  if money > 1.5 else ''
                self.post()
                print(f'1 can for you guy !\n{money_back}')
            else:
                print('Not enough money for a can')
        else:
            print('You can\'t buy can, please contact the number on the side.')

        return self.can_count

    def add_cans(self, amount):
        self.can_count += amount
        self.post()

    def auth(self):
        password = input('Password :')
        if password == self.password:
            self.admin = True
        # else retourner au menu
        return self.admin

    def take_change(self):
        self.change = 0
        self.post()

class Admin(Vendor):
    def __init__(self, can_count=100, can_price=1.5, change=0.5, password='azerty'):
        super().__init__(can_count, can_price, change, password)
