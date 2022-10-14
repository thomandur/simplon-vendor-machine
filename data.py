import csv
from datetime import datetime


class Data():

    def __init__(self, data) -> None:
        with open('data.csv', mode='w') as csv_file:
            self.fieldnames = ['can_count', 'can_price', 'change', 'datetime']
            writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerow({'can_count': data[0], 'can_price': data[1], 'change': data[2], 'datetime': datetime.today()})

    def get(self):
        with open('data.csv', mode='r') as csv_file:
            reader = csv.DictReader(csv_file, self.fieldnames)
            return list(reader)[-1]

    def post(self, data):
        with open('data.csv', mode='a') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
            writer.writerow({'can_count': data[0], 'can_price': data[1], 'change': data[2], 'datetime': datetime.today()})
