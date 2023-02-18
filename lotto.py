# want to generate and display 6 random numbers
# the numbers should be between 1 and 50
# import the random module
import random
# # opening statement giving quit instructions
# quitQ = input("Lottery number generator.\nPress Q to quit. Press any other key to continue.")
# # while loop so generator continues until operator quits
# while quitQ.upper() != "Q":
#     lottoList = []
#     # while there are less than 6 numbers in the list, keep going
#     while len(lottoList) < 6:
#         # generate a random integer between 1 and 50, add it to the list
#         lottoNum = random.randint(1, 50)
#         lottoList.append(lottoNum)
#         # turn the list into a set and back to a list to remove duplicates
#         lottoList = list((set(lottoList)))
#     # once we have 6 unique numbers, make a sorted version of the list
#     sortLotto = sorted(lottoList)
#     # instead of printing the list directly [x, y, z, a, b, c], loop through elements and print with "  "
#     for num in sortLotto:
#         print(num, end="  ")
#     # new line before asking operator if they want to generate numbers again
#     print("")
#     quitQ = input("Again? ")
# else:
#     print("Program Quit")
# try with it being a set the whole time
quitQ = input("Lottery number generator.\nPress Q to quit. Press any other key to continue.")
# while loop so generator continues until operator quits
while quitQ.upper() != "Q":
    lottoSet = set()
    # while there are less than 6 numbers in the list, keep going
    while len(lottoSet) < 6:
        # generate a random integer between 1 and 50, add it to the list
        lottoNum = random.randint(1, 50)
        lottoSet.add(lottoNum)
    # once we have 6 unique numbers, make a sorted version of the list
    sortLotto = sorted(lottoSet)
    # instead of printing the list directly [x, y, z, a, b, c], loop through elements and print with "  "
    for num in sortLotto:
        print(num, end="  ")
    # new line before asking operator if they want to generate numbers again
    print("")
    quitQ = input("Again? ")
else:
    print("Program Quit")
