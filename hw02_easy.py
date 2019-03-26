# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
print("Решение задачи 1")
fruit_list = ["яблоко", "дыня", "маракуйя", "арбуз", "член_Дамира"]
max_len = max(len(fruit) for fruit in fruit_list)
for index in range(len(fruit_list)):
    print('{}.'.format(index + 1), '{:>{}}'.format(fruit_list[index], max_len))

# Подсказка: воспользоваться методом .format()


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
print("Решение задачи 2")
list_1 = [1, "Valet", 2, 7, "Valet", 1, 1, "Valet"]
list_2 = ["Башня", 6, 1, "Valet", 3]
inc = 0
while inc < len(list_1):
    for element_2 in list_2:
        for element_1 in list_1:
            if element_1 == element_2:
                list_1.remove(element_1)
    inc += 1
print(list_1)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
print("Решение задачи 3")
number_list = [30, 13, 29, 8, 10, 51]
new_number_list = list(number_list)
for index in range(len(new_number_list)):
    if number_list[index] % 2 == 0:
        new_number_list[index] /= 4
    else:
        new_number_list[index] *= 2
print(new_number_list)
