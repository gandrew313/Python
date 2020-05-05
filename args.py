def echo(user, lang, sys):
    print('User -', user, 'Language -', lang, 'System -', sys)
echo('Mike', 'Python', 'Windows')

echo(lang = 'Python', sys = 'Linux', user = 'Mike')

def mirror(user = 'Carole', lang = 'Python'):
    print('\nUser -', user, 'Language -', lang)

mirror()
mirror(lang = 'Java')
mirror(user = 'Tony')
mirror('Susan', 'C++')
