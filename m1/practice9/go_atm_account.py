class Account:

    def __init__(self, name, starting_balance):
        self.account_name = name
        self._balance = starting_balance

    def check_balance(self):
        return self._balance

    def deposit(self, amount):

        if amount > 0:
            self._balance += amount
            return True

        return False

    def withdraw(self, amount):

        if amount > 0 and amount <= self._balance:

            self._balance -= amount

            return True

        return False    