"""
У любого продукта есть такие свойства: название, описание, цена, вес

Задания:
    1. Создайте класс продукта.
    2. Создайте экземпляр этого продукта и наполинте своими данными.
    3. Распечатайте о нем иформацию в таком виде: Информация о продукте: название, описание, цена, вес
"""


class Product:
    def __init__(
        self, title: str, description: str, price: float, weight: float
    ) -> None:
        self.title = title
        self.description = description
        self.price = price
        self.weight = weight

    def __str__(self) -> str:
        return f"Информация о продукте: {self.title}, {self.description}, {self.price}, {self.weight}"


if __name__ == "__main__":
    str1 = "Конструкция пишущего узла шариковых ручек представляет собой металлическую трубку из нержавеющей стали."
    str2 = "Между ее стенками располагается маленький вольфрамовый шарик."
    str3 = "Во время его движения по бумаге он «обмазывается» пастообразными чернилами со стороны стержня."
    product = Product(
        title="Ручка шариковая",
        description=f"{str1} {str2} {str3}",
        price=15.55,
        weight=0.01,
    )
    print(product)
