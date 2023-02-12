# calculator will loop until user presses Q to quit
quitQ = input("Press Q to quit. Press any other key to continue. ")
while quitQ.upper() != "Q":
    # user inputs all numbers at once, separated by spaces
    # note that there is no error handling here if user makes mistakes
    # will be problem if any alpha, special characters, or trailing spaces are added
    # note for future - look at trimming whitespace
    numStr = (input("Enter numbers separated by spaces: "))
    # split string into list using space as separator
    numList = numStr.split(" ")
    # define supported operations
    operators = ["+", "-", "*", "/"]
    # user input operator with loop to ensure it is supported
    inputOp = (input("Enter an operator (+, -, *, /): "))
    while inputOp not in operators:
        print("Invalid operator.")
        inputOp = (input("Enter an operator (+, -, *, /): "))
    # set the sum to the first number (float) in the list
    numSum = float(numList[0])
    # if/elif block for each supported operation
    # loops through list from the second number to the end, applying the operator to contribute to the sum/product
    if inputOp == "+":
        for i in range(1, len(numList)):
            x = float(numList[i])
            numSum += x
    elif inputOp == "-":
        for i in range(1, len(numList)):
            x = float(numList[i])
            numSum -= x
    elif inputOp == "*":
        for i in range(1, len(numList)):
            x = float(numList[i])
            numSum *= x
    elif inputOp == "/":
        for i in range(1, len(numList)):
            x = float(numList[i])
            numSum /= x
    # loop to print each number in the list (as string) followed by the operator with spaces
    # exclude the final number in the list as you don't want the operator to follow it
    for i in range(len(numList)-1):
        print(numList[i], inputOp, sep=" ", end=" ")
    # print the final number in the list and an equal sign
    print(f"{numList[-1]} =", end=" ")
    # several if options to format the answer
    if 0 < numSum < 0.01:
        print("{:1.2E}".format(numSum))
    elif numSum > 1000:
        print("{:,}".format(numSum))
    elif numSum - int(numSum) != 0:
        print("{:3.3f}".format(numSum))
    else:
        print("{:.0f}".format(numSum))
    # option to quit or continue
    quitQ = input("Press Q to quit. Press any other key to continue. ")
else:
    print("Calculator Quit")