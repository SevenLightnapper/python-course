# Задача 3: Обратное слова в предложении
"""
Напишите функцию, которая принимает предложение и возвращает новое предложение,
где каждое слово перевернуто, но порядок слов сохранен.
"""


def reverse_words_in_sentence(string):
    words = string.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)


# Пример использования
sentence = "Hello world in reverse!"
reversed_sentence = reverse_words_in_sentence(sentence)
print(reversed_sentence)
