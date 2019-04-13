# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


# Функция упрощения дроби
def simpling(numerator: int, denominator: int) -> list:
    common_factor = 0
    for iter in range(abs(numerator), 0, -1):
        if abs(numerator) % iter == 0 and denominator % iter == 0:
            common_factor = iter
            break
    if common_factor != 0:
        if numerator > 0:
            return [numerator // common_factor, denominator // common_factor]
        else:
            return [-abs(numerator // common_factor), denominator // common_factor]
    else:
        return [numerator, denominator]


# функция выделения целой части
def whole_fraction(numerator: int, denominator: int) -> list:
    if numerator % denominator == 0:
        return [numerator // denominator]
    elif numerator > denominator:
        return [numerator // denominator, simpling(numerator % denominator, denominator)]
    elif numerator < -denominator:
        return [numerator // denominator + 1, simpling(denominator - numerator % denominator, denominator)]
    else:
        return simpling(numerator, denominator)


# обратное действие(преобразование в неправильную дробь
def improper_fraction(entire: int, numerator: int, denominator: int) -> list:
    if entire >= 0:
        return simpling(entire * denominator + numerator, denominator)
    else:
        return simpling(entire * denominator - numerator, denominator)


# функция нахождения наименьшего общего кратного (общего знаменателя)
def least_common_multiple(denominator_1: int, denominator_2: int) -> int:
    common_multiple = 0
    for iter in range(max(denominator_1, denominator_2), (denominator_1 * denominator_2) + 1,
                      max(denominator_1, denominator_2)):
        if iter % min(denominator_1, denominator_2) == 0:
            common_multiple = iter
            break
    return common_multiple


# функция сложения двух дробей
def fraction_add(numerator_1: int, denominator_1: int, numerator_2: int, denominator_2: int) -> list:
    denominator = least_common_multiple(denominator_1, denominator_2)
    numerator = numerator_1 * (denominator // denominator_1) + numerator_2 * (denominator // denominator_2)
    return whole_fraction(numerator, denominator)


# функция вычитания двух дробей
def fraction_sub(numerator_1: int, denominator_1: int, numerator_2: int, denominator_2: int) -> list:
    denominator = least_common_multiple(denominator_1, denominator_2)
    numerator = numerator_1 * (denominator // denominator_1) - numerator_2 * (denominator // denominator_2)
    return whole_fraction(numerator, denominator)


# является ли выражение дробью, а не знаком сложения/вычитания
def is_fraction(expression : str) -> bool:
    if '+' in expression or '-' in expression:
        return False
    else:
        return True


expression = input("Введите выражение, которое необходимо вычислить: ")
expression = expression.split(' ')
if is_fraction(expression[1]):
    fraction_1_whole = int(expression[0])
    fraction_1 = expression[1].split('/')
    fraction_1_numer, fraction_1_denom = int(fraction_1[0]), int(fraction_1[1])
else:
    if '/' not in expression[0]:
        fraction_1_whole = int(expression[0])
        fraction_1_numer, fraction_1_denom = 0, 1
    else:
        fraction_1_whole = 0
        fraction_1 = expression[0].split('/')
        fraction_1_numer, fraction_1_denom = int(fraction_1[0]), int(fraction_1[1])
if is_fraction(expression[-2]):

        fraction_2_whole = int(expression[-2])
        fraction_2 = expression[-1].split('/')
        fraction_2_numer, fraction_2_denom = int(fraction_2[0]), int(fraction_2[1])
else:
    if '/' not in expression[-1]:
        fraction_2_whole = int(expression[-1])
        fraction_2_numer, fraction_2_denom = 0, 1
    else:
        if '-' in expression[-2] and len(expression) != 1:
            fraction_2_whole = int(expression[-2])
        else:
            fraction_2_whole = 0
        fraction_2 = expression[-1].split('/')
        fraction_2_numer, fraction_2_denom = int(fraction_2[0]), int(fraction_2[1])
fraction_1 = improper_fraction(fraction_1_whole, fraction_1_numer, fraction_1_denom)
fraction_2 = improper_fraction(fraction_2_whole, fraction_2_numer, fraction_2_denom)
if '+' in expression:
    result = fraction_add(fraction_1[0], fraction_1[1], fraction_2[0], fraction_2[1])
else:
    result = fraction_sub(fraction_1[0], fraction_1[1], fraction_2[0], fraction_2[1])
print("Результат: ", result)
