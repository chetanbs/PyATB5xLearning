class Bank:

    def __init__(self, account_number, balance):
        self.balance = balance
        self.__account_number = account_number

    def check_balance(self):
        print(self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount

    def show_me_account_number(self, is_auth):
        if is_auth == True:
            print(self.__account_number)
        else:
            print("Not Allowed")

    def __internal_private_method(self):
        print("Private Method, can be access by only Class")

details = Bank (2983740349, 100)
details.deposit(100)
details.check_balance()
print(details.balance)
# print(details.__account_number)  # 'Bank' object has no attribute '__account_number'.
details.show_me_account_number(True)
details.show_me_account_number(False)
# details.__internal_private_method()  # 'Bank' object has no attribute '__internal_private_method'.

# Private variables can be accessed through fuctions