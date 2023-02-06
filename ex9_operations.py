var = input("Please enter a value: ")

print("a) " + var.upper())
print("b) " + str(len(var)))

alphaOnly = var.isalpha()
alphaNum = var.isalnum()

if alphaOnly == True:
    print("c) False")
elif alphaNum == True:
    print("c) True")
else:
    print("c) Maybe??")

# print(var.isdecimal())
# print(var.isalnum())

# print(var.isnumeric())
# print(var.isdecimal())
# print(var.isalnum())
# print(var.isalpha())
# print(var.isdigit())
