import getpass

# hard-code the correct PIN
PIN = str(9182)
# attempt counter
attempts = 3
# ask for PIN, check for equality
# while attempts > 0:
#     enteredPIN = getpass.getpass("Enter your PIN: ")
#     if enteredPIN != PIN:
#         attempts -= 1
#         print("Incorrect PIN")
#         print("attempts remaining: " + str(attempts))
#         continue
#     else:
#         print ("PIN OK")
#         break

enteredPIN = getpass.getpass("Enter your PIN: ")
attempts -= 1
while enteredPIN != PIN and attempts > 0:
    print("Incorrect PIN. Attempts remaining: " + str(attempts))
    enteredPIN = getpass.getpass("Enter your PIN: ")
    attempts -= 1
else:
    if enteredPIN == PIN:
        print("PIN OK")
    else:
        print("Attempts remaining: 0. Contact bank.")
