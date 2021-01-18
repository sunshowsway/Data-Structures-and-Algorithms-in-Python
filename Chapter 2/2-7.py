class CreditCard:
    def __init__(self, customer, bank, acnt, limit, balance=0):
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = balance

    def charge(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError("price must be numeric")
        if price + self._balance > self._limit:
            return False
        self._balance += price
        return True

    def make_payment(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("amount must be numeric")
        if amount < 0:
            raise ValueError("amount must not be negative")
        self._balance -= amount