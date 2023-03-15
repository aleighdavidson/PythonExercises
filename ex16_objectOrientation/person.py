class Person:

    def __init__(self, first_name: str, last_name: str, dob: list, address: dict, phone: str):
        self._first_name = first_name
        self._last_name = last_name
        self._dob = dob
        self.address = address
        self.phone_number = phone

    def __str__(self):
        return self.get_name()

    def get_name(self):
        return f'Name: {self._first_name} {self._last_name}'

    def get_dob(self):
        months = ["January", "February", "March", "April", "May",
                  "June", "July", "August", "September", "October", "November", "December"]
        return f'DOB: {self._dob[0]} {months[self._dob[1]]} {self._dob[2]}'

    def set_address(self, house_number, street_name, city, country, postcode):
        self.address = {"House Number": house_number,
                        "Street Name": street_name,
                        "City": city,
                        "Country": country,
                        "Postcode": postcode
                        }

    def get_address(self):
        for i, key in enumerate(self.address.keys(), 1):
            print("{:15s} {:10s}".format(key, self.address[key]))
        # return f'Address: {self.address}'

    def set_phone(self, phone_num):
        self.phone_number = phone_num

    def get_phone(self):
        return f'Phone: {self.phone_number}'

