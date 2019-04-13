# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number: float, ndigits: int) -> float:
    number_1 = number * 10 ** ndigits
    if number_1 - int(number_1) >= 0.5:
        return int(number_1 + 1) / 10 ** ndigits
    else:
        return int(number_1) / 10 ** ndigits


test = my_round(2.1234567, 1)
print(test)


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number: int) -> bool:
    ticket_tuple = tuple(int(digit) for digit in ticket_number)
    if len(ticket_tuple) != 6:
        return False
    # хотелось бы комментариев, как сделать красивее следующую строку, а то больно громоздко выходит
    elif sum([ticket_tuple[0], ticket_tuple[1], ticket_tuple[2]]) == sum([ticket_tuple[3], ticket_tuple[4], ticket_tuple[5]]):
        return True
    else:
        return False


ticket = input('Введите номер билета: ')
if lucky_ticket(ticket):
    print("Счастливый билет!")
else:
    print("Билет не является счастливым(")

