# Домашняя работа по уроку "Различие атрибутов класса и экземпляра."
"""
Задача "История строительства":
Для решения этой задачи будем пользоваться решением к предыдущей задаче "Перегрузка операторов".

В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.

Правильней вписывать здание в историю сразу при создании объекта,
тем более можно удобно обращаться к атрибутам класса используя ссылку на сам класс - cls.
Дополните метод __new__ так, чтобы:
    1. Название объекта добавлялось в список cls.houses_history.
    2. Название строения можно взять из args по индексу.

Также переопределите метод __del__(self) в котором будет выводиться строка:
"<название> снесён, но он останется в истории"

Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__,
а также значение атрибута houses_history.
"""
from functools import total_ordering


@total_ordering  # для упрощения переопределения методов сравнения
class House:
    houses_history = []  # атрибут класса для хранения истории


    def __new__(cls, *args, **kwargs):
        # создание нового экземпляра объекта
        instance = super().__new__(cls)
        # добавление названия здания в историю
        if args:
            cls.houses_history.append(args[0])
        return instance


    def __del__(self):
        # вывод сообщения о сносе здания
        print(f"{self.name} снесен, но он останется в истории")


    def __init__(self, name, number_of_floors):
        # инициализация атрибутов объекта
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        # проверяем, что этаж в допустимом диапазоне
        if new_floor < 1 or new_floor > self.number_of_floors:
            print(self.name)
            print(f"Такого этажа [{new_floor}] не существует")
            print("-----------------")
        else:
            # выводим номера этажей от 1 до new_floor включительно
            print(self.name)
            for floor in range(1, new_floor + 1):
                print(floor)
            print("-----------------")


    # возвращает кол-во этажей
    def __len__(self):
        return self.number_of_floors


    # возвращает описание объекта
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


    # ==
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return NotImplemented


    # <
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return NotImplemented


    # увеличивает кол-во этажей на переданное значение,
    # если это значение типа int
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        return NotImplemented


    # увеличивает кол-во этажей на переданное значение
    # если это значение типа int
    def __radd__(self, value):
        return self.__add__(value)


    # работает аналогично __add__,
    # но применяется при использовании оператора +=
    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        return NotImplemented


# примеры создания объектов класса House
elbrus_house = House("ЖК Эльбрус", 30)
tower_house = House("ЖК Tower", 10)
private_house = House("Частный дом", 2)

house1 = House("House1", 5)
house2 = House("House2", 10)

print("История зданий:")
print(House.houses_history)

del house1
del house2

print("История зданий после удаления:")
print(House.houses_history)
