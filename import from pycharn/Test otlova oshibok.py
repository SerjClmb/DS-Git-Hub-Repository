print('Lets begin!')
try:
    print('Enter data.')
    a = int(input('a: '))
    b = int(input('b: '))
    print('You entered a right number!')
except ValueError:
    print('You entered wrong number!')
finally:
    print("Exit")
