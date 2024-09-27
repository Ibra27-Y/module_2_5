def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append([value])
    print(matrix)
    return matrix


n = int(input('Задайте строки :'))
m = int(input('Задайте столбцы :'))
value = input('Задайте значение : ')

matrix = get_matrix(n, m, value)

if n <= 0:
    print("Неверное количество строк:", n)
elif m <= 0:
    print("Неверное количество столбцов:", m)
