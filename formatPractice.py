# practice formatting
planets = {'Mercury': 57.91,
           'Venus': 108.2,
           'Earth': 149.597870,
           'Mars': 227.94
}
for i, key in enumerate(planets.keys(), 1):
    print("{:2d} {:<10s} {:06.2f} Gm".format(i, key, planets[key]))

numList = [2, 4, 6, 8, 1, 3, 5, 7, 9]
for i in range(len(numList)):
    print("{:.2f}".format(numList[i]))

numOpStr = "2 + 3 + 5 - 6 - 1"
numOpList = numOpStr.split(" ")
print(numOpList)
calcDict = {numOpList[0]: numOpList[1],
            numOpList[2]: numOpList[3],
            numOpList[4]: numOpList[5],
            numOpList[6]: numOpList[7],
            numOpList[8]: " "
            }
print(calcDict)

for i, key in enumerate(calcDict.keys(), 1):
    print("{:1s} {:<1s}".format(key, calcDict[key]), end=" ")