# Задача 1: Модификация вложенных списков.
"""
Напишите функцию, которая принимает список списков чисел и умножает каждый элемент на 2.
Покажите, как эта функция работает с изменяемыми объектами.
"""


def multiply_nested_list(list_):
    for i in range(len(list_)):
        for j in range(len(list_[i])):
            list_[i][j] *= 2


# Пример использования:
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Nested list:", nested_list)
multiply_nested_list(nested_list)
print("Nested list after multiplying:", nested_list)
