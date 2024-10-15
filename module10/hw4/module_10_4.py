# Домашнее задание по теме "Очереди для обмена данными между потоками."
"""
Задача "Потоки гостей в кафе":
Необходимо имитировать ситуацию с посещением гостями кафе.
Создайте 3 класса: Table, Guest и Cafe.

Класс Table:
    1. Объекты этого класса должны создаваться следующим способом - Table(1)
    2. Обладать атрибутами number - номер стола и guest - гость, который сидит за этим столом (по умолчанию None)

Класс Guest:
    1. Должен наследоваться от класса Thread (быть потоком).
    2. Объекты этого класса должны создаваться следующим способом - Guest('Vasya').
    3. Обладать атрибутом name - имя гостя.
    4. Обладать методом run, где происходит ожидание случайным образом от 3 до 10 секунд.

Класс Cafe:
    1. Объекты этого класса должны создаваться следующим способом - Cafe(Table(1), Table(2),....)
    2. Обладать атрибутами queue - очередь (объект класса Queue) и tables - столы в этом кафе (любая коллекция).
    3. Обладать методами guest_arrival (прибытие гостей) и discuss_guests (обслужить гостей).

Метод guest_arrival(self, *guests):
    1. Должен принимать неограниченное кол-во гостей (объектов класса Guest).
    2. Далее, если есть свободный стол, то садить гостя за стол (назначать столу guest),
       запускать поток гостя и выводить на экран строку "<имя гостя> сел(-а) за стол номер <номер стола>".
    3. Если же свободных столов для посадки не осталось,
       то помещать гостя в очередь queue и выводить сообщение "<имя гостя> в очереди".

Метод discuss_guests(self): Этот метод имитирует процесс обслуживания гостей.
    1. Обслуживание должно происходить пока очередь не пустая (метод empty) или хотя бы один стол занят.
    2. Если за столом есть гость(поток) и гость(поток) закончил приём пищи(поток завершил работу - метод is_alive),
       то вывести строки "<имя гостя за текущим столом> покушал(-а) и ушёл(ушла)" и "Стол номер <номер стола> свободен".
       Так же текущий стол освобождается (table.guest = None).
    3. Если очередь ещё не пуста (метод empty) и стол один из столов освободился (None),
       то текущему столу присваивается гость взятый из очереди (queue.get()).
       Далее выводится строка "<имя гостя из очереди> вышел(-ла) из очереди и сел(-а) за стол номер <номер стола>"
    4. Далее запустить поток этого гостя (start)

Таким образом мы получаем 3 класса на основе которых имитируется работа кафе:
    1. Table - стол, хранит информацию о находящемся за ним гостем (Guest).
    2. Guest - гость, поток, при запуске которого происходит задержка от 3 до 10 секунд.
    3. Cafe - кафе, в котором есть определённое кол-во столов и происходит имитация прибытия гостей (guest_arrival)
       и их обслуживания (discuss_guests).
"""
from queue import Queue
from random import randint
from threading import Thread
from time import sleep


class Table:
    def __init__(self, number: int):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name: str):
        super().__init__()
        self.name = name


    def run(self):
        time_to_eat = randint(3, 10)
        sleep(time_to_eat)


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)


    def guest_arrival(self, *guests: list[Guest]):
        for guest in guests:
            available_table = next((table for table in self.tables if table.guest is None), None)
            if available_table:
                available_table.guest = guest
                guest.start()
                print(f"{guest.name} сел(-а) за стол номер {available_table.number}")
            else:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")


    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушел(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None

                    if not self.queue.empty():
                        next_guest = self.queue.get()
                        table.guest = next_guest
                        next_guest.start()
                        print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
            sleep(1)


# пример использования
# создание столов
tables = [Table(number) for number in range(1, 6)]
# имена гостей
guest_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Victoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# создание гостей
guests = [Guest(name) for name in guest_names]
# заполнение кафе столами
cafe = Cafe(*tables)
# прием гостей
cafe.guest_arrival(*guests)
# обслуживание гостей
cafe.discuss_guests()
