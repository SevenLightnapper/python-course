#
"""
Задача "План перехват":

Напишите 2 функции:

Функция personal_sum(numbers):
    1. Должна принимать коллекцию numbers.
    2. Подсчитывать сумму чисел в numbers путём перебора и увеличивать переменную result.
    3. Если же при переборе встречается данное типа отличного от числового, то обработать исключение TypeError,
       увеличив счётчик incorrect_data на 1.
    4. В конечном итоге функция возвращает кортеж из двух значений: result - сумма чисел,
       incorrect_data - кол-во некорректных данных.

Функция calculate_average(numbers) Среднее арифметическое - сумма всех данных делённая на их количество.
    1. Должна принимать коллекцию numbers и возвращать: среднее арифметическое всех чисел.
    2. Внутри для подсчёта суммы используйте функцию personal_sum написанную ранее.
    3. Т.к. коллекция numbers может оказаться пустой,
       то обработайте исключение ZeroDivisionError при делении на 0 и верните 0.
    4. Также в numbers может быть записана не коллекция, а другие типы данных, например числа.
       Обработайте исключение TypeError выводя строку 'В numbers записан некорректный тип данных'.
       В таком случае функция просто вернёт None.

Пункты задачи:
    1. Создайте функцию personal_sum на основе условий задачи.
    2. Создайте функцию calculate_average на основе условий задачи.
    3. Вызовите функцию calculate_average несколько раз, передав в неё данные разных вариаций.
"""


def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for item in numbers:
        try:
            result += item
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {item}')

    return result, incorrect_data


def calculate_average(numbers):
    try:
        total_sum, incorrect_data = personal_sum(numbers)  # Используем функцию personal_sum для подсчета
        total_count = len(numbers) - incorrect_data  # Количество числовых данных
        if total_count == 0:  # Проверяем на деление на 0
            return 0
        return total_sum / total_count
    except ZeroDivisionError:
        return 0
    except TypeError:
        print("В numbers записан некорректный тип данных")
        return None


# Примеры использования функции calculate_average
print(calculate_average([1, 2, 3, 4]))  # Ожидается среднее 2.5
print(calculate_average([1, 'a', 3, None, 5]))  # Ожидается среднее 3.0 (1 + 3 + 5) / 3
print(calculate_average([]))  # Ожидается 0 (пустая коллекция)
print(calculate_average(123))  # Некорректный тип данных
print(calculate_average([10, 20, 'string', 30]))  # Ожидается среднее 20.0

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
