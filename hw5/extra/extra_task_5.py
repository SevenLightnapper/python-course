# Задача 5: Проверка на анаграмму
"""
Напишите функцию, которая принимает две строки и проверяет,
являются ли они анаграммами (содержат одни и те же символы в разном порядке).
"""


def are_anagrams(str_1, str_2):
    return sorted(str_1) == sorted(str_2)


# Пример использования
str1 = "listen"
str2 = "silent"
print(are_anagrams(str1, str2))

str1 = "hello"
str2 = "world"
print(are_anagrams(str1, str2))
