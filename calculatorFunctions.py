# update to calculatorHistory.py to use functions
from calcmodule import *

history = {}  # set up empty dictionary to hold calculation history and set key to 0
key = 0
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
        view_history(history)
        menu = input("Press Q to quit. Press H to view history. Press any other key to continue. ")
    else:
        continue
else:
    print("Calculator Quit")
