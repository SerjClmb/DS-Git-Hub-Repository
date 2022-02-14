test_matrix1 = [
    [1, 2, 3],
    [7, -1, 2],
    [123, 2, -1],
    [123, 5, 1]
]
sum_i = len(test_matrix1)
sum_j = len(test_matrix1[0])
s_j = 0
j_kol = []
for i in range(sum_i):
    s_j = 0
    for j in range(sum_j):
        s_j += 1
    j_kol.append(s_j)
    print(s_j)
if j_kol.count(sum_i) == sum_i:
    print('True')
else:
    print('False')
