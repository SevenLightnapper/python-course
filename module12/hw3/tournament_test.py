import unittest

from module12.hw3.runner_and_tournament import Runner, Tournament


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
