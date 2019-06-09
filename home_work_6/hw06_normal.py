# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class School:
    def __init__(self, school_name, school_adress, teachers, students):
        self._school_name = school_name
        self._school_adress = school_adress
        self._teachers = teachers # список объектов Teacher
        self._students = students # список объектов Student


class People:
    def __init__(self, last_name, first_name, middle_name):
        self._last_name = last_name
        self._first_name = first_name
        self._middle_name = middle_name

    def __str__(self):
        return '{} {} {}'.format(self._last_name, self._first_name, self._middle_name)


class Student(People):
    def __init__(self, last_name, first_name, middle_name,
                 class_room, mother, father):
        People.__init__(self, last_name, first_name, middle_name)
        self._class_room = class_room
        self._parents = {
            'mother': mother,
            'father': father,
            }

    def __str__(self):
        return '{} {}. {}.'.format(self._last_name, self._first_name[0], self._middle_name[0])

    def showParents(self):
        return 'Отец: {}, Мать: {}'.format(self._parents['father'], self._parents['mother'])


class Teacher(People):
    def __init__(self, last_name, first_name, middle_name, courses, classes):
        People.__init__(self, last_name, first_name, middle_name)
        self._courses = courses
        self._classes = classes

students = [
           Student("Антонов", "Андрей", "Антонович", "11А", People("Антонова", "Лидия", "Филипповна"),
                   People("Антонов", "Антон", "Андреевич")),
           Student("Игнатьев", "Игорь", "Иванович", "11А", People("Игнатьева", "Агриппина", "Львовна"),
                   People("Игнатьев", "Иван", "Лукич")),
           Student("Кириллов", "Артем", "Ильич", "9А", People("Кириллова", "Дарья", "Викторовна"),
                   People("Кириллов", "Илья", "Аркадьевич")),
           Student("Сергеев", "Сергей", "Сергеевич", "8А", People("Сергеева", "Агата", "Ивановна"),
                   People("Сергеев", "Сергей", "Владимирович")),
           Student("Яковлев", "Ян", "Дмитриевич", "8А", People("Яковлева", "Анна", "Сергеевна"),
                   People("Яковлев", "Дмитрий", "Харитонович"))
           ]

teachers = [
           Teacher("Хренов", "Тихон", "Малафеевич", "Физика", ["11А", "8А"]),
           Teacher("Важнова", "Юлия", "Викторовна", "Химия", ["11А", "9А"]),
           Teacher("Смирнов", "Александр", "Витальевич", "ОБЖ", ["9А", "8А"]),
           Teacher("Чернявский", "Валентин", "Викторович", "Музыка", ["11А", "8А", "9А"]),
           Teacher("Копытов", "Василий", "Викторович", "Информатика", ["9А"]),
           ]

school = School("Школа №1", "Москва, Яблочная ул., 32", students, teachers)
classes = []
pupils = []
# почему подчеркивает, когда я for и if хочу написать в одну строку?
for student in students:
    if student._class_room not in set(classes):
        classes.append(student._class_room)
print("Список классов в школе {}: {}".format(school._school_name, classes))
class_room = input("Список учеников какого класса тебе нужен? ")
for student in students:
    if student._class_room == class_room:
        pupils.append(student)
        print(student)
if len(pupils) == 0:
    print("В указанном классе нет учеников")
for student in students:
    print(student, student.showParents())
for class_room in classes:
    print("Список учителей в {} классе:".format(class_room))
    for teacher in teachers:
        if class_room in teacher._classes:
            print(teacher)


def lessons_list(pupil):
    list_of_lessons = []
    for teacher in teachers:
        if pupil._class_room in teacher._classes:
            list_of_lessons.append(teacher._courses)
    return list_of_lessons


for student in students:
    print('Ученик: {}, Класс: {}, Предметы: {}'.format(student, student._class_room, lessons_list(student)))
