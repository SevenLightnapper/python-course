# Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"
"""
Задача "Всё не так уж просто":
Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Используя этот список составьте второй список primes содержащий только простые числа.
А так же третий список not_primes, содержащий все не простые числа.
Выведите списки primes и not_primes на экран(в консоль).
Пункты задачи:

    1. Создайте пустые списки primes и not_primes.
    2. При помощи цикла for переберите список numbers.
    3. Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1ого цикла.
    4. Отметить простоту числа можно переменной is_prime, записав в неё значение True перед проверкой.
    5. В процессе проверки на простоту записывайте числа из списка numbers в списки primes и not_primes
    в зависимости от значения переменной is_prime после проверки (True - в prime, False - в not_prime).
    6. Выведите списки primes и not_primes на экран(в консоль).
"""
# Исходный список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Создаем пустые списки для простых и непростых чисел
primes = []
not_primes = []

# Перебираем числа в списке numbers
for num in numbers:
    # Пропускаем число 1, так как оно не является ни простым, ни составным
    if num == 1:
        continue

    # Предполагаем, что число простое
    is_prime = True

    # Числа меньше 2 не являются простыми
    if num < 2:
        is_prime = False
    else:
        # Проверяем делители от 2 до sqrt(num)
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

    # Записываем числа в соответствующие списки
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)

# Выводим списки на экран
print("Primes:", primes)
print("Not Primes:", not_primes)
