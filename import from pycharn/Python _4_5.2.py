import random
my_list = []
sum = 0
i = -1
while True:
    i += 1
    my_list.append(random.randint(0, 10))
    if sum < 10:
        print(my_list)
        sum += my_list[i]
        if sum >= 10:
            print(sum)
            break
