# Практическое задание по работе в Pycharm - "Переменные".
"""
Задача:
Напишите 4 переменных которые будут обозначать следующие данные:

  1.  Количество выполненных ДЗ (запишите значение 12)
  2.  Количество затраченных часов (запишите значение 1.5)
  3.  Название курса (запишите значение 'Python')
  4.  Время на одно задание (вычислить используя 1 и 2 переменные)

Выведите на экран(в консоль), используя переменные, следующую строку:
Курс: Python, всего задач: 12, затрачено часов: 1.5, среднее время выполнения 0.125 часа.
"""
homeworks_done_count = 12
hours_spent_count = 1.5
course_name = 'Python'
time_per_homework = hours_spent_count / homeworks_done_count
# используется оператор '+' для корректного отображения запятых
print("Курс:", course_name +
      ", всего задач:", str(homeworks_done_count) +
      ", затрачено часов:", str(hours_spent_count) +
      ", среднее время выполнения", time_per_homework, "часа.")
