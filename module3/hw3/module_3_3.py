# Домашнее задание по уроку "Распаковка позиционных параметров"
"""
Задача "Распаковка":
    1.Функция с параметрами по умолчанию:
        - Создайте функцию print_params(a = 1, b = 'строка', c = True),
        которая принимает три параметра со значениями по умолчанию (например сейчас это: 1, 'строка', True).
        - Функция должна выводить эти параметры.
        - Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
        - Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
    2.Распаковка параметров:
        - Создайте список values_list с тремя элементами разных типов.
        - Создайте словарь values_dict с тремя ключами,
        соответствующими параметрам функции print_params, и значениями разных типов.
        - Передайте values_list и values_dict в функцию print_params,
        используя распаковку параметров (* для списка и ** для словаря).
    3.Распаковка + отдельные параметры:
        - Создайте список values_list_2 с двумя элементами разных типов
        - Проверьте, работает ли print_params(*values_list_2, 42)
"""


# Step 1: Create a function with default parameters
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


# Call the function with varying arguments
print_params()
print_params(10)
print_params(10, 'другая строка')
print_params(10, 'другая строка', False)
print_params(b=25)         # works
print_params(c=[1, 2, 3])  # works

# Step 2: Unpacking parameters
values_list = [42, 'пример', False]
values_dict = {'a': 3.14, 'b': 'значение', 'c': None}

print_params(*values_list)
print_params(**values_dict)

# Шаг 3: Unpacking + separate parameters
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
