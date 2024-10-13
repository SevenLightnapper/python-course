# Домашнее задание по теме "Методы Юнит-тестирования"
"""
Задача:
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
В этом коде сможете обнаружить дополненный с предыдущей задачи класс Runner и новый класс Tournament.
Изменения в классе Runner:
Появился атрибут speed для определения скорости бегуна.
Метод __eq__ для сравнивания имён бегунов.
Переопределены методы run и walk, теперь изменение дистанции зависит от скорости.
Класс Tournament представляет собой класс соревнований, где есть дистанция, которую нужно пробежать и список участников. Также присутствует метод start, который реализует логику бега по предложенной дистанции.

Напишите класс TournamentTest, наследованный от TestCase. В нём реализуйте следующие методы:

setUpClass - метод, где создаётся атрибут класса all_results. Это словарь в который будут сохраняться результаты всех тестов.
setUp - метод, где создаются 3 объекта:
Бегун по имени Усэйн, со скоростью 10.
Бегун по имени Андрей, со скоростью 9.
Бегун по имени Ник, со скоростью 3.
tearDownClass - метод, где выводятся all_results по очереди в столбец.

Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90. У объекта класса Tournament запускается метод start, который возвращает словарь в переменную all_results. В конце вызывается метод assertTrue, в котором сравниваются последний объект из all_results (брать по наибольшему ключу) и предполагаемое имя последнего бегуна.
Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament соблюсти):
Усэйн и Ник
Андрей и Ник
Усэйн, Андрей и Ник.
Как можно понять: Ник всегда должен быть последним.

Дополнительно (не обязательно, не влияет на зачёт):
В данной задаче, а именно в методе start класса Tournament, допущена логическая ошибка. В результате его работы бегун с меньшей скоростью может пробежать некоторые дистанции быстрее, чем бегун с большей.
Попробуйте решить эту проблему и обложить дополнительными тестами.
"""
import unittest
from module12.hw2.runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        # Создаем атрибут для хранения результатов всех тестов
        cls.all_results = {}


    def setUp(self):
        # Создаем объекты бегунов
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)


    @classmethod
    def tearDownClass(cls):
        # Выводим результаты всех тестов после их завершения
        for test_name, result in cls.all_results.items():
            # Используем имена бегунов для отображения результатов
            finishers = {place: str(participant) for place, participant in result.items()}
            print(f"{test_name}: {finishers}")


    def test_tournament_usain_and_nick(self):
        # Создаем объект Tournament для Усэйна и Ника
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()

        # Сохраняем результаты в all_results
        TournamentTest.all_results["Усэйн и Ник"] = results

        # Проверяем, что Ник последний
        self.assertTrue(results[max(results.keys())] == self.nick)


    def test_tournament_andrey_and_nick(self):
        # Создаем объект Tournament для Андрея и Ника
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()

        # Сохраняем результаты в all_results
        TournamentTest.all_results["Андрей и Ник"] = results

        # Проверяем, что Ник последний
        self.assertTrue(results[max(results.keys())] == self.nick)


    def test_tournament_usain_andrey_and_nick(self):
        # Создаем объект Tournament для Усэйна, Андрея и Ника
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()

        # Сохраняем результаты в all_results
        TournamentTest.all_results["Усэйн, Андрей и Ник"] = results

        # Проверяем, что Ник последний
        self.assertTrue(results[max(results.keys())] == self.nick)


# Запуск тестов
if __name__ == '__main__':
    unittest.main()
