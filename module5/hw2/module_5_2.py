# Домашняя работа по уроку "Атрибуты и методы объекта."
"""
Задача "Developer - не только разработчик":
Реализуйте класс House, объекты которого будут создаваться следующим образом:
    House('ЖК Эльбрус', 30)
Объект этого класса должен обладать следующими атрибутами:
    self.name - имя, self.number_of_floors - кол-во этажей
Также должен обладать методом go_to(new_floor),
где new_floor - номер этажа(int), на который нужно приехать.
Метод go_to выводит на экран(в консоль) значения от 1 до new_floor(включительно).
Если же new_floor больше чем self.number_of_floors или меньше 1,
то вывести строку "Такого этажа не существует".
Пункты задачи:
    1. Создайте класс House.
    2. Внутри класса House определите метод __init__, в который передадите название и кол-во этажей.
    3. Внутри метода __init__ создайте атрибуты объекта self.name и self.number_of_floors,
    присвойте им переданные значения.
    4. Создайте метод go_to с параметром new_floor и напишите логику внутри него на основе описания задачи.
    5. Создайте объект класса House с произвольным названием и количеством этажей.
    6. Вызовите метод go_to у этого объекта с произвольным числом.
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
