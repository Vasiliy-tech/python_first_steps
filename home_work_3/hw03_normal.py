# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


from typing import Union


def fibonacci(n: int, m: int) -> list:
    fibonacci_list = [1, 1]
    while len(fibonacci_list) < m:
        fibonacci_list.append(fibonacci_list[len(fibonacci_list)-1] + fibonacci_list[len(fibonacci_list)-2])
    return fibonacci_list[n-1:]


print(fibonacci(4, 8))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list: list) -> list:
    for count in range(len(origin_list)-1):
        for count_1 in range(len(origin_list)-1):
            if origin_list[count_1] > origin_list[count_1+1]:
                origin_list[count_1],  origin_list[count_1+1] = origin_list[count_1+1],  origin_list[count_1]
    return origin_list


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def my_filter(func: bool, iterable: Union[str, list, tuple, dict, set]) -> list:
    if func is not None:
        return [argument for argument in iterable if func(argument)]
    else:
        return [argument for argument in iterable if argument]


list_1 = [28, -12, 29, 43543525, 1, 0]
print(my_filter(lambda x: x > 25, list_1))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Point(abs(self.x - other.x), abs(self.y - other.y))


# проверка на лежание точек на одной прямой
def line_check(point_1: Point, point_2: Point, point_3: Point) -> bool:
    if (point_3 - point_1).x / (point_2 - point_1).x == (point_3 - point_1).y / (point_2 - point_1).y:
        return True
    else:
        return False


def parallelogramm(point_1: Point, point_2: Point, point_3: Point, point_4: Point) -> bool:
    if (point_1 - point_2).x == (point_3 - point_4).x and (point_1 - point_2).y == (point_3 - point_4).y \
     or (point_1 - point_4).x == (point_2 - point_3).x and (point_1 - point_4).y == (point_2 - point_3).y:
        return True
    else:
        return False


A1 = Point(0, 0)
A2 = Point(1, 4)
A3 = Point(5, 1)
A4 = Point(6, 6)
if parallelogramm(A1, A4, A2, A3) and not line_check(A1, A2, A3):
    print('точки образуют параллелограмм')
else:
    print('точки не образуют параллелограмм')
