
# Module that allows to read data from bank extract csv
import csv
import codecs
import os
import pprint
import json
from bs4 import BeautifulSoup


class Line():

    def __init__(
            self, date, description, account,
            category, amount, balance):
        self.date = date.strip()
        self.description = ' '.join(description.split())
        self.account = account.strip(' ')
        self.category = category.strip(' ')
        self.amount = self.str_to_number(amount)
        self.balance = self.str_to_number(balance)
        # if self.amount < 0:
        #     self.amount = self.amount * -1

    def str_to_number(self, amount):
        return float(
            ''.join(amount.replace('PLN', '')
                    .replace(',', '.')
                    .strip()
                    .split()))

    def __dict__(self):
        return {
            "date": self.date,
            "description": self.description,
            "account": self.account,
            "category": self.category,
            "amount": self.amount,
            "balance": self.balance,
        }

    def __str__(self):

        str_amount = str(self.amount)
        return f'{self.date}|{self.description}|{self.account}|' \
            f'{self.category}|{str_amount}|{self.balance}'


class Line2():

    def __init__(
            self, date, description, account,
            category, balance, amount):
        # print(len(description))
        self.date = date.strip()
        self.description = ' '.join(description.split())
        self.account = account.strip(' ')
        self.category = category.strip(' ')
        self.amount = self.str_to_number(amount)
        self.balance = self.str_to_number(balance)
        # if self.amount < 0:
        #     self.amount = self.amount * -1

    def str_to_number(self, amount):
        return float(
            ''.join(amount.replace('PLN', '')
                    .replace(',', '.')
                    .strip()
                    .split()))

    def __dict__(self):
        return {
            "date": self.date,
            "description": self.description,
            "account": self.account,
            "category": self.category,
            "amount": self.amount,
            "balance": self.balance,
        }

    def __str__(self):

        str_amount = str(self.amount)
        return f'{self.date}|{self.description}|{self.account}|' \
            f'{self.category}|{str_amount}|{self.balance}'


class TransactionList():

    def __init__(self, path, line):
        self.line = line
        self.balance = 99999
        self.path = path
        self.filename = self.get_file_name()
        self.transactions = []
        self.skipped_lines = []
        # self.read_file()
        self.read_html()
        self.count_balance()

    def read_file(self):

        with codecs.open(self.path, 'r', encoding='windows-1250',
                         errors='ignore') as csvfile:
            linereader = csv.reader(csvfile, delimiter=';')
            for row in linereader:
                try:
                    pprint.pprint(row)
                    print(5*'#')
                    transaction = self.line(row[0], (row[3]),
                                            (row[5]), (row[2]),
                                            (row[7]), (row[6]))
                    print(transaction)
                    self.transactions.append(transaction)
                except Exception as e:
                    self.skipped_lines.append(e)
                    pass

    def read_html(self):

        # read file
        with open(self.path, 'r') as f:
            raw_html = f.read()

        soup = BeautifulSoup(raw_html)

        transactions = soup.table.find_all('table')[3]

        transactions_rows = transactions.find_all('tr', class_=None)

        for row in transactions_rows:
            tds = row.find_all('td')
            print(tds[1])
            try:
                tds[1] = tds[1].replace('<br/>', ' ')
                print(tds[1])
            except:
                pass
            transaction = self.line(
                tds[0].text, tds[1].text, tds[2].text, tds[3].text, tds[5].text, tds[4].text)
            self.transactions.append(transaction)

    def count_balance(self):

        balance = 0
        for transaction in self.transactions:
            balance += transaction.amount
            self.balance = balance

    def get_json(self):
        json_response = [line.__dict__() for line in self.transactions]
        self.count_balance()
        json_response.append({'total': self.balance})
        return json_response

    def get_file_name(self):

        end = len(self.path)
        beg = self.path.rfind('/', 0, end)+1
        return self.path[beg:end]
