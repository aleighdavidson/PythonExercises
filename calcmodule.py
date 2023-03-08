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
    elif calc_result > 1000:
        format_result = "{:,}".format(calc_result)
    elif calc_result - int(calc_result) != 0:
        format_result = "{:3.3f}".format(calc_result)
    else:
        format_result = "{:.0f}".format(calc_result)
    return format_result


def view_history(history):
    for i, key in enumerate(history.keys(), 1):
        print("{} {} {:<10s}".format(key, ": ", history[key]))


operators = ["+", "-", "*", "/"]  # define supported operations
