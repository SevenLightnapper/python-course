# Домашнее задание по теме "Простые Юнит-Тесты"
"""
Задача "Проверка на выносливость":

В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
В этом коде сможете обнаружить класс Runner, объекты которого вам будет необходимо протестировать.

Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest. В классе пропишите следующие методы:
    1. test_walk - метод, в котором создаётся объект класса Runner с произвольным именем.
       Далее вызовите метод walk у этого объекта 10 раз.
       После чего методом assertEqual сравните distance этого объекта со значением 50.
    2. test_run - метод, в котором создаётся объект класса Runner с произвольным именем.
       Далее вызовите метод run у этого объекта 10 раз.
       После чего методом assertEqual сравните distance этого объекта со значением 100.
    3. test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами.
       Далее 10 раз у объектов вызываются методы run и walk соответственно.
       Т.к. дистанции должны быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.

Запустите кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку.

Пункты задачи:
    1. Скачайте исходный код для тестов.
    2. Создайте класс RunnerTest и соответствующие описанию методы.
    3. Запустите RunnerTest и убедитесь в правильности результатов.
"""
from module12.hw1.runner import Runner
import unittest


class RunnerTest(unittest.TestCase):
    """ Тесты для класса Runner """

    def test_walk(self):
        # Создаем объект класса Runner
        runner = Runner("TestRunner")

        # Вызываем метод walk 10 раз
        for _ in range(10):
            runner.walk()

        # Проверяем, что расстояние равно 50
        self.assertEqual(runner.distance, 50)


    def test_run(self):
        # Создаем объект класса Runner
        runner = Runner("TestRunner")

        # Вызываем метод run 10 раз
        for _ in range(10):
            runner.run()

        # Проверяем, что расстояние равно 100
        self.assertEqual(runner.distance, 100)


    def test_challenge(self):
        # Создаем два объекта класса Runner
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")

        # Runner1 бегает, Runner2 ходит
        for _ in range(10):
            runner1.run()
            runner2.walk()

        # Проверяем, что дистанции разные
        self.assertNotEqual(runner1.distance, runner2.distance)


# Запуск тестов
if __name__ == '__main__':
    unittest.main()
