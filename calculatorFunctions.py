# update to calculatorHistory.py to use functions


def num_input():
    num_string = input("Enter numbers separated by spaces: ")
    num_list = num_string.split(" ")
    return num_list


def operator_input():
    operator = input("Enter an operator (+, -, *, /): ")
    while operator not in operators:  # user input operator with loop to ensure it is supported
        print("Invalid operator.")
        operator = (input("Enter an operator (+, -, *, /): "))
    return operator


def calculations(num_list, operator):
    calc_result = float(num_list[0])  # set the result to the first number (float) in the list
    if operator == "+":
        for i in range(1, len(num_list)):
            x = float(num_list[i])
            calc_result += x
    elif operator == "-":
        for i in range(1, len(num_list)):
            x = float(num_list[i])
            calc_result -= x
    elif operator == "*":
        for i in range(1, len(num_list)):
            x = float(num_list[i])
            calc_result *= x
    elif operator == "/":
        for i in range(1, len(num_list)):
            x = float(num_list[i])
            calc_result /= x
    return calc_result


def formatting(calc_result):  # several if options to format the answer
    if 0 < calc_result < 0.01:
        format_result = "{:1.2E}".format(calc_result)
    elif result > 1000:
        format_result = "{:,}".format(calc_result)
    elif result - int(result) != 0:
        format_result = "{:3.3f}".format(calc_result)
    else:
        format_result = "{:.0f}".format(calc_result)
    return format_result


def view_history():
    for i, key in enumerate(history.keys(), 1):
        print("{} {} {:<10s}".format(key, ": ", history[key]))


history = {}  # set up empty dictionary to hold calculation history and set key to 0
key = 0
operators = ["+", "-", "*", "/"]  # define supported operations
# calculator will loop until user presses Q to quit
menu = input("Press Q to quit. Press any other key to continue. ")
while menu.upper() != "Q":
    key += 1  # increment key for history dict
    numList = num_input()
    inputOp = operator_input()
    result = calculations(numList, inputOp)
    formatResult = formatting(result)
    equation = f'{inputOp.join(numList)} = {formatResult}'
    history[key] = equation
    print(equation)
    # option to quit, view history, or continue
    menu = input("Press Q to quit. Press H to view history. Press any other key to continue. ")
    if menu.upper() == "H":
        view_history()
        menu = input("Press Q to quit. Press H to view history. Press any other key to continue. ")
    else:
        continue
else:
    print("Calculator Quit")
