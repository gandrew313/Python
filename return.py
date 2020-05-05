num = input('Enter integer')

def square(num):
    if not num.isdigit():
        return 'Invalid Entry'
    num = int(num)
    return num * num

print(num, 'squared is -', square(num))
