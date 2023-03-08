from rpsmodule import *

play = "Y"
while play.upper() != "N":
    print("Let's play Rock, Paper, Scissors!")
    userChoice = user_input()
    userWord = user_conversion(userChoice)
    computerChoice = computer_input()
    computerWord = computer_conversion(computerChoice)
    print(f"You chose... {userWord} \n Computer chose... {computerWord}.")
    referee(userWord, computerWord)
    play = play_input()
if play == "N":
    print("Thanks for playing! Goodbye!")
