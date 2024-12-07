from abc import abstractmethod


class BankAccount:

    def __init__(self, balance, acc_number):
        self.__balance = balance
        self.acc_number = acc_number

class BankName(BankAccount):

    def withdraw(self):
        print("Yes")

    @abstractmethod
    def loan(self):
        pass

    @staticmethod
    def call_customer_care():
        print("Calling CustomerCare")