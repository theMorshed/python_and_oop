class Product:
    def __init__(self, name, price, quantity) -> None:
        self.product_name = name
        self.product_price = price
        self.product_quantity = quantity

class Store:
    def __init__(self) -> None:
        self.__product_price = {}
        self.__product_quantity = {}
        self.__profit = 0

    def add_product(self, name, price, quantity):
        product = Product(name, price, quantity)
        self.__product_price[product.product_name] = product.product_price
        self.__product_quantity[product.product_name] = product.product_quantity

    def buy_product(self, name, quantity):
        if name in self.__product_price:
            if self.__product_quantity[name] >= quantity:
                self.__profit = self.__profit + ((5 * self.__product_price[name]) / 100) * quantity
                self.__product_quantity[name] = self.__product_quantity[name] - quantity
                print(f"You've successfully buy {name}")
            else:
                print("Product are insufficient amount")

    def display_product(self):
        print("All product price", self.__product_price)
        print("All product quantity", self.__product_quantity)

    def disply_profit(self):
        print("Tota profit", self.__profit)


class Shop(Store):
    def __init__(self, name) -> None:
        self.shop_name = name
        super().__init__()

shop = Shop("Phishop")
shop.add_product("IphoneX", 45000, 40)
shop.add_product("SamsungY", 23000, 24)
shop.display_product()
shop.buy_product("IphoneX", 5)
shop.display_product()
shop.disply_profit()

shop2 = Shop("Jakanaka")
shop2.add_product("Hat", 450, 400)
shop2.display_product()