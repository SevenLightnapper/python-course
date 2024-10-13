#
"""
Задание:
Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента
и проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.

1. Создайте функцию introspection_info(obj), которая принимает объект obj.
2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
      - Тип объекта.
      - Атрибуты объекта.
      - Методы объекта.
      - Модуль, к которому объект принадлежит.
      - Другие интересные свойства объекта, учитывая его тип (по желанию).
"""


def introspection_info(obj):
    # Получаем тип объекта
    obj_type = type(obj).__name__

    # Получаем атрибуты объекта (без методов)
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    # Получаем методы объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    # Получаем модуль, в котором определен объект
    obj_module = obj.__class__.__module__

    # Дополнительные свойства, если необходимо
    extra_properties = {
        "is_class": isinstance(obj, type),
        "docstring": obj.__doc__,
        "repr": repr(obj)
    }

    # Возвращаем словарь с интроспекцией
    return {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module,
        'extra_properties': extra_properties
    }


# Пример использования
class ExampleClass:
    def __init__(self, name, value):
        self.name = name
        self.value = value


    def greet(self):
        return f"Hello, {self.name}!"


    def say_goodbye(self):
        return f"Bye, {self.name}!"


example = ExampleClass("John", 42)

# Интроспекция объекта
info = introspection_info(example)
print(info)
