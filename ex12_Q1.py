cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
# this adds each letter as a separate item to the list
# cheese += 'Oke'
# because it thinks it is a tuple

# cheese.append(['Oke', 'Brie']) will add the two together in the square brackets as a single item to the list
# cheese.extend(['Oke', 'Brie'])
print(cheese)
# this worked though
cheese += ['Oke', 'Brie']
print(cheese)
