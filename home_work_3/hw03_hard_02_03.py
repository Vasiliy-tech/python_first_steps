# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

with open('workers.txt', 'r', encoding='UTF-8') as file_workers:
    data = file_workers.readline()
    name_index = data.find("Имя")
    surname_index = data.find("Фамилия")
    salary_index = data.find("Зарплата")
    position_index = data.find("Должность")
    hour_rate_index = data.find("Норма_часов")
    for line in file_workers:
        full_name = line[name_index:line.find(" ", surname_index)]
        hour_rate = int(line[line.rfind(' '):])
        salary = int(line[salary_index:line.find(" ", salary_index)])
        with open('hours_of.txt', 'r', encoding='UTF-8') as file_hours:
            headline = file_hours.readline()
            for line_of_hours in file_hours:
                hours_worked = int(line_of_hours[line_of_hours.rfind(' '):])
                if full_name in line_of_hours:
                    if hours_worked <= hour_rate:
                        full_salary = hours_worked / hour_rate * salary
                        print('{:<16}: {:<10}'.format(full_name, full_salary))
                    else:
                        full_salary = salary + hours_worked % hour_rate * salary / hour_rate * 2
                        print('{:<16}: {:<10}'.format(full_name, full_salary))

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
capital_letters = list(map(chr, range(ord('А'), ord('Я') + 1)))
for letter in capital_letters:
    name_of_file = "fruits_" + letter + ".txt"
    with open('fruits.txt', 'r', encoding="UTF-8") as file_fruits:
        for line in file_fruits:
            if letter in line:
                with open(name_of_file, 'a', encoding='UTF-8') as new_fruits_file:
                    new_fruits_file.write(line)
# не понимаю, почему невозможно объединить строки 48 и 49 (выдает SyntaxError)
