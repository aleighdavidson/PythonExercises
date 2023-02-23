import random


def play_input():
    play_again = input("Do you want to play again? Y for Yes, N for No: ")
    while play_again.upper() not in play_options:
        print("Invalid, try again: ")
        play_again = input("Do you want to play again? Y for Yes, N for No: ")
    return play_again.upper()


def user_input():
    user_choice = input("Enter R (Rock), P (Paper), or S (Scissors): ")
    while user_choice.upper() not in rps_options:
        print("Invalid, try again: ")
        user_choice = input("Enter R (Rock), P (Paper), or S (Scissors): ")
    return user_choice.upper()


def user_conversion(user_choice):
    if user_choice == "R":
        user_word = "Rock"
    if user_choice == "P":
        user_word = "Paper"
    if user_choice == "S":
        user_word = "Scissors"
    return user_word


def computer_input():
    return random.randint(0, 2)


def computer_conversion(computer_choice):
    if computer_choice == 0:
        computer_word = "Rock"
    if computer_choice == 1:
        computer_word = "Paper"
    if computer_choice == 2:
        computer_word = "Scissors"
    return computer_word


def user_wins():
    print("You win! :D")  # try to input a unicode emoji here?


def computer_wins():
    print("You lose :(")


def draw():
    print("It's a draw!")


def referee(user_word, computer_word):
    if user_word == "Rock" and computer_word == "Scissors":
        user_wins()
    elif user_word == "Rock" and computer_word == "Paper":
        computer_wins()
    elif user_word == "Paper" and computer_word == "Rock":
        user_wins()
    elif user_word == "Paper" and computer_word == "Scissors":
        computer_wins()
    elif user_word == "Scissors" and computer_word == "Rock":
        computer_wins()
    elif user_word == "Scissors" and computer_word == "Paper":
        user_wins()
    elif user_word == computer_word:
        draw()


rps_options = ["R", "P", "S"]
play_options = ["Y", "N"]
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
