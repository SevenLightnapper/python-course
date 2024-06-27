# Задача 6: Сортировка списка кортежей
"""
Напишите функцию, которая принимает список кортежей,
где каждый кортеж содержит два числа, и возвращает список,
отсортированный по второму числу в каждом кортеже.
"""


# первый вариант (с лямбдой)
def sort_tuples_by_second_element(tuples_):
    return sorted(tuples_, key=lambda x: x[1])


# Пример использования
tuples_list = [(1, 3), (4, 2), (2, 5)]
print("Original list:", tuples_list)
sorted_list = sort_tuples_by_second_element(tuples_list)
print("Sorted list:", sorted_list)


# второй вариант (с доп методом)
def get_second_element(tuple_):
    return tuple_[1]


def sort_tuples_by_second(tuples_):
    return sorted(tuples_, key=get_second_element)


# Пример использования
tuples_list_2 = [(1, 3), (4, 2), (2, 5)]
print("Original list:", tuples_list_2)
sorted_list_2 = sort_tuples_by_second(tuples_list_2)
print("Sorted list:", sorted_list_2)
