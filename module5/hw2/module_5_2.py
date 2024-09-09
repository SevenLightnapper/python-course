# Домашняя работа по уроку "Специальные методы классов"
"""
Задача "Магические здания":
Для решения этой задачи будем пользоваться решением к предыдущей задаче "Атрибуты и методы объекта".

Необходимо дополнить класс House следующими специальными методами:
    1. __len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
    2. __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".
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


    def __len__(self):
        return self.number_of_floors


    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


# примеры создания объекта класса House
elbrus_house = House("ЖК Эльбрус", 30)
tower_house = House("ЖК Tower", 10)
private_house = House("Частный дом", 2)

# вызовы метода __str__
print(elbrus_house)
print(tower_house)
print(private_house)

# вызовы метода __len__
print(len(elbrus_house))
print(len(tower_house))
print(len(private_house))
