# Практическое задание по уроку "Базовые структуры данных"
"""
№1 - Задача «Длина слова».
Описание: Запишите в переменную a произвольную строку.
Затем вычислите длину строки и выведите результат на экран(в консоль).
"""
print('task 1')
a = 'task number one'
print('длина строки =', len(a))

"""
№2 - Задача «Суммы и разности».
Описание: запишите два целых числа в переменные first и second, 
вычислите их сумму и разность, запишите их в переменные summa и diff. 
Затем выведите значения переменных summa и diff на экран(в консоль).
"""
print('\ntask 2')
first = 1
second = 2
summa = first + second
diff = first - second
print('сумма =', summa, '| разность =', diff)

"""
№3 - Задача «Среднее арифметическое».
Описание: Запишите три числа в переменные first, second и third соответственно 
и вычислите их среднее арифметическое, записав в переменную mean. 
Затем выведите значения переменной mean на экран(в консоль).
"""
print('\ntask 3')
first = 15
second = 2.5
third = -1
mean = (first + second + third) / 3
print('среднее арифметическое =', mean)

"""
№4 - Задача «Простые строчки».
Описание: Создайте две переменных first_string и second_string 
и запишите в них строки "Вторник" и "Понедельник". 
Выведите на экран(в консоль) строки так, 
чтобы "Понедельник" шёл перед "Вторником" 
и между ними находилась запятая с пробелом (", ")
Понедельник, Вторник
"""
print('\ntask 4')
first_string = 'Вторник'
second_string = 'Понедельник'
print(second_string + ', ' + first_string)

"""
Задача «Сложная формула».
Описание: Запишите три числа в переменные a, b и c соответственно 
и создайте переменную f, в которую запишите результат выражения: (a * b) + (a * c). 
Возведите полученное число в третью степень и результат разделите(обычное деление) на два. 
Выведите его на экран(в консоль).
"""
print('\ntask 5')
a = 1
b = 2
c = 3
f = (a * b) + (a * c)
print(f ** 3 / 2)