# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# # Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# # если отработают норму часов. Если же они отработали меньше нормы,
# # то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# # удвоенную ЗП, пропорциональную норме.
# # Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"
#
# # С использованием классов.
# # Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# # каждый работник получал строку из файла
import re


class Worker:

    def __init__(self, str):
        self._str = str
        element = re.findall(r'\w+', str)
        self._name = element[0]
        self._surname = element[1]
        self._salary = int(element[2])
        self._position = element[3]
        self._hour_rate = int(element[4])

    def __str__(self):
        return '{} {}'.format(self._name, self._surname)

    def findHours(self):
        hours_file = open('hours_of.txt','r', encoding='UTF-8')
        for line in hours_file:
            if self._name in line and self._surname in line:
                element = re.findall(r'\w+', line)
                self._work_hours = int(element[-1])
        hours_file.close()
        return self._work_hours

    def fullSalary(self):
        if self.findHours() <= self._hour_rate:
            return self.findHours() / self._hour_rate * self._salary
        else:
            return self._salary + (self.findHours() - self._hour_rate) * self._salary / self._hour_rate * 2


workers = []
works_file = open('workers.txt','r', encoding='UTF-8')
headline = works_file.readline()
for line in works_file:
    workers.append(Worker(line))
works_file.close()
for worker in workers:
    print("Работник: {}, зарплата - {} рублей".format(worker, worker.fullSalary()))






