tup = 'Hello'
print(len(tup))
print(type(tup))
tup = 'Hello',
print(len(tup))
print(type(tup))

# the trailing comma after the string 'Hello' turns it into a tuple
# the length of that tuple is 1

# without the trailing comma, it is not a tuple, just a string with 5 characters, hence len 5
