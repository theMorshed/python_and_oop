class Bank:
    total_balance = 0
    total_loan_amount = 0
    __loan_allowed = True

    def __init__(self, name, address):
        self.name = name
        self.address = address
   
    @classmethod
    def stop_loan_permission(self):
        self.__loan_allowed = False

    @classmethod
    def loan_allowed_status(self):
        return self.__loan_allowed

class Person:    
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Admin(Person):
    def __init__(self, name, email):
        super().__init__(name, email)

    def total_available_balance(self):
        return Bank.total_balance
    
    def total_loan_amount(self):
        return Bank.total_loan_amount
    
    def stop_loan(self):
        Bank.stop_loan_permission()

class User(Person):
    def __init__(self, name, email):
        self.__balance = 0
        self.history = []
        super().__init__(name, email)

    def deposit_balance(self, amount):
        if amount > 0:
            self.__balance += amount
            Bank.total_balance += amount
            self.history.append(f"deposit {amount} taka in his account")
        
    def withdraw_balance(self, amount):
        if amount > Bank.total_balance:
            print("The bank is under Bankrupt.")
        else:
            if amount <= self.__balance:
                self.__balance -= amount
                Bank.total_balance -= amount
                self.history.append(f"withdraw {amount} taka from his account")

    def take_loan(self, amount):
        if Bank.loan_allowed_status() == False:
            print("You can't take loan from this bank.")
            return
        
        if amount <= self.__balance * 2 and amount <= Bank.total_balance:
            Bank.total_balance -= amount
            print("Here is your loan", amount)
        else:
            print("Bank does't have sufficient amount of money. Try again later. Thanks to banking with us.")

    def __repr__(self):
        return f"Name: {self.name} and Balance: {self.__balance}"
    
    @property
    def get_balance(self):
        return self.__balance
    
user = User("tapas", "tapas@gmail.com")
admin = Admin("morshed", "morshed@manjur.com")
print(user)
user.deposit_balance(20000)
user.withdraw_balance(1500)
print(user.get_balance)
for history in user.history:
    print(history)
print("Total Balance", Bank.total_balance)
user.take_loan(12000)
user.withdraw_balance(2000)
print("Total Balance", Bank.total_balance)
admin.stop_loan()
user.take_loan(1000)