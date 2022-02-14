secret_passwords = {
    'Enot': 'ulybaka',
    'Agent12': '1password1',
    'MouseLulu': 'myshkanaruhka'
}
name = []
password = []
while True:
    name = input('Enter your name: ')
    if name in secret_passwords:
        password = input('Enter your password: ')
        if password == secret_passwords[name]:
            print('Welcome')
            break
        else:
            print('Wrong password!!!')
    else:
        print('Wrong name!!!')
