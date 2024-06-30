# Практическое задание по теме: "Словари и множества"
"""
1. Работа со словарями:
  - Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
Например: Имя(str)-Год рождения(int).
  - Выведите на экран словарь my_dict.
  - Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict без ошибки.
  - Добавьте ещё две произвольные пары того же формата в словарь my_dict.
  - Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран.
  - Выведите на экран словарь my_dict.

2. Работа с множествами:
  - Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
  - Выведите на экран множество my_set (должны отобразиться только уникальные значения).
  - Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
  - Удалите один любой элемент из множества my_set.
  - Выведите на экран измененное множество my_set.
"""
# словарь
my_dict = {
    "Alice": 1990,
    "Bob": 1985,
    "Charlie": 2000
}
print("My dictionary:", my_dict)

# Существующий ключ
print("My dictionary - Alice:", my_dict["Alice"])
# Отсутствующий ключ (используется метод get, чтобы избежать ошибки)
print("My dictionary - David:", my_dict.get("David", "Not Found"))

my_dict["David"] = 1995
my_dict["Eve"] = 1988
print("Added two pairs to dictionary:", my_dict)

removed_value = my_dict.pop("Bob", "Not Found")
print("Value of removed pair:", removed_value)
print("My dictionary after removal:", my_dict)


# множество
my_set = {1, 2, 2, 3, "apple", "banana", "apple"}
print("My set:", my_set)

my_set.add("cherry")
my_set.add(4)
print("Added two elements to set:", my_set)

my_set.remove('apple')
print("Set after removal:", my_set)
