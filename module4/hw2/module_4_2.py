# Домашнее задание по уроку "Пространство имен"
"""
Ваша задача:
    1. Создайте новую функцию def test_function
    2. Создайте другую функцию внутри функции inner_function,
    функция должна печатать значение "Я в области видимости функции test_function"
    3. Вызовите функцию inner_function внутри функции test_function
    4. Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы
    5. Полученный код напишите в ответ к домашнему заданию
"""


def test_function():
    print("Я test_function")

    def inner_function():
        print("\tЯ в области видимости функции test_function")

    print("Вызов inner_function:")
    inner_function()


# calling inner_function() causes an error
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
# inner_function()
test_function()
