#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# print a line of hyphens the same length as the Belgium string
# considered same length to mean the same number of characters, rather than taking up the same amount of space
for e in Belgium:
    print("-", end="")
print("\n")
# another option learned from Maia to use range and len()
for i in range(len(Belgium)):
    print("-", end="")
print("\n")
# Belgium string with commas replaced with colons
print(Belgium.replace(",", ":"))

# want to add 2nd and 4th entries in the string
# convert string to list using .split
BelgiumList = Belgium.split(",")
print(BelgiumList)
popBelgium = int(BelgiumList[1])
popBrussels = int(BelgiumList[3])
print(popBelgium + popBrussels)
