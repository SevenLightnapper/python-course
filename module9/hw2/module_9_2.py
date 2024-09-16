# Домашнее задание по теме "Списковые, словарные сборки"
"""
Задача:

Даны несколько списков, состоящих из строк:
    * first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
    * second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

1. В переменную first_result запишите список созданный при помощи сборки состоящий из длин строк списка first_strings,
   при условии, что длина строк не менее 5 символов.
2. В переменную second_result запишите список созданный при помощи сборки
   состоящий из пар слов(кортежей) одинаковой длины.
   Каждое слово из списка first_strings должно сравниваться с каждым из second_strings. (два цикла)
3. В переменную third_result запишите словарь созданный при помощи сборки,
   где парой ключ-значение будет строка-длина строки.
   Значения строк будут перебираться из объединённых вместе списков first_strings и second_strings.
   Условие записи пары в словарь - чётная длина строки.
"""

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Список длин строк из first_strings, если длина строки не менее 5 символов
first_result = [len(s) for s in first_strings if len(s) >= 5]

# Список кортежей одинаковой длины слов из first_strings и second_strings
second_result = [(f, s) for f in first_strings for s in second_strings if len(f) == len(s)]

# Словарь, где ключ - строка, значение - длина строки, если длина строки чётная
third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}

print("First result:", first_result, "\n")
print("Second result:", second_result, "\n")
print("Third result:", third_result)
