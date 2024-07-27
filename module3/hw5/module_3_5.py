# Самостоятельная работа по уроку "Рекурсия"
"""
Задача "Рекурсивное умножение цифр":
Напиши функцию get_multiplied_digits,
которая принимает аргумент целое число number и подсчитывает произведение цифр этого числа.

Пункты задачи:
    1. Напишите функцию get_multiplied_digits и параметр number в ней.
    2. Создайте переменную str_number и запишите строковое представление(str) числа number в неё.
    3. Основной задачей будет отделение первой цифры в числе:
    создайте переменную first и запишите в неё первый символ из str_number в числовом представлении(int).
    4. Возвращайте значение first * get_multiplied_digits(int(str_number[1:])).
    5. Таким образом вы умножите первую цифру числа на результат работы этой же функции с числом,
    но уже без первой цифры. 4 пункт можно выполнить только тогда, когда длина str_number больше 1,
    т.к. в противном случае не получиться взять срез str_number[1:].
    6. Если же длина str_number не больше 1, тогда вернуть оставшуюся цифру first.
Стек вызовов будет выглядеть следующим образом:
get_multiplied_digits(40203) -> 4 * get_multiplied_digits(203) -> 4 * 2 * get_multiplied_digits(3) -> 4 * 2 * 3
"""


def get_multiplied_digits(number):
    # Check if the input is a valid integer
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")

    # Convert the number to a string
    str_number = str(number)

    # Check if the string contains only digits
    if not str_number.isdigit():
        raise ValueError("Input must be a non-negative integer")

    # if the length of the number is 1, return that digit as an integer
    if len(str_number) == 1:
        return int(str_number)

    # Separate the first digit and the rest of the number
    first = int(str_number[0])
    remaining_number = int(str_number[1:])

    # Recursively call the function on the remaining number and multiply the result by the first digit
    return first * get_multiplied_digits(remaining_number)


# Test the function
try:
    result = get_multiplied_digits(40203)
    print(result)
    result = get_multiplied_digits(10)
    print(result)
except ValueError as e:
    print(e)
