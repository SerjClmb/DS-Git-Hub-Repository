value_of_data = int(input('Please, enter value of data: '))
big_user_data = list()

while True:
    users = input('Please enter username: ')
    ages = input('Please enter your age: ')
    emails = input('Please enter your email: ')
    big_user_data.append({'username': users, 'age': ages, 'email': emails})
    value_of_data -= 1
    if value_of_data == 0:
        break

m = 0
data_all = list()
sort_user_data = dict()
value_of_username = []
value_of_age = []
value_of_email = []

value_of_all = []
iter_value_of_all = iter(value_of_all)
list_of_value = []



n = len(big_user_data)
por_num = list(range(1,n+1))

for nums, dicts in zip(por_num, big_user_data):
    data_all.append((nums, dicts))


iter_value = iter(list_of_value)

for i in big_user_data:
    for j in i.values():
        list_of_value.append(j)


        for elem in iter_value:
            m += 1
            if m:
                value_of_username = value_of_username.append(elem)
                value_of_age = value_of_age.append(elem)
                value_of_email = value_of_email.append(elem)
                for c, x in zip(i.keys(), iter_value_of_all):
                    sort_user_data.update({c: x})



print(value_of_username)
print(list_of_value)
print(value_of_all)
print(data_all)
print(sort_user_data)