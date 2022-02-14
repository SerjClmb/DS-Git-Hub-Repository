import random
my_list = []
n = 0
for i in range(0, 10):
    my_list.append(random.randint(0, 10))
    print(i)
    for e in my_list:
        if my_list.count(e) > 1 or my_list.count(i) > 1:
            print(my_list)
            n = 1
            break
    if n > 0:
        break
print('Yes')
