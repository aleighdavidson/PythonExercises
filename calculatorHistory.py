# update to stringCalculator.py which will remember the calculation history and print it on request
# set up empty dictionary to hold calculation history and set key to 0
history = {}
key = 0
# define supported operations
operators = ["+", "-", "*", "/"]
# calculator will loop until user presses Q to quit
menu = input("Press Q to quit. Press any other key to continue. ")
while menu.upper() != "Q":
    # increment key for history dict
    key += 1
    # user inputs all numbers at once, separated by spaces
    # note that there is no error handling here if user makes mistakes
    # will be problem if any alpha, special characters, or trailing spaces are added
    # note for future - look at trimming whitespace
    numStr = (input("Enter numbers separated by spaces: "))
    # split string into list using space as separator
    numList = numStr.split(" ")
    # user input operator with loop to ensure it is supported
    inputOp = (input("Enter an operator (+, -, *, /): "))
    while inputOp not in operators:
        print("Invalid operator.")
        inputOp = (input("Enter an operator (+, -, *, /): "))
    # set the result to the first number (float) in the list
    result = float(numList[0])
    # if/elif block for each supported operation
    # loops through list from the second number to the end, applying the operator to contribute to the sum/product
    if inputOp == "+":
        for i in range(1, len(numList)):
            x = float(numList[i])
            result += x
    elif inputOp == "-":
        for i in range(1, len(numList)):
            x = float(numList[i])
            result -= x
    elif inputOp == "*":
        for i in range(1, len(numList)):
            x = float(numList[i])
            result *= x
    elif inputOp == "/":
        for i in range(1, len(numList)):
            x = float(numList[i])
            result /= x
    # several if options to format the answer
    if 0 < result < 0.01:
        formatResult = "{:1.2E}".format(result)
    elif result > 1000:
        formatResult = "{:,}".format(result)
    elif result - int(result) != 0:
        formatResult = "{:3.3f}".format(result)
    else:
        formatResult = "{:.0f}".format(result)
    # create empty string to hold the equation
    # equation = ""
    # loop to add each number in the list followed by the operator with spaces to an f' string
    # exclude the final number in the list as you don't want the operator to follow it
    # for i in range(i):
    #     equation += f'{numList[i]} {inputOp} '
    # add the final number in the list and an equal sign
    # equation += f"{numList[-1]} = {formatResult}"
    # to avoid looping the string concatenation, just .join
    # note this doesn't allow me to include the spaces around the operator
    equation = f'{inputOp.join(numList)} = {formatResult}'
    history[key] = equation
    print(equation)
    # option to quit, view history, or continue
    menu = input("Press Q to quit. Press H to view history. Press any other key to continue. ")
    if menu.upper() == "H":
        for i, key in enumerate(history.keys(), 1):
            print("{} {} {:<10s}".format(key, ": ", history[key]))
        menu = input("Press Q to quit. Press H to view history. Press any other key to continue. ")
    else:
        continue
else:
    print("Calculator Quit")
