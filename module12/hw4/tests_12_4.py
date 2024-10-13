#
"""
Задача "Логирование бегунов":
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
Основное обновление - выбрасывание исключений, если передан неверный тип в name и если передано отрицательное значение в speed.

Для решения этой задачи вам понадобиться класс RunnerTest из предыдущей задачи.
В модуле tests_12_4.py импортируйте пакет logging и настройте basicConfig на следующие параметры:
Уровень - INFO
Режим - запись с заменой('w')
Название файла - runner_tests.log
Кодировка - UTF-8
Формат вывода - на своё усмотрение, обязательная информация: уровень логирования, сообщение логирования.

Дополните методы тестирования в классе RunnerTest следующим образом:
test_walk:
Оберните основной код конструкцией try-except.
При создании объекта Runner передавайте отрицательное значение в speed.
В блок try добавьте логирование INFO с сообщением '"test_walk" выполнен успешно'
В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением "Неверная скорость для Runner".
test_run:
Оберните основной код конструкцией try-except.
При создании объекта Runner передавайте что-то кроме строки в name.
В блок try добавьте логирование INFO с сообщением '"test_run" выполнен успешно'
В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением "Неверный тип данных для объекта Runner".
"""
import unittest
import logging
from rt_with_exceptions import Runner


# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(levelname)s: %(message)s'
)


# Декоратор для пропуска тестов, если is_frozen = True
def skip_if_frozen(func):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            self.skipTest('Тесты в этом кейсе заморожены')
        return func(self, *args, **kwargs)
    return wrapper


class RunnerTest(unittest.TestCase):
    """ Тесты для класса Runner """

    is_frozen = False  # Эти тесты должны выполняться


    @skip_if_frozen
    def test_walk(self):
        try:
            # Создаем объект класса Runner с отрицательной скоростью, что вызовет исключение
            runner = Runner("TestRunner", speed=-5)
            # Вызываем метод walk 10 раз
            for _ in range(10):
                runner.walk()

            # Логируем успешное выполнение теста
            logging.info('"test_walk" выполнен успешно')

        except ValueError as e:
            # Логируем исключение
            logging.warning(f"Неверная скорость для Runner: {e}", exc_info=True)


    @skip_if_frozen
    def test_run(self):
        try:
            # Создаем объект класса Runner с неверным типом имени
            runner = Runner(12345, speed=10)  # Это вызовет исключение

            # Вызываем метод run 10 раз
            for _ in range(10):
                runner.run()

            # Логируем успешное выполнение теста
            logging.info('"test_run" выполнен успешно')

        except TypeError as e:
            # Логируем исключение
            logging.warning(f"Неверный тип данных для объекта Runner: {e}", exc_info=True)


# Запуск тестов
if __name__ == '__main__':
    unittest.main()
