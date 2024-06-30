# Задача 4: Частота символов
"""
Напишите функцию, которая принимает строку и возвращает словарь,
где ключи — это символы строки, а значения — частота их появления.
"""


def char_frequency(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency


# Пример использования:
string = "Hello world!!!"
char_freq_map = char_frequency(string)
print(char_freq_map)
