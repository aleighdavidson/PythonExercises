from person import Person


class Employee(Person):

    def __init__(self, first_name, last_name, dob, address, phone, ni, salary, dept):
        super().__init__(first_name, last_name, dob, address, phone)
        self._ni = ni
        self._gross_salary = salary
        self.department = dept

    def set_salary(self, gross_salary):
        self._gross_salary = gross_salary

    def get_salary(self):
        return f'£{self._gross_salary}'

    def set_department(self, dept):
        self.department = dept

    def get_department(self):
        return f'{self._first_name} {self._last_name} is in the {self.department} department.'
