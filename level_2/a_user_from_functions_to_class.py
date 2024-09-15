""" "
У нас есть функции для работы с пользователем, но хочется работать с ним через класс.

Задания:
    1. Создайте класс User и перенесите всю логику работы с пользователем туда.
"""


def make_username_capitalized(username: str):
    return username.capitalize()


def generate_short_user_description(username: str, user_id: int, name: str):
    return f"User with id {user_id} has {username} username and {name} name"


class User:
    def __init__(self, user_id: int, name: str, username: str) -> None:
        self.user_id = user_id
        self.name = name
        self.username = username

    def make_username_capitalized(self) -> str:
        return self.username.capitalize()

    def generate_short_user_description(self) -> str:
        return f"User with id {self.user_id} has {self.username} username and {self.name} name"


if __name__ == "__main__":
    user = User(user_id=1, name="john smith", username="john smith")
    print(
        f"{user.name}, {user.make_username_capitalized()}, {user.generate_short_user_description()}"
    )
