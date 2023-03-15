from accounts import Account


class Current(Account):
    account_type = "Current"

    def __init__(self, account_number: int, customer: object, balance: float, overdraft: float):
        super().__init__(account_number, customer, balance)
        self.overdraft = overdraft

    def earn_interest(self, interest_rate=1.25):
        super().earn_interest(interest_rate)

    def withdrawal(self, withdrawal_amount):
        if withdrawal_amount > self.balance + self.overdraft:
            print(f'Insufficient arranged overdraft to cover withdrawal.')
        elif withdrawal_amount > self.balance:
            self.balance -= withdrawal_amount
            print(f'You are now using your arranged overdraft for account {self._account_number}. '
                  f'New balance is £{self.balance}.')
        else:
            super().withdrawal(withdrawal_amount)
