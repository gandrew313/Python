a = 1
b = 2

print('\nVariable a is:', 'One' if (a == 1) else 'Not one')
print('\nVariable a is:', 'Even' if (a % 2 == 0) else 'Odd')

print('\nVariable b is:', 'Two' if (b == 2) else 'Not two')
print('\nVariable b is:', 'Even' if (b % 2 == 0) else 'Odd')

max = a if (a > b) else b

print('Greater Value is', max)
