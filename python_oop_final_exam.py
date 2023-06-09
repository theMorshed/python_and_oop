class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class User(Person):
    def __init__(self, name, email):
        self.__balance = 0
        self.history = []
        super().__init__(name, email)

    def deposit_balance(self, amount):
        if amount > 0:
            self.__balance += amount
            self.history.append(f"deposit {amount} taka in his account")
        
    def withdraw_balance(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            self.history.append(f"withdraw {amount} taka from his account")

    def take_loan(self):
        print(f"You'll have loan of {self.__balance * 2} takk from this bank.")
        desire = input("Would you like to take loan: ")
        if desire.lower() == "yes":
            print(self.__balance * 2)

    def __repr__(self):
        return f"Name: {self.name} and Balance: {self.__balance}"
    
    @property
    def get_balance(self):
        return self.__balance
    
user = User("tapas", "tapas@gmail.com")
print(user)
user.deposit_balance(20000)
user.withdraw_balance(1500)
print(user.get_balance)
for history in user.history:
    print(history)
user.take_loan()