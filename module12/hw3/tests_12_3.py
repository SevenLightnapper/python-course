import unittest

from runner_and_tournament import Runner, Tournament


# Декоратор для пропуска тестов, если is_frozen = True
def skip_if_frozen(func):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            self.skipTest('Тесты в этом кейсе заморожены')
        return func(self, *args, **kwargs)
    return wrapper


# Обновляем классы тестов
class RunnerTest(unittest.TestCase):
    """ Тесты для класса Runner """

    is_frozen = False  # Эти тесты должны выполняться


    @skip_if_frozen
    def test_walk(self):
        # Создаем объект класса Runner
        runner = Runner("TestRunner")

        # Вызываем метод walk 10 раз
        for _ in range(10):
            runner.walk()

        # Проверяем, что расстояние равно 50
        self.assertEqual(runner.distance, 50)


    @skip_if_frozen
    def test_run(self):
        # Создаем объект класса Runner
        runner = Runner("TestRunner")

        # Вызываем метод run 10 раз
        for _ in range(10):
            runner.run()

        # Проверяем, что расстояние равно 100
        self.assertEqual(runner.distance, 100)


    @skip_if_frozen
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


class TournamentTest(unittest.TestCase):
    """ Тесты для класса Tournament """

    is_frozen = True  # Замороженные тесты


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


    @skip_if_frozen
    def test_tournament_usain_and_nick(self):
        # Создаем объект Tournament для Усэйна и Ника
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()

        # Сохраняем результаты в all_results
        TournamentTest.all_results["Усэйн и Ник"] = results

        # Проверяем, что Ник последний
        self.assertTrue(results[max(results.keys())] == self.nick)


    @skip_if_frozen
    def test_tournament_andrey_and_nick(self):
        # Создаем объект Tournament для Андрея и Ника
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()

        # Сохраняем результаты в all_results
        TournamentTest.all_results["Андрей и Ник"] = results

        # Проверяем, что Ник последний
        self.assertTrue(results[max(results.keys())] == self.nick)


    @skip_if_frozen
    def test_tournament_usain_andrey_and_nick(self):
        # Создаем объект Tournament для Усэйна, Андрея и Ника
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()

        # Сохраняем результаты в all_results
        TournamentTest.all_results["Усэйн, Андрей и Ник"] = results

        # Проверяем, что Ник последний
        self.assertTrue(results[max(results.keys())] == self.nick)
