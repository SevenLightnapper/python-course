# Домашнее задание по теме "Создание исключений"
"""
Задача "Некорректность":

Создайте 3 класса (2 из которых будут исключениями):

Класс Car должен обладать следующими свойствами:
    1. Атрибут объекта model - название автомобиля (строка).
    2. Атрибут объекта __vin - vin номер автомобиля (целое число). Уровень доступа private.
    3. Метод __is_valid_vin(vin_number) - принимает vin_number и проверяет его на корректность.
       Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
    4. Атрибут __numbers - номера автомобиля (строка).
    5. Метод __is_valid_numbers(numbers) - принимает numbers и проверяет его на корректность.
       Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
    6. Классы исключений IncorrectVinNumber и IncorrectCarNumbers,
       объекты которых обладают атрибутом message - сообщение, которое будет выводиться при выбрасывании исключения.

Работа методов __is_valid_vin и __is_valid_numbers:
    1. __is_valid_vin
        1. Выбрасывает исключение IncorrectVinNumber с сообщением 'Некорректный тип vin номер',
           если передано не целое число. (тип данных можно проверить функцией isinstance).
        2. Выбрасывает исключение IncorrectVinNumber с сообщением 'Неверный диапазон для vin номера',
           если переданное число находится не в диапазоне от 1000000 до 9999999 включительно.
        3. Возвращает True, если исключения не были выброшены.
    2. __is_valid_numbers
        1. Выбрасывает исключение IncorrectCarNumbers с сообщением 'Некорректный тип данных для номеров',
           если передана не строка. (тип данных можно проверить функцией isinstance).
        2. Выбрасывает исключение IncorrectCarNumbers с сообщением 'Неверная длина номера',
           переданная строка должна состоять ровно из 6 символов.
        3. Возвращает True, если исключения не были выброшены.

ВАЖНО!
Методы __is_valid_vin и __is_valid_numbers должны вызываться и при создании объекта
(в __init__ при объявлении атрибутов __vin и __numbers).
"""


class IncorrectVinNumber(Exception):
    """
    Класс исключения описывающий ошибку 'Некорректный VIN номер'.
    Атрибут объекта класса:
        * message - сообщение, которое выводится при выбрасывании исключения
    """


    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class IncorrectCarNumbers(Exception):
    """
    Класс исключения описывающий ошибку 'Некорректные номера'.
    Атрибут объекта класса:
        * message - сообщение, которое выводится при выбрасывании исключения
    """


    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class Car:
    """
    Класс описывающий автомобиль.
    Атрибуты объекта класса:
        1. приватные:
            * __vin - VIN номер автомобиля (целое число)
            * __numbers - номера автомобиля (строка)
        2. публичные:
            * model - название автомобиля (строка)
    """


    def __init__(self, model: str, vin: int, numbers: str):
        self.model: str = model
        self.__vin: int = vin
        self.__numbers = numbers

        # Проверяем корректность VIN и номеров при создании объекта
        self.__is_valid_vin(self.__vin)
        self.__is_valid_numbers(self.__numbers)


    def __is_valid_vin(self, vin_number: int) -> bool:
        """
        Метод проверяет VIN номер автомобиля на корректность.
        :param vin_number: VIN номер
        :return: True, если VIN номер корректный. В остальных случаях выбрасывает исключение.
        """
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True


    def __is_valid_numbers(self, numbers: str) -> bool:
        """
        Метод проверяет номера автомобиля на корректность.
        :param numbers: Номера
        :return: True, если номера корректные. В остальных случаях выбрасывает исключение.
        """
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True


# пример использования
try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
