cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
# this adds each letter as a separate item to the list
# cheese += 'Oke'
# cheese.append(['Oke', 'Brie']) will add the two together in the square brackets as a single item to the list
# cheese.extend(['Oke', 'Brie'])
print(cheese)
# this worked though
cheese += ['Oke', 'Brie']
print(cheese)
# need the square brackets to tell it it's a list? why is it making the string separate elements for each letter?
