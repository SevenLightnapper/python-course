#
"""
Задача "Заморозка кейсов":

Подготовка:

В этом задании используйте те же TestCase, что и в предыдущем: RunnerTest и TournamentTest.

Часть 1. TestSuit.
    1. Создайте модуль suite_12_3.py для описания объекта TestSuite.
       Укажите на него переменной с произвольным названием.
    2. Добавьте тесты RunnerTest и TournamentTest в этот TestSuit.
    3. Создайте объект класса TextTestRunner, с аргументом verbosity=2.

Часть 2. Пропуск тестов.
    1. Классы RunnerTest дополнить атрибутом is_frozen = False и TournamentTest атрибутом is_frozen = True.
    2. Напишите соответствующий декоратор к каждому методу (кроме @classmethod), который при значении is_frozen = False будет выполнять тесты, а is_frozen = True - пропускать и выводить сообщение 'Тесты в этом кейсе заморожены'.

Таким образом вы сможете контролировать пропуск всех тестов в TestCase изменением всего одного атрибута.
Запустите TestSuite и проверьте полученные результаты тестов из обоих TestCase
"""
import unittest
from module12.hw3.tests_12_3 import TournamentTest