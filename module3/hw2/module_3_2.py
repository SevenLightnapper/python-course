# Домашняя работа по уроку "Способы вызова функции"
"""
Задача "Рассылка писем":
Часто при разработке и работе с рассылками писем(e-mail) они отправляются от одного и того же пользователя
(администрации или службы поддержки). Тем не менее должна быть возможность сменить его в редких случаях.
Попробуем реализовать функцию с подробной логикой.

Создайте функцию send_email, которая принимает 2 обычных аргумента:
сообщение и получатель и 1 обязательно именованный аргумент со значением по умолчанию - отправитель.
Внутри функции реализовать следующую логику:
    1. Проверка на корректность e-mail отправителя и получателя.
    2. Проверка на отправку самому себе.
    3. Проверка на отправителя по умолчанию.

Пункты задачи:
    1. Создайте функцию send_email, которая принимает 2 обычных аргумента: message(сообщение), recipient(получатель)
       и 1 обязательно именованный аргумент со значением по умолчанию sender = "university.help@gmail.com".
    2. Если строки recipient и sender не содержат "@" или не оканчиваются на ".com"/".ru"/".net",
       то вывести на экран(в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
    3. Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"
    4. Если же отправитель по умолчанию - university.help@gmail.com,
       то вывести сообщение: "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
    5. В противном случае вывести сообщение:
       "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>."
    6. Здесь <sender> и <recipient> - значения хранящиеся в этих переменных.
    7. За один вызов функции выводится только одно и перечисленных уведомлений!
       Проверки перечислены по мере выполнения.
"""


def send_email(message, recipient, *, sender="university.help@gmail.com"):
    # Проверка на корректность e-mail
    valid_domains = [".com", ".ru", ".net"]
    if "@" not in recipient or not any(recipient.endswith(domain) for domain in valid_domains):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    if "@" not in sender or not any(sender.endswith(domain) for domain in valid_domains):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    # Проверка на отправку самому себе
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    # Проверка на отправителя по умолчанию
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


# вызовы функции
send_email("Hello!", "example@gmail.com")
send_email("Hello!", "example@gmail.com", sender="admin@website.com")
send_email("Hello!", "university.help@gmail.com")
send_email("Hello!", "invalid@email")
send_email("Hello!", "example@gmail.com", sender="invalid_sender.com")
send_email("Hello!", "example@gmail.com", sender="example@gmail.com")

# Ошибка
# TypeError: send_email() takes 2 positional arguments but 3 were given
# Может быть только 2 позиционных аргумента!
# Третий аргумент обязан быть именованным!
# send_email("Hello!", "example@gmail.com", "example@gmail.com")
