# Практическая работа по уроку "Динамическая типизация"
"""
Создайте переменные разных типов данных:
  - Создайте переменную name и присвойте ей значение имени (строка).
  - Выведите значение переменной name на экран.
  - Создайте переменную age и присвойте ей значение возраста (целое число).
  - Выведите значение переменной age на экран.
  - Перезапишите в age текущее значение переменной age + новое.
Как неверно (просто перезапись на новое число):
a = 15
a = 17
  - Выведите измененное значение переменной age на экран.
  - Создайте переменную is_student и присвойте ей значение True (логическое значение).
  - Выведите значение переменной is_student на экран.
"""
name = 'Kamilla'
print('Name:', name)
age = 20
print('Age:', age)
age += 10
print('New Age:', age)
is_student = True
print('Is Student:', is_student)