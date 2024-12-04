"""Classes & Objects in Python"""


class Account:
    """Class Account!"""

    account_type = 'Normal Savings'

    def __init__(self, initial_amount: float) -> None:
        self.pub = True  # public property
        self._pro = True  # protected property (_)
        if initial_amount > 0:
            self.__balance = initial_amount  # private property
        else:
            raise ValueError('you can not have a negative balance')

    def deposit(self, amount: float) -> None:
        """Deposite method"""
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError('you can not deposit negative amount')

    def withdraw(self, amount):
        """withdraw method"""
        if amount < 0 or amount > self.__balance:
            raise ValueError('you can not withdraw')
        else:
            self.__balance -= amount

    def get_balance(self) -> float:
        """return available balance"""
        return self.__balance


try:
    my_account = Account(1000)
    # print(my_account._pro)
    print(f"initial balance: {my_account.get_balance()}")
    print('depositing 300')
    my_account.deposit(300)
    balance = my_account.get_balance()
    print(f"Available balance: {balance}")
    print('withdrawing: 400')
    my_account.withdraw(400)
    balance = my_account.get_balance()
    print(f"Available balance: {balance}")
except ValueError as e:
    print(f"Something went wrong: {e}")
