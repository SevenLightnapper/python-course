# Дополнительное практическое задание по модулю: "Подробнее о функциях."
"""
Задание "Раз, два, три, четыре, пять .... Это не всё?":
Все ученики урбана, без исключения, — очень умные ребята.
Настолько умные, что иногда по утру сами путаются в том, что намудрили вчера вечером.
Один из таких учеников уснул на клавиатуре в процессе упорной учёбы (ещё и трудолюбивые).
Тем не менее, даже после сна, его код остался рабочим и выглядел следующим образом:

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

Увидев это студент задался вопросом: "А есть ли универсальное решение для подсчёта суммы всех чисел и длин всех строк?"
Да, выглядит страшно, да и обращаться нужно к каждой внутренней структуре (списку, словарю и т.д.) по-разному.

Ученику пришлось каждый раз использовать индексацию и обращение по ключам -
универсального решения для таких структур он не нашёл.

Помогите сокурснику осуществить его задумку.

Что должно быть подсчитано:
    - Все числа (не важно, являются они ключами или значениям или ещё чем-то).
    - Все строки (не важно, являются они ключами или значениям или ещё чем-то)

Для примера, указанного выше, расчёт вёлся следующим образом:
1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99
"""


def calculate_sum_and_length(data):
    """
    Function calculates the sum of all integers and the total length of all strings
    in a data structure.
    Contains a nested function process_element(element):
        Function recursively processes elements of various data types
        to calculate the sum of integers and the total length of strings.

    :param data: elements of different types
    :return: 1. sum of all numbers in data
             2. length of all strings in data
             3. sum of all numbers and string lengths in data
    """
    total_sum = 0
    total_length = 0

    # Recursive function for processing different data types
    def process_element(element):
        nonlocal total_sum, total_length
        if isinstance(element, int):
            total_sum += element
        elif isinstance(element, str):
            total_length += len(element)
        elif isinstance(element, (list, tuple, set)):
            for item in element:
                process_element(item)
        elif isinstance(element, dict):
            for key, value in element.items():
                process_element(key)
                process_element(value)

    process_element(data)

    return total_sum, total_length, total_sum + total_length


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_sum_and_length(data_structure)
print(f"Sum of all numbers: {result[0]}")
print(f"Total length of all strings: {result[1]}")
print(f"Total sum of all numbers and string lengths: {result[2]}")
# print(calculate_sum_and_length.__doc__)
