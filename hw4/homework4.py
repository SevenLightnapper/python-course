# Практическая работа по уроку "Организация программ и методы строк."
"""
1. Организуйте программу:

    - Создайте переменную my_string и присвойте ей значение строки с произвольным текстом (функция input()).
    - Вывести количество символов введённого текста

2. Работа с методами строк:
Используя методы строк, выполните следующие действия:

    - Выведите строку my_string в верхнем регистре.
    - Выведите строку my_string в нижнем регистре.
    - Измените строку my_string, удалив все пробелы.
    - Выведите первый символ строки my_string.
    - Выведите последний символ строки my_string.
"""
my_string = input("Enter an arbitrary line: ")
print("Amount of symbols in the input string:", len(my_string))
print("Input string in upper case:", my_string.upper())
print("Input string in lower case:", my_string.lower())
print("Input string without spaces:", my_string.replace(" ", ""))
print("First symbol of the input string:", my_string[0])
print("Last symbol of the input string:", my_string[-1])
