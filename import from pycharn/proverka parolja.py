user_database = {
    'user': 'password',
    'iseedeadpeople': 'greedisgood',
    'hesoyam': 'tgm'
}
username = input('Enter your login ')
password = input('Enter your password ')

def check_user(username, password):
	if user_database.get(username):
		if user_database.get(password):
			return True
		else:
			return False
	else:
		return False
