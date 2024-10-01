"""
У нас есть класс Product, который подходит для многих продуктов, но не для еды.
В пищевом продукте нам нужно хранить еще срок годности, который будет влиять и на другие методы

Задания:
    1. Переопределите частично метод __init__ у FoodProduct так, чтобы там хранилось еще свойство expiration_date.
       Используйте super() для этого.
    2. Переопределите у FoodProduct полностью метод get_full_info, чтобы он возвращал еще и информацию о сроке годности
    3. Переопределите частично метод is_available у FoodProduct, чтобы там учитывался еще и срок годности. Если он
       меньше чем текущая дата - то is_available должен возвращать False. Используйте super() для этого.
    3. Создайте экземпляры каждого из двух классов и вызовите у них все доступные методы
"""

from datetime import datetime


class Product:
    def __init__(self, title, quantity):
        self.title = title
        self.quantity = quantity

    def get_full_info(self):
        return f"Product {self.title}, {self.quantity} in stock."

    def is_available(self):
        return self.quantity > 0


class FoodProduct(Product):
    def __init__(self, title, quantity, expiration_date):
        super().__init__(title, quantity)
        self.expiration_date = expiration_date

    def get_full_info(self):
        formated_date = datetime.strftime(self.expiration_date, "%Y-%M-%d")
        return f"FoodProduct {self.title}, {self.quantity}, {formated_date} in stock."

    def is_available(self):
        return super().is_available() and self.expiration_date > datetime.now()


if __name__ == "__main__":
    product = Product("Пила", 12)
    print(product.get_full_info())
    print(f"is available {product.is_available()}")

    food_product = FoodProduct("Молоко", 0, datetime.strptime("2024-10-15", "%Y-%M-%d"))
    print(food_product.get_full_info())
    print(f"is available {food_product.is_available()}")
