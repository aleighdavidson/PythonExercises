from person import Person


class Customer(Person):
    def __init__(self, first_name: str, last_name: str, dob: list, address: dict, phone: str):
        super().__init__(first_name, last_name, dob, address, phone)


