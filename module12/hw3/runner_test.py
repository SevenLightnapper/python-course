import unittest

from module12.hw3.runner_and_tournament import Runner


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
