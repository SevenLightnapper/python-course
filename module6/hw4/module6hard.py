# Дополнительное практическое задание по модулю: "Наследование классов."
"""
Задание "Они все так похожи":
2D? 3D? Даже 4D?.... Настолько глубоко мы заходить конечно же не будем, 4D подождёт,
но вот с двумерными и трёхмерными фигурами можем поэкспериментировать.
Вы когда-нибудь задумывались как устроены графические библиотеки для языков программирования?
Безусловно, там выполняются огромные расчёты при помощи вашей видеокарты, но...
Что лежит в основе удобного использования таких объектов?

По названию задачи можно понять, что все геометрические фигуры обладают схожими свойствами, такими как:
длины сторон, цвет и др.

Давайте попробуем реализовать простейшие классы для некоторых таких фигур и при этом применить наследование
(в будущем, изучая сторонние библиотеки, вы будете замечать схожие классы, уже написанные кем-то ранее):

Общее ТЗ:

Реализовать классы Figure(родительский), Circle, Triangle и Cube,
объекты которых будут обладать методами изменения размеров, цвета и т.д.
Многие атрибуты и методы должны быть инкапсулированны
и для них должны быть написаны интерфейсы взаимодействия (методы) - геттеры и сеттеры.

Подробное ТЗ:

Атрибуты класса Figure: sides_count = 0
Каждый объект класса Figure должен обладать следующими атрибутами:
    * Атрибуты(инкапсулированные): __sides(список сторон (целые числа)), __color(список цветов в формате RGB)
    * Атрибуты(публичные): filled(закрашенный, bool)
И методами:
    * Метод get_color, возвращает список RGB цветов.
    * Метод __is_valid_color - служебный, принимает параметры r, g, b,
      который проверяет корректность переданных значений перед установкой нового цвета.
      Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
    * Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения,
      предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
    * Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон,
      возвращает True если все стороны целые положительные числа и кол-во новых сторон совпадает с текущим,
      False - во всех остальных случаях.
    * Метод get_sides должен возвращать значение я атрибута __sides.
    * Метод __len__ должен возвращать периметр фигуры.
    * Метод set_sides(self, *new_sides) должен принимать новые стороны,
      если их количество не равно sides_count, то не изменять, в противном случае - менять.

Атрибуты класса Circle: sides_count = 1
Каждый объект класса Circle должен обладать следующими атрибутами и методами:
    * Все атрибуты и методы класса Figure
    * Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
    * Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).

Атрибуты класса Triangle: sides_count = 3
Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
    * Все атрибуты и методы класса Figure
    * Метод get_square возвращает площадь треугольника. (можно рассчитать по формуле Герона)

Атрибуты класса Cube: sides_count = 12
Каждый объект класса Cube должен обладать следующими атрибутами и методами:
    * Все атрибуты и методы класса Figure.
    * Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
    * Метод get_volume, возвращает объём куба.

ВАЖНО!
При создании объектов делайте проверку на количество переданных сторон,
если сторон не ровно sides_count, то создать массив с единичными сторонами и в том кол-ве, которое требует фигура.
Пример 1: Circle((200, 200, 100), 10, 15, 6), т.к. сторона у круга всего 1, то его стороны будут - [1]
Пример 2: Triangle((200, 200, 100), 10, 6), т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]
Пример 3: Cube((200, 200, 100), 9), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
Пример 4: Cube((200, 200, 100), 9, 12), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]
"""
import math
from typing import List, Tuple


