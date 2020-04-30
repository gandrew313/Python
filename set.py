zoo = ('Kangaroo', 'Leopard', 'Moose')
print('Tuple -', zoo, '\tLength -', len(zoo))
print(type(zoo))

bag = {'Red', 'Green', 'Blue'}
bag.add('Yellow')
print('\nContents of set bag-', bag, '\tLength -', len(bag))
print( type(bag))
print('\nIs Green in set bag? -', 'Green' in bag)
print('Is Orange in set bag? -', 'Orange' in bag)

box = {'Red', 'Purple', 'Yellow'}
print('\nContents of set box -', box, '\tLength of set', len(box))
print('Common to both sets -', bag.intersection(box))
