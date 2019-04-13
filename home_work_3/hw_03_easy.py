# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number: float, ndigits: int) -> float:
    size_of_float = (len(str(number)) - str(number).find(".") - 1)
    str_of_number = str(number)
    if size_of_float > ndigits:
        last_of_ndigits = int(
            str_of_number[-(size_of_float - ndigits)])  # цифра в числе, идущая за разрядом ndigits
        if last_of_ndigits <= 5:
            return str_of_number[:-(size_of_float - ndigits)]
        else:
            return str_of_number[:-(size_of_float - ndigits + 1)] + str(
                int(str_of_number[-(size_of_float - ndigits + 1)]) + 1)
    elif size_of_float == ndigits:
        return number
    else:
        return str(number) + '0' * (ndigits - size_of_float)


print(my_round(24.42, 4))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number: int) -> bool:
    str_of_ticket_number = str(ticket_number)
    if int(str_of_ticket_number[0]) + int(str_of_ticket_number[1]) + int(str_of_ticket_number[2]) == int(
            str_of_ticket_number[-1]) + int(str_of_ticket_number[-2]) + int(str_of_ticket_number[-3]):
        access = True
    else:
        access = False
    return access


res = lucky_ticket(624642)
print(res)
