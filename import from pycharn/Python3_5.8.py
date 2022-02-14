a = [1, 11, 11, 23, 45]
number_of_elements_a = len(a)
b = set(a)
b = list(b)
number_of_elements_b = len(b)
print(number_of_elements_a)
print(number_of_elements_b)
if number_of_elements_a != number_of_elements_b:
    print('False')
else:
    print('True')
