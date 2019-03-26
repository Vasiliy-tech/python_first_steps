# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне
fruits = ['яблоко', 'ананас', 'банан', 'апельсин', 'киви', 'мандаринkjfhtfhgjgjhgchghfghfh', 'помело', 'помидор',
          'огурец', 'перец']
print(fruits)
len_max = len(max(fruits, key=len))
print(len_max)
count = 0
for fruit in fruits:
    count += 1
    # Выравнивание необходимым количеством пробелов, 5-отступ от нумерации:
    width = ' ' * (len_max + 5 - len(fruit) - len(str(count)))
    print('{}.'.format(count), '{}'.format(width), '{}'.format(fruit))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
list_1 = [12, 68, ' ', 745, 'dsgg', 45, 12, 12, 98]
list_2 = [35, 36, 785, 45, 63, 12]
for element in list_2:
    while element in list_1:
        list_1.remove(element)
print(list_1)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
set_of_integer = [145, 25, 14, 36, 41]
new_set = []
for unit in set_of_integer:
    if unit % 2 == 0:
        new_set.append(unit / 4)
    else:
        new_set.append(unit * 2)
print(new_set)
