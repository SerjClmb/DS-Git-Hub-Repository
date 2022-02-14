matrix_example = [
          [1, 5, 4],
          [4, 2, -2],
          [7, 65, 77]
]

def matrix_sum(matrix1, matrix2):
    matrix_sum = []
    matrix_one_list = []
    if len(matrix1) == len(matrix2):
        for m in range(0, len(matrix1)):
            if len(matrix1[0]) == len(matrix1[m]) == len(matrix2[m]):
                continue
            else:
                return print('Error! Matrices dimensions are different!')
    else:
        return print('Error! Matrices dimensions are different!')



    for i, j in zip(matrix1, matrix2):
        for x, y in zip(i, j):
            while True:
                matrix_one_list.append(x+y)
                if len(matrix_one_list) == len(matrix1[0]):
                    matrix_sum.append(matrix_one_list)
                    matrix_one_list = []
                break

    return matrix_sum


print(matrix_sum(matrix_example, matrix_example))
