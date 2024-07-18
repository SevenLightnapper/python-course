# fake_math.py
"""
Функция должна возвращать результат деления first на second,
но когда в second записан 0 - возвращать строку 'Ошибка'.
"""


def divide(first, second):
    if second == 0:
        return 'Ошибка' # Error
    return first / second
