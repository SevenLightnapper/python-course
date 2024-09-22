# Домашнее задание по теме "Позиционирование в файле"
"""
Задача "Записать и запомнить":
Создайте функцию custom_write(file_name, strings),
которая принимает аргументы file_name - название файла для записи, strings - список строк для записи.

Функция должна:
    1. Записывать в файл file_name все строки из списка strings, каждая на новой строке.
    2. Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>),
       а значением - записываемая строка.
       Для получения номера байта начала строки используйте метод tell() перед записью.

Пример полученного словаря:

{(1, 0): 'Text for tell.', (2, 16): 'Используйте кодировку utf-8.'}

Где:
    * 1, 2 - номера записанных строк.
    * 0, 16 - номера байт, на которых началась запись строк.
    * 'Text for tell.', 'Используйте кодировку utf-8.' - сами строки.
"""
def custom_write(file_name: str, strings: list[str]) -> dict[tuple[int, int], str]:
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        for i, string in enumerate(strings, start=1):
            byte_position = file.tell()  # Запоминаем начальную позицию перед записью
            file.write(string + '\n')  # Записываем строку в файл
            strings_positions[(i, byte_position)] = string  # Добавляем в словарь информацию о строке

    return strings_positions


# Пример использования
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
