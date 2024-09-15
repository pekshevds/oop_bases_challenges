"""
Нам неоюходимо проверить, находится ли фамилия пользователя в списке запрещенных.

Задания:
    1. Cоздайте класс юзера, у которого параметры: имя, фамилия, возраст.
    2. Добавьте ему метод should_be_banned, который проверяет, должен ли быть пользователь забанен.
       Пользователя стоит забанить, если его фамилия находится в SURNAMES_TO_BAN.
"""

SURNAMES_TO_BAN = ["Vaughn", "Wilhelm", "Santaros", "Porter", "Smith"]


class User:
    def __init__(self, name: str, username: str, age: int):
        self.name = name
        self.username = username
        self.age = age

    def should_be_banned(self) -> bool:
        return self.name in SURNAMES_TO_BAN


if __name__ == "__main__":
    user1 = User(name="Smith", username="john smith", age=35)
    print(f"{user1.name} should_be_banned : {user1.should_be_banned()}")

    user2 = User(name="Croft", username="lara croft", age=25)
    print(f"{user2.name} should_be_banned : {user2.should_be_banned()}")
