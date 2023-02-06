# hard-code the correct PIN
PIN = str(9182)
# attempt counter
attempts = 3
# ask for PIN, check for equality
# while attempts > 0:
#     enteredPIN = input("Enter your PIN: ")
#     if enteredPIN != PIN:
#         attempts = attempts - 1
#         print("Incorrect PIN")
#         print("attempts remaining: " + str(attempts))
#         continue
#     else:
#         print ("PIN OK")
#         break

# but we want to avoid a break
# Without a break, the above code will keep asking user to input PIN even after they get it right
# SUCCESSFUL ATTEMPT!
enteredPIN = input("Enter your PIN: ")
attempts -= 1
while enteredPIN != PIN and attempts > 0:
    print("Incorrect PIN. Attempts remaining: " + str(attempts))
    enteredPIN = input("Enter your PIN: ")
    attempts -= 1
else:
    if enteredPIN == PIN:
        print("PIN OK")
    else:
        print("Attempts remaining: 0. Contact bank.")

# here are a bunch of failed attempts that also resulted in infinite loops without breaks
# while attempts > 0:
#     attempts = attempts - 1
#     enteredPIN = input("Enter your PIN:")
#     if enteredPIN != PIN:
#         print("Incorrect PIN. Attempts remaining: " + str(attempts))
#         continue
#     print("PIN OK")

# enteredPIN = input("Enter your PIN: ")
# if enteredPIN == PIN:
#     print("PIN OK")
# else:
#     while attempts > 0:
#         attempts = attempts - 1
#         print("Incorrect PIN")
#         print("attempts remaining: " + str(attempts))
#         enteredPIN = input("Enter your PIN: ")
#         continue

# enteredPIN = input("Enter your PIN: ")
# if enteredPIN == PIN:
#     print("PIN OK")
# else:
#     while enteredPIN != PIN and attempts > 0:
#         attempts = attempts - 1
#         print("Incorrect PIN")
#         print("attempts remaining: " + str(attempts))
#         enteredPIN = input("Enter your PIN: ")
#     elif enteredPIN == PIN:
#         print("PIN OK")

# enteredPIN = input("Enter your PIN: ")
#     if enteredPIN == PIN:
#         print("PIN OK")
#     elif enteredPIN != PIN:
#         attempts = attempts - 1
#         print("Incorrect PIN")
#         print("attempts remaining: " + str(attempts))
