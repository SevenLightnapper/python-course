# Домашнее задание по теме "Файлы в операционной системе"
"""
Задание:

Создайте новый проект или продолжите работу в текущем проекте.
    2. Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
    3. Примените os.path.join для формирования полного пути к файлам.
    4. Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
    5. Используйте os.path.getsize для получения размера файла.
    6. Используйте os.path.dirname для получения родительской директории файла.
"""
import os
import time


# Переменная directory указывает на каталог для обхода
directory = "."

# Используем os.walk для обхода всех файлов в директории
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)  # Полный путь к файлу
        filetime = os.path.getmtime(filepath)  # Время последнего изменения файла
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))  # Форматирование времени
        filesize = os.path.getsize(filepath)  # Размер файла в байтах
        parent_dir = os.path.dirname(filepath)  # Родительская директория файла

        # Вывод информации о файле
        print(f'Обнаружен файл: {file}, '
              f'Путь: {filepath}, '
              f'Размер: {filesize} байт, '
              f'Время изменения: {formatted_time}, '
              f'Родительская директория: {parent_dir}')
