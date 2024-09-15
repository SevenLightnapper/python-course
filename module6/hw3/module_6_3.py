# Домашнее задание по теме "Множественное наследование"
"""
Задача "Мифическое наследование":
Необходимо написать 3 класса:
Horse - класс описывающий лошадь. Объект этого класса обладает следующими атрибутами:
    1. x_distance = 0 - пройденный путь.
    2. sound = 'Frrr' - звук, который издаёт лошадь.
И методами:
    1. run(self, dx), где dx - изменение дистанции, увеличивает x_distance на dx.

Eagle - класс описывающий орла. Объект этого класса обладает следующими атрибутами:
    1. y_distance = 0 - высота полёта
    2. sound = 'I train, eat, sleep, and repeat' - звук, который издаёт орёл (отсылка)
И методами:
    1. fly(self, dy) где dy - изменение дистанции, увеличивает y_distance на dy.

Pegasus - класс описывающий пегаса. Наследуется от Horse и Eagle в том же порядке.
Объект такого класса должен обладать атрибутами классов родителей в порядке наследования.
Также обладает методами:
    1. move(self, dx, dy) - где dx и dy изменения дистанции.
       В этом методе должны запускаться наследованные методы run и fly соответственно.
    2. get_pos(self) возвращает текущее положение пегаса в виде кортежа - (x_distance, y_distance) в том же порядке.
    3. voice - который печатает значение унаследованного атрибута sound.
Пункты задачи:
    1. Создайте классы родители: Horse и Eagle с методами из описания.
    2. Создайте класс наследник Pegasus с методами из описания.
    3. Создайте объект класса Pegasus и вызовите каждый из ранее перечисленных методов, проверив их работу.
"""


class Horse:
    """
    Класс описывающий лошадь.
    Объект этого класса обладает следующими атрибутами:
        * x_distance - пройденный путь
        * sound - звук, который издает лошадь
    """
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'


    def run(self, dx):
        """
        Метод увеличивает пройденный путь лошади на dx
        :param dx:
        """
        self.x_distance += dx


class Eagle:
    """
    Класс описывающий орла.
    Объект этого класса обладает следующими атрибутами:
        * y_distance - высота полета
        * sound - звук, который издает орел
    """
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'


    def fly(self, dy):
        """
        Метод увеличивает высоту полета орла на dy
        :param dy:
        """
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    """
    Класс описывающий пегаса. Наследник классов Horse и Eagle.
    """
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)


    def move(self, dx, dy):
        """
        Метод изменения положения пегаса.
        :param dx: Изменение пройденного пути
        :param dy: Изменение высоты полета
        """
        self.run(dx)
        self.fly(dy)


    def get_pos(self):
        """
        Метод возвращает текущее положение пегаса.
        :return: Текущее положение пегаса
        """
        return self.x_distance, self.y_distance


    def voice(self):
        """
        Метод печатает значение унаследованного атрибута 'sound'
        """
        print(self.sound)


# пример использования
pegasus = Pegasus()

print("Initial position:", pegasus.get_pos())
pegasus.move(10, 20)
print("Position after moving:", pegasus.get_pos())
pegasus.move(-5, -10)
print("Position after moving again:", pegasus.get_pos())
pegasus.voice()