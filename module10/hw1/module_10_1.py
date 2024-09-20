# Домашнее задание по теме "Создание потоков".
"""
Задача "Потоковая запись в файлы":

Необходимо создать функцию wite_words(word_count, file_name), где word_count - количество записываемых слов,
file_name - название файла, куда будут записываться слова.
Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл
с прерыванием после записи каждого на 0.1 секунду.
Сделать паузу можно при помощи функции sleep из модуля time,
предварительно импортировав её: from time import sleep.
В конце работы функции вывести строку "Завершилась запись в файл <название файла>".

После создания файла вызовите 4 раза функцию wite_words, передав в неё следующие значения:
    1. 10, example1.txt
    2. 30, example2.txt
    3. 200, example3.txt
    4. 100, example4.txt

После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:
    1. 10, example5.txt
    2. 30, example6.txt
    3. 200, example7.txt
    4. 100, example8.txt

Запустите эти потоки методом start не забыв, сделать остановку основного потока при помощи join.
Также измерьте время затраченное на выполнение функций и потоков.
Как это сделать рассказано в лекции к домашнему заданию.
"""
import threading
from time import sleep, time


def write_words(word_count: int, file_name: str):
    """
    Функция записывает указанное количество слов в файл с паузой 0.1 секунды между записями.
    :param word_count: Количество слов для записи
    :param file_name: Название файла для записи
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)  # пауза 0.1 секунды между записями
    print(f"Завершилась запись в файл {file_name}")


# Последовательные вызовы функции
start_time = time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = time()
print(f"Время выполнения последовательных вызовов: {end_time - start_time:.2f} секунд")


# Параллельные вызовы функции с потоками
start_time = time()

# Создание потоков
threads = [
    threading.Thread(target=write_words, args=(10, 'example5.txt')),
    threading.Thread(target=write_words, args=(30, 'example6.txt')),
    threading.Thread(target=write_words, args=(200, 'example7.txt')),
    threading.Thread(target=write_words, args=(100, 'example8.txt'))
]

# Запуск потоков
for thread in threads:
    thread.start()

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()

end_time = time()
print(f"Время выполнения многопоточных вызовов: {end_time - start_time:.2f} секунд")
