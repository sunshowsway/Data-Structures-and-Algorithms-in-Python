class CreditCard:
    def __init__(self, customer, bank, acnt, limit, balance=0):
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = balance

    def get_customer(self):
        return self._customer
    
    def get_bank(self):
        return self._bank

    def get_acnt(self):
        return self._acnt

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

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


if __name__ == "__main__":
    wallet = []
    wallet.append(CreditCard("John Bowman", "California Savings", "5391 0375 9387 5309", 2500))
    wallet.append(CreditCard("John Bowman", "California Federal", "3485 0399 3395 1954", 3500))
    wallet.append(CreditCard("John Bowman", "California Finance", "5391 0375 9387 5309", 5000))

    for val in range(1, 58):  # Causes California Finance CreditCard to exceed limit first
        wallet[0].charge(val)
        wallet[1].charge(val * 2)
        wallet[2].charge(val * 3)

    for card in wallet:
        print("Customer =", card.get_customer())
        print("Bank =", card.get_bank())
        print("Account =", card.get_acnt())
        print("Limit =", card.get_limit())
        print("Balance =", card.get_balance())
        while card.get_balance() > 100:
            card.make_payment(100)
            print("New balance =", card.get_balance())
        print()