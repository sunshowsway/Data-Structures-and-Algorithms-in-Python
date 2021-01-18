class CreditCard:
    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = 0

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
        self._balance -= amount