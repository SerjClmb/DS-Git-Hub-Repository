import random
my_list = []
for i in range(0, 10):
    my_list.append(random.randint(0, 10))
print my_list

similar_numbers = 'no'
for digit in my_list:
    if my_list.count(digit) > 1:
        similar_numbers = 'yes'
        break

print similar_numbers= list(set(my_list)) else print(‘no’)