class Bank:
    # protected bank data
    _total_balance = 0
    _total_loan_amount = 0
    _loan_allowed = True

    def __init__(self, name, address):
        self.name = name
        self.address = address

class Person:    
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Admin(Person, Bank):
    def __init__(self, name, email):
        super().__init__(name, email)

    def create_an_account(self):
        pass
    
    # stop loan feature
    def stop_loan(self):
        Bank._loan_allowed = False

    # display total balance of whole Bank
    def total_balance(self):
        print("Total Bank Balance is", Bank._total_balance)
    
    # display total provided loan amount
    def total_loan_amount(self):
        print("Total Provided Loan is", Bank._total_loan_amount)

class User(Person, Bank):
    def __init__(self, name, email):
        super().__init__(name, email)

    def create_an_account(self):
        self.__balance = 0
        self.history = []

    # deposit balance
    def deposit_balance(self, amount):
        if amount > 0:
            self.__balance += amount
            Bank._total_balance += amount
            self.history.append(f"deposit {amount} taka in his account")

    # withdraw balance  
    def withdraw_balance(self, amount):
        if amount > Bank._total_balance:
            print("The bank is under Bankrupt.")
        else:
            if amount <= self.__balance:
                self.__balance -= amount
                Bank._total_balance -= amount
                self.history.append(f"withdraw {amount} taka from his account")

    # transfer amount
    def transfer_amount(self, amount, receiver):
        if amount <= self.__balance:
            self.__balance -= amount
            receiver.deposit_balance(amount)
            self.history.append(f"Transfer {amount} taka")

    # take a loan
    def take_loan(self, amount):
        if Bank._loan_allowed == False:
            print("You can't take loan from this bank.")
            return
        
        if amount <= self.__balance * 2 and amount <= Bank._total_balance:
            Bank._total_balance -= amount
            Bank._total_loan_amount += amount
            print("Here is your loan", amount)
        else:
            print("Bank does't have sufficient amount of money. Try again later. Thanks to banking with us.")

    # display transaction history of a client
    def transaction_history(self):
        print(f"############ Transaction History of {self.name} ############")
        for history in self.history:
            print(history)
        print("############ Transaction History End ############")

    # display balace of a client
    def available_balance(self):
        print(self.__balance)



user1 = User("mohim", "m@g.com")
user2 = User("harun", "h@g.com")
user3 = User("safi", "sa@g.com")
admin = Admin("morshed", "m@g.com")
admin.create_an_account()
user1.create_an_account()
user2.create_an_account()
user3.create_an_account()
user1.deposit_balance(20000)
user2.deposit_balance(20000)
user3.deposit_balance(20000)
user1.take_loan(40000)
user3.take_loan(20000)
user1.take_loan(10000)
admin.total_balance()
admin.total_loan_amount()
user2.withdraw_balance(10000)
user2.available_balance()
user2.transfer_amount(10000, user3)
user2.available_balance()
user2.transaction_history()
user1.transaction_history()
