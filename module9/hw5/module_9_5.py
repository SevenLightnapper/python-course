# Домашнее задание по теме "Итераторы"
"""
Задача "Range - это просто":

Создайте пользовательский класс исключения StepValueError, который наследуется от ValueError.
Наследования достаточно, класс оставьте пустым при помощи оператора pass.

Создайте класс Iterator, который обладает следующими свойствами:

Атрибуты объекта:
    1. start - целое число с которого начинается итерация.
    2. stop - целое число на котором заканчивается итерация.
    3. step - шаг с которой совершается итерация.
    4. pointer - указывает на текущее число в итерации (изначально start)
Методы:
    1. __init__(self, start, stop, step=1) - принимающий значения старта и конца итерации, а также шага.
       В этом методе в первую очередь проверяется step на равенство 0.
       Если равно, то выбрасывается исключение StepValueError('шаг не может быть равен 0')
    2. __iter__ - метод сбрасывающий значение pointer на start и возвращающий сам объект итератора.
    3. __next__ - метод увеличивающий атрибут pointer на step.
       В зависимости от знака атрибута step итерация завершиться либо когда pointer станет больше stop,
       либо меньше stop. Учтите это при описании метода.
"""


class StepValueError(ValueError):
    """
    Класс исключения. Наследник класса ValueError.
    Исключение выбрасывается, если шаг итерации равен 0.
    """
    pass


class Iterator:
    """
    Класс описывающий итератор.
    Атрибуты объекта класса:
        * start - целое число, с которого начинается итерация.
        * stop - целое число на котором заканчивается итерация.
        * step - шаг с которой совершается итерация.
        * pointer - указывает на текущее число в итерации (изначально start)
    """


    def __init__(self, start: int, stop: int, step: int = 1):
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')
        self.start: int = start
        self.stop: int = stop
        self.step: int = step
        self.pointer: int = start


    def __iter__(self):
        """
        Сбрасывает указатель на стартовое значение и возвращает объект итератора.
        :return: Объект итератора
        """
        self.pointer = self.start
        return self


    def __next__(self):
        """
        Возвращает текущее значение и сдвигает указатель на шаг вперед.
        Если итерация достигла конца, вызывает StopIteration.
        :raises StopIteration: Когда итерация завершена
        :return: Текущее значение указателя
        """
        # self.pointer > self.stop -- если знак '>' заменить на '>=', то элемент self.stop не будет учитываться
        # self.pointer < self.stop -- если знак '<' заменить на '<=', то элемент self.stop не будет учитываться
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration
        current_value = self.pointer
        self.pointer += self.step
        return current_value


# пример использования
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()