class Figure:
    """
    Базовый родительский класс описывающий Фигуру.
    Атрибут класса:
        * sides_count - количество сторон фигуры (по умолчанию 0)
    Атрибуты объекта класса:
        1. Инкапсулированные:
            * __sides - список сторон (целые числа)
            * __color - список цветов в формате RGB
        2. Публичные:
            * filled - закрашенный (условие True | False)
    """
    sides_count: int = 0


    def __init__(self, color: Tuple[int, int, int], *sides: int):
        self.__sides: List[int] = [1] * self.sides_count
        self.__color: Tuple[int, int, int] = color
        self.filled: bool = False
        self.set_sides(*sides)


    def get_color(self) -> Tuple[int, int, int]:
        """
        Метод возвращает текущий цвет фигуры в формате RGB.
        :return: Цвет фигуры в формате RGB
        """
        return self.__color


    def __is_valid_color(self, r: int, g: int, b: int) -> bool:
        """
        Метод проверяет корректность переданных значений перед установкой нового цвета.
        Корректный цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
        :param r: Число красного канала
        :param g: Число зеленого канала
        :param b: Число синего канала
        :return: результат проверки - условие (True | False)
        """
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))


    def set_color(self, r: int, g: int, b: int) -> None:
        """
        Метод изменяет цвет фигуры на переданные значения, предварительно проверив их на корректность.
        :param r: Число красного канала
        :param g: Число зеленого канала
        :param b: Число синего канала
        """
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)


    def __is_valid_sides(self, *new_sides: int) -> bool:
        """
        Метод принимает неограниченное количество сторон,
        возвращает True если все стороны целые положительные числа,
        возвращает False во всех остальных случаях
        :param new_sides: новое количество сторон
        :return: результат проверки - условие (True | False)
        """
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)


    def get_sides(self) -> List[int]:
        """
        Метод возвращает список текущих сторон фигуры.
        :return: Стороны фигуры
        """
        return self.__sides


    def __len__(self) -> int:
        """
        Метод возвращает периметр фигуры.
        :return: Периметр фигуры
        """
        return sum(self.__sides)


    def set_sides(self, *new_sides: int) -> None:
        """
        Метод меняет стороны фигуры, если их количество равно sides_count.
        :param new_sides: Новые стороны фигуры
        :return: результат проверки - условие (True | False)
        """
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    """
    Класс описывающий фигуру Круг. Наследник класса Фигура.
    Атрибут класса:
        * sides_count - количество сторон круга
    Атрибуты объекта класса:
        1. Инкапсулированные:
            * __radius - радиус круга
    """
    sides_count: int = 1


    def __init__(self, color: Tuple[int, int, int], *sides: int):
        super().__init__(color, *sides)
        if len(self.get_sides()) == 0:
            self.set_sides(1)
        self.__radius: float = self.get_sides()[0] / (2 * math.pi)


    def get_square(self) -> float:
        """
        Метод возвращает площадь круга.
        :return: Площадь круга
        """
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    """
    Класс описывающий фигуру Треугольник. Наследник класса Фигура.
    Атрибут класса:
        * sides_count - количество сторон треугольника
    """
    sides_count = 3


    def __init__(self, color: Tuple[int, int, int], *sides: int):
        super().__init__(color, *sides)
        if len(self.get_sides()) != 3:
            self.set_sides(1, 1, 1)


    def get_square(self) -> float:
        """
        Метод возвращает площадь треугольника.
        :return: Площадь треугольника
        """
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    """
    Класс описывающий фигуру Куб. Наследник класса Фигура.
    Атрибут класса:
    * sides_count - количество сторон куба
    """
    sides_count: int = 12


    def __init__(self, color: Tuple[int, int, int], *sides: int):
        super().__init__(color, *sides)
        if len(sides) == 1:
            self.set_sides(*[sides[0]] * 12)
        elif len(sides) == 12:
            self.set_sides(*[sides[0]] * 12)


    def get_volume(self) -> float:
        """
        Метод возвращает объем куба.
        :return: Объем куба
        """
        edge_length = self.get_sides()[0]
        return edge_length ** 3

    def set_sides(self, *new_sides: int) -> None:
        """
        Метод переопределяет метод из класса родителя.
        Добавлены две дополнительные проверки:
            * смена сторон куба 1 числом
            * смена сторон куба 12 одинаковыми числами
        :param new_sides: Новые стороны куба
        """
        if len(new_sides) == 1:
            super().set_sides(*[new_sides[0]] * 12)
        elif all(side == new_sides[0] for side in new_sides):
            super().set_sides(*new_sides)


# пример использования №1
print("\n-------------Circle-------------")
circle = Circle((200, 200, 100), 15)
print("INFO:")
print("\tCircle Color:", circle.get_color())
print("\tCircle Sides:", circle.get_sides())
print("\tCircle Square:", circle.get_square())
print("COLOR CHANGE:")
circle.set_color(300, 70, 15)  # цвет не изменится
print("\tCircle color did not change", circle.get_color())
circle.set_color(10, 255, 0) # цвет изменится
print("\tCircle color changed", circle.get_color())
print("SIDES CHANGE:")
circle.set_sides(4, 4)  # не изменится
print("\tTriangle sides did not change", circle.get_sides())
circle.set_sides(100)  # изменится
print("\tTriangle sides changed", circle.get_sides())

print("\n-------------Triangle-------------")
triangle = Triangle((100, 150, 200), 6, 8, 10)
print("INFO:")
print("\tTriangle Color:", triangle.get_color())
print("\tTriangle Sides:", triangle.get_sides())
print("\tTriangle Square:", triangle.get_square())
print("COLOR CHANGE:")
triangle.set_color(-255, 70, 15)  # цвет не изменится
print("\tTriangle color did not change", triangle.get_color())
triangle.set_color(255, 255, 255) # цвет изменится
print("\tTriangle color changed", triangle.get_color())
print("SIDES CHANGE:")
triangle.set_sides(4, 4)  # не изменится
print("\tTriangle sides did not change", triangle.get_sides())
triangle.set_sides(3, 3, 3)  # изменится
print("\tTriangle sides changed", triangle.get_sides())

print("\n-------------Cube-------------")
cube = Cube((255, 0, 0), 6)
print("INFO:")
print("\tCube Color:", cube.get_color())
print("\tCube Sides:", cube.get_sides())
print("\tCube Volume:", cube.get_volume())
print("COLOR CHANGE:")
cube.set_color(0, -70, 15)  # цвет не изменится
print("\tCube color did not change", cube.get_color())
cube.set_color(0, 0, 0) # цвет изменится
print("\tCube color changed", cube.get_color())
print("SIDES CHANGE:")
cube.set_sides(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)  # не изменится
print("\tCube sides did not change", cube.get_sides())
cube.set_sides(4, 4, 4, 4)  # не изменится
print("\tCube sides did not change", cube.get_sides())
cube.set_sides(3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3)  # изменится
print("\tCube sides changed", cube.get_sides())
cube.set_sides(27)  # изменится
print("\tCube sides changed", cube.get_sides())
