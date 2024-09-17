# Домашнее задание по теме "Введение в функциональное программирование"
"""
Задача "Вызов разом":

Напишите функцию apply_all_func(int_list, *functions), которая принимает параметры:
    1. int_list - список из чисел (int, float)
    2. *functions - неограниченное кол-во функций (которые применимы к спискам, состоящим из чисел)
Эта функция должна:
    1. Вызвать каждую функцию к переданному списку int_list
    2. Возвращать словарь, где ключом будет название вызванной функции,
       а значением - её результат работы со списком int_list.

Пункты задачи:
    1. В функции apply_all_func создайте пустой словарь results.
    2. Переберите все функции из *functions.
    3. При переборе функций записывайте в словарь results результат работы этой функции под ключом её названия.
    4. Верните словарь results.
    5. Запустите функцию apply_all_func, передав в неё список из чисел и набор других функций.
"""
from typing import List, Dict, Callable


def apply_all_func(int_list: List[float],
                   *functions: Callable[[List[float]], float]) -> Dict[str, float]:
    """
    Применяет набор функций к списку чисел и возвращает словарь с результатами.
    :param int_list: Список чисел (int или float)
    :param functions: Неограниченное количество функций для применения к списку
    :return: Словарь, где ключ — название функции, а значение — результат работы функции с int_list
    """
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results


def sum_list(lst: List[float]):
    """
    Возвращает сумму всех элементов списка.
    :param lst: Список чисел
    :return: Сумма элементов списка
    """
    return sum(lst)


def max_value(lst: List[float]):
    """
    Возвращает максимальное значение из списка.
    :param lst: Список чисел
    :return: Максимальное число в списке
    """
    return max(lst)


def min_value(lst: List[float]):
    """
    Возвращает минимальное значение из списка.
    :param lst: Список чисел
    :return: Минимальное число в списке
    """
    return min(lst)


def avg_value(lst: List[float]) -> float:
    """
    Возвращает среднее значение списка.
    :param lst: Список чисел
    :return: Среднее арифметическое списка
    """
    return sum(lst) / len(lst)

def range_value(lst: List[float]) -> float:
    """
    Возвращает диапазон списка, как разницу между максимальным и минимальным значением.
    :param lst: Список чисел
    :return: Разница между максимальным и минимальным значениями
    """
    return max(lst) - min(lst)

def multiply_list(lst: List[float]) -> float:
    """
    Возвращает произведение всех элементов списка.
    :param lst: Список чисел
    :return: Произведение всех чисел в списке
    """
    product = 1
    for num in lst:
        product *= num
    return product


# пример использования
numbers: List[float] = [1, 2, 3, 4, 5]
result: Dict[str, float] = apply_all_func(numbers,
                                          sum_list, max_value, min_value, avg_value, range_value, multiply_list)

print(f"Result of function '{apply_all_func.__name__}': " + "{")
for key, value in result.items():
    print(f"\t'{key}': {value},")
print("}")