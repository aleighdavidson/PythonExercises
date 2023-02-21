# # Simple, no checks, addition only
# # ask user to input two numbers
# input_1 = input("Enter a number:")
# input_2 = input("Enter another number:")
#
# # turn inputs into floats
# number1 = float(input_1)
# number2 = float(input_2)
#
# sumOfInputs = number1 + number2
# print("Sum of previous two numbers: " + str(sumOfInputs))

# # Looped, four operations, checks inputs are numbers
# quitQ = input("Press Q to quit. Press any other key to continue.")
# while quitQ.upper() != "Q":
#     input1 = input("Enter first number: ")
#     while not input1.isdecimal():
#         print("Not a number.")
#         input1 = input("Enter first number: ")
#     else:
#         inputOp = input("Choose an operator: + (add), - (subtract), * (multiply), or / (divide): ")
#         while inputOp != "+" and inputOp != "-" and inputOp != "*" and inputOp != "/":
#             print("Invalid operator.")
#             inputOp = input("Choose an operator: + (add), - (subtract), * (multiply), or / (divide): ")
#         else:
#             input2 = input("Enter second number: ")
#             while not input2.isdecimal():
#                 print("Not a number.")
#                 input2 = input("Enter second number: ")
#             else:
#                 num1 = int(input1)
#                 num2 = int(input2)
#                 if inputOp == "+":
#                     print(num1 + num2)
#                 elif inputOp == "-":
#                     print(num1 - num2)
#                 elif inputOp == "*":
#                     print(num1 * num2)
#                 elif inputOp == "/":
#                     print(num1 / num2)
#                 quitQ = input("Press Q to quit. Press any other key to continue.")
# else:
#     print("Calculator Quit")

# Looped, as above, also prints the operation out
# quitQ = input("Press Q to quit. Press any other key to continue.")
# while quitQ.upper() != "Q":
#     input1 = input("Enter first number: ")
#     while not input1.isdecimal():
#         print("Not a number.")
#         input1 = input("Enter first number: ")
#     else:
#         inputOp = input("Choose an operator: + (add), - (subtract), * (multiply), or / (divide): ")
#         while inputOp != "+" and inputOp != "-" and inputOp != "*" and inputOp != "/":
#             print("Invalid operator.")
#             inputOp = input("Choose an operator: + (add), - (subtract), * (multiply), or / (divide): ")
#         else:
#             input2 = input("Enter second number: ")
#             while not input2.isdecimal():
#                 print("Not a number.")
#                 input2 = input("Enter second number: ")
#             else:
#                 num1 = int(input1)
#                 num2 = int(input2)
#                 if inputOp == "+":
#                     ans = str(num1 + num2)
#                 elif inputOp == "-":
#                     ans = str(num1 - num2)
#                 elif inputOp == "*":
#                     ans = str(num1 * num2)
#                 elif inputOp == "/":
#                     ans = str(num1 / num2)
#                 print(input1 + " " + inputOp + " " + input2 + " = " + ans)
#                 quitQ = input("Press Q to quit. Press any other key to continue.")
# else:
#     print("Calculator Quit")

# 10 Feb 2023 update
# let the user enter as many numbers they want and perform the selected operation on all of them.
# Or, let the user enter more than just one operator and perform the operations on all supplied numbers.
# You can also practice your formatting - rather than printing just the result, print out all the operations in a neat way.
# included operators list
# idea for multiple numbers: add them to a list?

# calculator will loop until user presses Q to quit
quitQ = input("Press Q to quit. Press any other key to continue.")
while quitQ.upper() != "Q":
    # define i (counter) as 0
    i = 0
    # create an empty list to collect the input numbers
    numList = []
    # define list of supported operators
    operators = ["+", "-", "*", "/"]
    op = ""
    # need at least 2 numbers before asking for operator so start with a small loop
    while i < 2:
        num = input("Enter a number: ")
        # check if input is a number (accepts integers only)
        if num.isdecimal():
            # if it .isdecimal, increase counter and add it (as an integer) to the list
            i += 1
            numList.append(int(num))
        else:
            # otherwise, ask again
            print("Not a number.")
    # now we have 2 numbers, we are asking for a number or operator
    # could change to while i > 2 but that could be infinite, assuming 100 is well above what anyone would need
    while i >= 2:
        num = input("Enter a number or operator (+, -, *, /): ")
        # if input .isdecimal, increase counter, add to list
        if num.isdecimal():
            i += 1
            numList.append(int(num))
        # if input is one of the defined operators, break this loop of asking for numbers
        elif num in operators:
            op = num
            break
        # otherwise (e.g. a letter or non-operation character was entered), ask again
        else:
            print("Not a number or accepted operator.")
    # start the sum/product off with the first number in the list
    result = numList[0]
    # series of if/elif blocks for each operation
    # loop through the list, adding each number to the sum (or subtracting, multiplying, etc)
    if op == "+":
        for i in range(1, i):
            result += numList[i]
    elif op == "-":
        for i in range(1, i):
            result -= numList[i]
    elif op == "*":
        for i in range(1, i):
            result *= numList[i]
    elif op == "/":
        for i in range(1, i):
            result /= numList[i]
    # loop to print each number in the list followed by the operator with spaces
    # exclude the final number in the list as you don't want the operator to follow it
    for i in range(i):
        print(numList[i], op, end=" ")
    # print the final number in the list (same line as other numbers)
    print(numList[-1])
    # print an equal sign on the next line, with no line break before the answer
    print("=", end=" ")
    # several if options to format the answer
    if 0 < result < 0.01:
        print("{:1.2E}".format(result))
    elif result > 1000:
        print("{:,}".format(result))
    elif result - int(result) != 0:
        print("{:3.3f}".format(result))
    else:
        print("{:.0f}".format(result))
    # option to quit or continue
    quitQ = input("Press Q to quit. Press any other key to continue.")
else:
    print("Calculator Quit")
