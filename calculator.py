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
quitQ = input("Press Q to quit. Press any other key to continue.")
while quitQ.upper() != "Q":
    input1 = input("Enter first number: ")
    while not input1.isdecimal():
        print("Not a number.")
        input1 = input("Enter first number: ")
    else:
        inputOp = input("Choose an operator: + (add), - (subtract), * (multiply), or / (divide): ")
        while inputOp != "+" and inputOp != "-" and inputOp != "*" and inputOp != "/":
            print("Invalid operator.")
            inputOp = input("Choose an operator: + (add), - (subtract), * (multiply), or / (divide): ")
        else:
            input2 = input("Enter second number: ")
            while not input2.isdecimal():
                print("Not a number.")
                input2 = input("Enter second number: ")
            else:
                num1 = int(input1)
                num2 = int(input2)
                if inputOp == "+":
                    ans = str(num1 + num2)
                elif inputOp == "-":
                    ans = str(num1 - num2)
                elif inputOp == "*":
                    ans = str(num1 * num2)
                elif inputOp == "/":
                    ans = str(num1 / num2)
                print(input1 + " " + inputOp + " " + input2 + " = " + ans)
                quitQ = input("Press Q to quit. Press any other key to continue.")
else:
    print("Calculator Quit")
