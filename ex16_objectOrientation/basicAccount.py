from accounts import Account


class Basic(Account):
    account_type = "Basic"

    def __init__(self, account_number: int, customer: object, balance: float):
        super().__init__(account_number, customer, balance)

    def earn_interest(self, interest_rate=0):
        super().earn_interest(interest_rate)
