users_list = ['admin', 'ivan', 'ivan_ivan']


def decor(get):
    def decorated():
        x = input('Please enter username: ')
        if x in users_list:
            get()
        else:
            print('This username not found!')
    return decorated


@decor
def get_data_from_database():
    return print("Super secure data from database")


get_data_from_database()
