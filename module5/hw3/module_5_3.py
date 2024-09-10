# Домашняя работа по уроку "Перегрузка операторов."
"""
Для решения этой задачи будем пользоваться решением к предыдущей задаче "Специальные методы класса".

Необходимо дополнить класс House следующими специальными методами:
    1. __eq__(self, other) - должен возвращать True,
    если количество этажей одинаковое у self и у other.
    2. Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=)
    должны присутствовать в классе и возвращать результаты сравнения по соответствующим операторам.
    Как и в методе __eq__ в сравнении участвует кол-во этажей.
    3. __add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
    4. __radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).

Остальные методы арифметических операторов, где self - x, other - y:

Следует заметить, что other может быть не только числом, но и вообще любым объектом другого класса.
Для более точной логики работы методов __eq__, __add__ и других методов сравнения и арифметики
перед выполняемыми действиями лучше убедиться в принадлежности к типу при помощи функции isinstance:
    isinstance(other, int) - other указывает на объект типа int.
    isinstance(other, House) - other указывает на объект типа House.
"""


class House:
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


    # <=
    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return NotImplemented


    # >
    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return NotImplemented


    # >=
    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return NotImplemented


    # !=
    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
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


# примеры создания объекта класса House
elbrus_house = House("ЖК Эльбрус", 30)
tower_house = House("ЖК Tower", 10)
private_house = House("Частный дом", 2)

house1 = House("House1", 5)
house2 = House("House2", 10)

# примеры сравнения
print(house1 == house2)         # False
print(house1 != elbrus_house)   # True
print(house1 > house2)          # False
print(house1 >= house2)         # False
print(private_house < house1)   # True
print(private_house <= house1)  # True

# примеры увеличения
print(house1)
house1 += 3        # __iadd__
print(house1)
print(house1 + 2)  # __add__
print(2 + house1)  # __radd__
