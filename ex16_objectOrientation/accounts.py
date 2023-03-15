class Account:

    def __init__(self, account_number: int, customer: object, balance: float):
        self._account_number = account_number
        self._customer = customer
        self.balance = balance

    def get_customer(self):
        return self._customer

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print(f'£{deposit_amount} added to account {self._account_number}. New balance is £{self.balance}.')

    def withdrawal(self, withdrawal_amount):
        if withdrawal_amount > self.balance:
            print(f'Insufficient funds in account {self._account_number}.')
        else:
            self.balance -= withdrawal_amount
            print(f'£{withdrawal_amount} has been withdrawn from account {self._account_number}. '
                  f'New balance is £{self.balance}.')

    def get_balance(self):
        return self.balance

    def earn_interest(self, interest_rate):
        self.balance = ((interest_rate/100)+1)*self.balance
        return self.balance




