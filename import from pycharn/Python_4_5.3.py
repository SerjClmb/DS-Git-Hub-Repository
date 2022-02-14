current_health = 500
attack = 80
second_num = 0
while current_health > 0:
    second_num += 1
    current_health -= attack
    print(current_health)
print(second_num)
