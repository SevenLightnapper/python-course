# Домашнее задание по теме "Создание функций на лету"
"""
Задача "Функциональное разнообразие":

Lambda-функция:

Даны 2 строки:
    * first = 'Мама мыла раму'
    * second = 'Рамена мало было'
Необходимо составить lambda-функцию для следующего выражения - list(map(?, first, second)).
Здесь ? - место написания lambda-функции.

Результатом должен быть список совпадения букв в той же позиции:
    [False, True, True, False, False, False, False, False, True, False, False, False, False, False]
Где True - совпало, False - не совпало.

Замыкание:

Напишите функцию get_advanced_writer(file_name), принимающую название файла для записи.
Внутри этой функции, напишите ещё одну - write_everything(*data_set),
где *data_set - параметр принимающий неограниченное количество данных любого типа.
Логика write_everything заключается в добавлении в файл file_name всех данных из data_set в том же виде.
Функция get_advanced_writer возвращает функцию write_everything.

Метод __call__:
Создайте класс MysticBall, объекты которого обладают атрибутом words хранящий коллекцию строк.
В этом классе также определите метод __call__,
который будет случайным образом выбирать слово из words и возвращать его.
Для случайного выбора с одинаковой вероятностью для каждого данного в коллекции
можете использовать функцию choice из модуля random.
"""

# №1 LAMBDA-ФУНКЦИЯ
first = 'Мама мыла раму'
second = 'Рамена мало было'

# lambda-функция для сравнения символов на одинаковых позициях
result = list(map(lambda f, s: f == s, first, second))

print(result)


# №2 ЗАМЫКАНИЕ
def get_advanced_writer(file_name: str):
    """
    Функция возвращает другую функцию write_everything, которая записывает переданные данные в файл.
    :param file_name: Имя файла для записи
    :return: Функция write_everything
    """


    def write_everything(*data_set):
        """
        Функция записывает данные из *data_set в файл file_name.
        :param data_set: Неограниченное количество данных для записи
        """
        with open(file_name, 'a') as f:
            for data in data_set:
                f.write(str(data) + '\n')


    return write_everything


# пример использования
writer = get_advanced_writer('example.txt')
writer('Hello', 123, [1, 2, 3], {'key': 'value'})


# №3 МЕТОД __call__
import random
from typing import List


class MysticBall:
    def __init__(self, words: List[str]):
        """
        Инициализация объекта MysticBall с коллекцией слов.
        :param words: Список строк (слов)
        """
        self.words = words


    def __call__(self) -> str:
        """
        Выбирает случайное слово из коллекции и возвращает его.
        :return: Случайно выбранное слово
        """
        return random.choice(self.words)


# пример использования
magic_ball = MysticBall(['Да', 'Нет', 'Может быть', 'Скоро'])
print(magic_ball())  # выведет случайно выбранное слово
print(magic_ball())  # выведет случайно выбранное слово
print(magic_ball())  # выведет случайно выбранное слово
