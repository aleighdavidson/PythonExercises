#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# print a line of hyphens the same length as the Belgium string
# considered same length to mean the same number of characters, rather than taking up the same amount of space
for e in Belgium:
    print("-", end="")
print("\n")
# Belgium string with commas replaced with colons
print(Belgium.replace(",", ":"))

# want to add 2nd and 4th entries in the string
# convert string to list using .split
BelgiumList = Belgium.split(",")
print(BelgiumList)
popBelgium = int(BelgiumList[1])
popBrussels = int(BelgiumList[3])
print(popBelgium + popBrussels)


# input1 = input("Enter first number: ")
# print(float(input1))
# try:
#     input1 == float(input1)
# except:
#     print("Not a number.")
#     input1 = input("Enter first number: ")
# else:

i = 0
numList = []
operators = ["+", "-", "*", "/"]
numSum = 0
while i < 2:
    num = input("Enter a number: ")
    if num.isdecimal():
        i += 1
        numList.append(int(num))
        print(numList)
    else:
        print("Not a number or accepted operator.")
        num = input("Enter a number or operator(+, -, *, /): ")
while i < 100:
    num = input("Enter a number or operator (+, -, *, /): ")
    if num.isdecimal():
        i += 1
        numList.append(int(num))
        print(numList)
    elif num in operators:
        break
    else:
        print("Not a number or accepted operator.")
        num = input("Enter a number or operator(+, -, *, /): ")
numSum = numList[0]
if num == "+":
    for i in range(1, i):
        x = numList[i]
        numSum += x
elif num == "-":
    for i in range(1, i):
        x = numList[i]
        numSum -= x
elif num == "*":
    for i in range(1, i):
        x = numList[i]
        numSum *= x
elif num == "/":
    for i in range(1, i):
        x = numList[i]
        numSum /= x
for i in range(0,i):
    print(numList[i], end="")
    print(num, end="")
print(numList[-1], end="")
print("=" + str(numSum))


