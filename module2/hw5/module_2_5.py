# Домашняя работа по уроку "Функции в Python. Функция с параметром"
"""
Задача "Матрица воплоти":
Напишите функцию get_matrix с тремя параметрами n, m и value,
которая будет создавать матрицу(вложенный список) размерами n строк и m столбцов,
заполненную значениями value и возвращать эту матрицу в качестве результата работы.

Пункты задачи:
    1. Объявите функцию get_matrix и напишите в ней параметры n, m и value.
    2. Создайте пустой список matrix внутри функции get_matrix.
    3. Напишите первый(внешний) цикл for для кол-ва строк матрицы, n повторов.
    4. В первом цикле добавляйте пустой список в список matrix.
    5. Напишите второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов.
    6. Во втором цикле пополняйте ранее добавленный пустой список значениями value.
    7. После всех циклов верните значение переменной matrix.
    8. Выведите на экран(консоль) результат работы функции get_matrix.
"""


# long solution
def get_matrix_long(rows, cols, fill_value):
    # create an empty list for the matrix
    matrix = []
    # outer loop for rows
    for i in range(rows):
        # add an empty list to the matrix
        _row = []
        matrix.append(_row)
        # inner loop for columns
        for j in range(cols):
            # add the value to the current row
            _row.append(fill_value)
    # returning the resulting matrix
    return matrix


# short solution
def get_matrix_short(rows, cols, fill_value):
    # inner list '[value for _ in range(cols)]' creates a row with 'rows' elements,
    # each of which is equal to 'fill_value'
    # outer list '[[fill_value for _ in range(cols)] for _ in range(rows)]'
    # creates 'cols' such rows, forming the matrix
    return [[fill_value for _ in range(cols)] for _ in range(rows)]


n = int(input("Enter 'n' value: "))     # number of rows
m = int(input("Enter 'm' value: "))     # number of columns
value = input("Enter 'value' value: ")  # value to fill

# print the resulting matrix of long solution
print("Long solution:")
matrix_long = get_matrix_long(n, m, value)
for row in matrix_long:
    print(row)

# print the resulting matrix of short solution
print("Short solution:")
matrix_short = get_matrix_short(n, m, value)
for row in matrix_short:
    print(row)
