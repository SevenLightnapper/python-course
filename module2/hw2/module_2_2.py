# Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else."
"""
Задача "Все ли равны?":
На вход программе подаются 3 целых числа и
записываются в переменные first, second и third соответственно.
Ваша задача написать условную конструкцию (из if, elif, else),
которая выводит кол-во одинаковых чисел среди 3-х введённых.

Пункты задачи:

    1. Если все числа равны между собой, то вывести 3
    2. Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
    3. Если равных чисел среди 3-х вообще нет, то вывести 0
"""

first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
third = int(input("Enter the third number: "))

print("You've entered", end=" ")

if first == second == third:
    print(3, "equal numbers")
elif first == second or first == third or second == third:
    print(2, "equal numbers")
else:
    print(0, "equal numbers")
