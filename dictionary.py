dict = {'name': 'Rob', 'ref': 'Python', 'sys': 'Windows'}
print('Dictionary Contents -', dict)
print('\nReference -', dict['ref'])
print('\nAll Keys -', dict.keys())

del dict ['name']
dict['user'] = 'Tom'
print('New Dictionary Contents -', dict)
print('\nIS there a "name" key? -', 'name' in dict)
