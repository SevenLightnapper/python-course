# Домашнее задание по теме "Оператор "with"
"""
Задача "Найдёт везде":

Напишите класс WordsFinder, объекты которого создаются следующим образом:

WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).

Объект этого класса должен принимать при создании неограниченного количество названий файлов
и записывать их в атрибут file_names в виде списка или кортежа.

Также объект класса WordsFinder должен обладать следующими методами:
    * get_all_words - подготовительный метод, который возвращает словарь следующего вида:
    {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}

Где:
    1. 'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
    2. ['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.

Алгоритм получения словаря такого вида в методе get_all_words:
    1. Создайте пустой словарь all_words.
    2. Переберите названия файлов и открывайте каждый из них, используя оператор with.
    3. Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
    4. Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке.
       (тире обособлено пробелами, это не дефис в слове).
    5. Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
    6. В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.

find(self, word) - метод, где word - искомое слово.
Возвращает словарь, где ключ - название файла, значение - позиция первого такого слова в списке слов этого файла.

count(self, word) - метод, где word - искомое слово.
Возвращает словарь, где ключ - название файла, значение - количество слова word в списке слов этого файла.

В методах find и count пользуйтесь ранее написанным методом get_all_words
для получения названия файла и списка его слов.
Для удобного перебора одновременно ключа(названия) и значения(списка слов)
можно воспользоваться методом словаря - item().

for name, words in get_all_words().items():
  # Логика методов find или count
"""
import string


class WordsFinder:
    def __init__(self, *file_names: str):
        self.file_names = list(file_names)


    def get_all_words(self) -> dict[str, list[str]]:
        """
        Метод возвращает словарь вида (ключ - название файла, значение - список из слов этого файла):
        {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
        :return: полученный словарь
        """
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read().lower()  # приведение к нижнему регистру
                    # удаление пунктуации
                    for char in string.punctuation:
                        if char != '-':  # сохранение дефиса в словах
                            content = content.replace(char, '')
                    # разбиение строк на слова
                    words = content.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                # если файл не найден, возвращается пустой список для этого файла
                all_words[file_name] = []
        return all_words


    def find(self, word: str) -> dict[str, int]:
        """
        Метод поиска позиции искомого слова.
        :param word: Искомое слово
        :return: словарь, где ключ - название файла,
        значение - позиция первого такого слова в списке слов данного файла
        """
        word = word.lower()
        result_ = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            try:
                # поиск первой позиции слова
                position = words.index(word)
                # +1 для соответствия порядку слов (так отсчет начинается с 1, а не 0)
                result_[file_name] = position + 1
            except ValueError:
                # если слова не найдено, возвращается -1
                result_[file_name] = -1
        return result_


    def count(self, word: str) -> dict[str, int]:
        """
        Метод подсчета вхождений искомого слова в файле.
        :param word: Искомое слово
        :return: словарь, где ключ - название файла,
        значение - количество вхождений искомого слова в данном файле.
        """
        word = word.lower()
        result_ = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            # подсчет вхождений слова
            result_[file_name] = words.count(word)
        return result_


# пример использования №1 - test_file.txt
finder1 = WordsFinder('test_file.txt')
print(finder1.get_all_words())  # Все слова
print(finder1.find('TEXT'))  # 3 слово по счёту
print(finder1.count('teXT'))  # 4 слова teXT в тексте всего

# пример использования №2 - walt_whitman.txt
finder2 = WordsFinder('walt_whitman.txt')
print(finder2.get_all_words())
print(finder2.find('captain'))
print(finder2.count('captain'))

# пример использования №3 - if.txt
finder3 = WordsFinder('if.txt')
print(finder3.get_all_words())
print(finder3.find('if'))
print(finder3.count('if'))

# пример использования №4 - mother_goose.txt
finder4 = WordsFinder('mother_goose.txt',)
print(finder4.get_all_words())
print(finder4.find('Child'))
print(finder4.count('Child'))

# пример использования №5 - 3 files
finder5 = WordsFinder('walt_whitman.txt',
                      'if.txt',
                      'mother_goose.txt')
print(finder5.get_all_words())
print(finder5.find('the'))
print(finder5.count('the'))
