"""
У нас есть класс UserManager, который содержит в себе спискок юзернэймов пользователей и может расширять этот список.

Задания:
    1. Создайте класс AdminManager, который будет наследником UserManager.
       У него должен быть свой уникальный метод ban_username, который по переданному в него юзернэйму будет удалять
       юзернэйм из списка. Если такого юзернэйма в списке нет - должно печататься сообщение: "Такого пользователя не существует."
    2. Создайте класс SuperAdminManager, который будет наследником AdminManager.
       У него должен быть свой уникальный метод ban_all_users, который будет удалять все юзернэймы из списка.
    3. Создайте экземпляры каждого из трех классов и у каждого экземпляра вызовите все возможные методы.
"""


class UserManager:
    def __init__(self):
        self.usernames = []

    def add_user(self, username):
        self.usernames.append(username)

    def get_users(self):
        return self.usernames


class AdminManager(UserManager):
    def ban_username(self, username: str):
        if username not in self.get_users():
            print("Такого пользователя не существует.")
            return
        self.usernames.remove(username)


class SuperAdminManager(AdminManager):
    def ban_all_users(self):
        self.usernames.clear()


if __name__ == "__main__":
    um1 = UserManager()
    um1.add_user("Vasya")
    um1.add_user("Petya")
    um1.add_user("Slava")

    am1 = AdminManager()
    am1.add_user("Vasya")
    am1.add_user("Petya")
    am1.add_user("Slava")
    am1.ban_username("Slava")
    am1.ban_username("Tolya")

    sam1 = SuperAdminManager()
    sam1.add_user("Vasya")
    sam1.add_user("Petya")
    sam1.add_user("Slava")
    sam1.ban_username("Slava")
    sam1.ban_username("Tolya")
    sam1.ban_all_users()
