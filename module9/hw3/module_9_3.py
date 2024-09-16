# Домашнее задание по теме "Генераторные сборки"
"""
Задача:

Дано 2 списка:
    * first = ['Strings', 'Student', 'Computers']
    * second = ['Строка', 'Урбан', 'Компьютер']

Необходимо создать 2 генераторных сборки:
    1. В переменную first_result запишите генераторную сборку,
       которая высчитывает разницу длин строк из списков first и second, если их длины не равны.
       Для перебора строк попарно из двух списков используйте функцию zip.
    2. В переменную second_result запишите генераторную сборку,
       которая содержит результаты сравнения длин строк в одинаковых позициях из списков first и second.
       Составьте эту сборку НЕ используя функцию zip. Используйте функции range и len.
"""


# исходные списки
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# генераторная сборка для разницы длин строк, если их длины не равны
first_result = (len(f) - len(s) for f, s in zip(first, second) if len(f) != len(s))

# генераторная сборка для сравнения длин строк без использования zip
second_result = (len(first[i]) == len(second[i]) for i in range(min(len(first), len(second))))

print("First gen obj:", first_result)
print("Second gen obj:", second_result)

print("First result:", list(first_result))
print("Second result:", list(second_result))