"""
У нас есть класс кредитного банковского аккаунта со свойствами: полное имя владельца и баланс.

Задания:
    1. Нужно вынести методы, которые не относится непосредственно к кредитам в отдельны класс BankAccount.
    2. CreditAccount нужно отнаследовать от BankAccount.
    3. Создать экземпляр класс BankAccount и вызвать у него каждый из возможных методов.
    4. Создать экземпляр класс CreditAccount и вызвать у него каждый из возможных методов.
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, amount: float):
        self.balance += amount

    def decrease_balance(self, amount: float):
        self.balance -= amount


class CreditAccount(BankAccount):
    def is_eligible_for_credit(self):
        return self.balance > 1000


if __name__ == "__main__":
    ba1 = BankAccount("Vasya", 1000.99)
    ba1.increase_balance(548.98)
    ba1.decrease_balance(125.54)
    print(f"balance: {ba1.balance}")
    ca1 = CreditAccount("Petya", 465.88)
    ca1.increase_balance(1110.30)
    ca1.decrease_balance(125.00)
    print(
        f"balance: {ca1.balance}, is_eligible_for_credit: {ca1.is_eligible_for_credit()}"
    )
