basket = ['Apple', 'Bun', 'Cola']
crate = ['Egg', 'Fig', 'Grape']

print('Basket List -', basket)
print('Basket elements -', len(basket))

basket.append('Damson')
print('Appended -', basket)
print('Last item removed -', basket.pop())
print('Latest basket list -', basket)

basket.extend(crate)
print('Extended -', basket)
del basket[1]
print('Item removed -', basket)
del basket[1:3] #will actually remove spots 1-2
print('Slice removed', basket)
