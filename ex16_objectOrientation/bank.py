from customer import Customer
from employee import Employee
from basicAccount import Basic
from currentAccount import Current
from savingsAccount import Savings

def print_values(value):
    for i in value:
        print(i, end=" ")
    print("")


customer1_first_name = "Alexandra"
customer1_last_name = "Davidson"
customer1_dob = [14, 10, 1990]
customer1_address = {"House Number": "25",
                     "Street Name": "Wisteria Way",
                     "City": "Solihull",
                     "Country": "UK",
                     "Postcode": "B91 2ST"
                     }
customer1_phone = "07484189876"
customer1 = Customer(customer1_first_name, customer1_last_name, customer1_dob, customer1_address, customer1_phone)
# customer1.change_phone("07484189876")
# customer1.change_address("25", "Wisteria Way", "Solihull", "UK", "B91 2ST")
print(customer1)
print(customer1.get_name())
print(customer1.get_dob())
print(customer1.get_phone())
print(customer1.get_address())

employee1_first_name = "Alexandra"
employee1_last_name = "Davidson"
employee1_dob = [14, 10, 1990]
employee1_address = {"House Number": "25",
                     "Street Name": "Wisteria Way",
                     "City": "Solihull",
                     "Country": "UK",
                     "Postcode": "B91 2ST"
                     }
employee1_phone = "07484189876"
employee1 = Employee(employee1_first_name, employee1_last_name, employee1_dob, employee1_address, employee1_phone)
# employee1.set_salary(40000, "GBP")
# employee1.set_department("Quality")
# employee1_name = employee1.get_name()
# employee1_salary = employee1.get_salary()
#
#
# print(employee1_name)
# print_values(employee1_salary)
# print(employee1.get_department())

# account1 = Basic(10000001, customer1, 250)
# account1.deposit(1000)
# print(account1.get_balance())
# print(account1.get_customer())

# account2 = Savings(10000002, "Joe Blogs", 1000)
# account2.earn_interest()
# print(account2.get_balance())
#
# account3 = Current(10000003, customer1, 100, 100)
# account3.withdrawal(50)
# print(account3.get_balance())
# account3.withdrawal(100)
# print(account3.get_balance())
# account3.withdrawal(100)
# print(account3.get_balance())
