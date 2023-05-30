# A class is a blueprint of object
class Product:
    def __init__(self, name, price, quantity) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self) -> str:
        return f"Name: {self.name}, price: {self.price}, quantity: {self.quantity}"

product_one = Product("Ergonomic Chair", 50000, 20)
product_two = Product("Height Adjustable Table", 34000, 2)
product_three = Product("Mi Mobile", 34000, 23)

print(product_one)
print(product_two)
print(product_three)

