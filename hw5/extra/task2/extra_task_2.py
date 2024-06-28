# Задача 2: Копирование изменяемых объектов
"""
Напишите функцию, которая принимает список и возвращает его глубокую копию,
где все вложенные списки также копируются.
"""
import copy


def deepcopy_list(input_list):
    return copy.deepcopy(input_list)


# Пример использования
original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Original list:", original_list)
copied_list = deepcopy_list(original_list)
print("Copied list:", copied_list)

# Изменим оригинальный список и проверим, что копия не изменилась
original_list[0][0] = 100
print("Modified original list:", original_list)
print("Copied list:", copied_list)
