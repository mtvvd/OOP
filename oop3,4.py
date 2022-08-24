class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_value = []

    def rate_lecture(self, lecturer, course, grade):

        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_average_student_rating(self, students_grades):
        for elm in students_grades.values():
            average_val = sum(elm) / len(elm)
            self.average_value = average_val

    def __str__(self):
        return f"\nИмя студента: {self.name}\nФамилия студента: {self.surname}\nСредняя оценка от эксперта за Дз: {self.average_value}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"

    def __lt__(self, other):
        return self.average_value < other.average


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades = {}
        self.average = []

    def get_average_lecturer_rating(self, lecturers_grades):
        for elm in lecturers_grades.values():
            sum_v = sum(elm) / len(elm)
            # print(sum_v)
            self.average = sum_v

    def __str__(self):
        return f"\nИмя лектора: {self.name}\nФамилия лектора: {self.surname}\nСредняя оценка от студента за лекции: {self.average}"

    def __lt__(self, other):
        return self.average < other.average_value


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"\nИмя эксперта: {self.name}\nФамилия эксперта: {self.surname}"


first_Lecturer = Lecturer('Oliver', 'Williams')
first_Lecturer.courses_attached += ['Python', 'Git']

second_Lecturer = Lecturer('Brian', 'Kelly')
second_Lecturer.courses_attached += ['Python', 'Git']

first_student = Student('Jack', 'Gibson', 'your_gender')
first_student.courses_in_progress += ['Python', 'Git']
first_student.finished_courses += ['Английский для программистов', 'Введение в программирование']

second_student = Student('Edward', 'Graham', 'your_gender')
second_student.courses_in_progress += ['Python', 'Git']
second_student.finished_courses += ['Английский для программистов', 'Введение в программирование']

first_Reviewer = Reviewer('Charley', 'Grant')
first_Reviewer.courses_attached += ['Python', 'Git']

second_Reviewer = Reviewer('Oscar', 'Davis')
second_Reviewer.courses_attached += ['Python', 'Git']

first_student.rate_lecture(first_Lecturer, 'Python', 10)
first_student.rate_lecture(first_Lecturer, 'Python', 9)
first_student.rate_lecture(first_Lecturer, 'Python', 8)
first_student.rate_lecture(first_Lecturer, 'Python', 10)

second_student.rate_lecture(second_Lecturer, 'Python', 10)
second_student.rate_lecture(second_Lecturer, 'Python', 7)
second_student.rate_lecture(second_Lecturer, 'Python', 8)
second_student.rate_lecture(second_Lecturer, 'Python', 9)

first_student.rate_lecture(first_Lecturer, 'Git', 1)
first_student.rate_lecture(first_Lecturer, 'Git', 7)
first_student.rate_lecture(first_Lecturer, 'Git', 7)
first_student.rate_lecture(first_Lecturer, 'Git', 1)

second_student.rate_lecture(second_Lecturer, 'Git', 9)
second_student.rate_lecture(second_Lecturer, 'Git', 5)
second_student.rate_lecture(second_Lecturer, 'Git', 4)
second_student.rate_lecture(second_Lecturer, 'Git', 2)

print("Оценки 1-го лектора за лекцию от 1-го студента", first_Lecturer.grades)
print("Оценки 2-го лектора за лекцию от 2-го студента", second_Lecturer.grades)

first_Reviewer.rate_hw(first_student, 'Python', 10)
first_Reviewer.rate_hw(first_student, 'Python', 9)
first_Reviewer.rate_hw(first_student, 'Python', 8)
first_Reviewer.rate_hw(first_student, 'Python', 7)

second_Reviewer.rate_hw(second_student, 'Python', 10)
second_Reviewer.rate_hw(second_student, 'Python', 6)
second_Reviewer.rate_hw(second_student, 'Python', 8)
second_Reviewer.rate_hw(second_student, 'Python', 5)

first_Reviewer.rate_hw(first_student, 'Git', 6)
first_Reviewer.rate_hw(first_student, 'Git', 10)
first_Reviewer.rate_hw(first_student, 'Git', 4)
first_Reviewer.rate_hw(first_student, 'Git', 9)

second_Reviewer.rate_hw(second_student, 'Git', 7)
second_Reviewer.rate_hw(second_student, 'Git', 3)
second_Reviewer.rate_hw(second_student, 'Git', 9)
second_Reviewer.rate_hw(second_student, 'Git', 9)

print("Оценки 1-го студента за Дз от 1-го эксперта", first_student.grades)
print("Оценки 2-го студента за Дз от 2-го эксперта", second_student.grades)

first_student.get_average_student_rating(
    first_student.grades)  
second_student.get_average_student_rating(second_student.grades)
first_Lecturer.get_average_lecturer_rating(first_Lecturer.grades)
second_Lecturer.get_average_lecturer_rating(second_Lecturer.grades)

print(first_Reviewer)
print(second_Reviewer)

print(first_Lecturer)
print(second_Lecturer)

print(first_student)
print(second_student)

print('\nЗадание 3.2 сравнение оценок лекторов и студентов')
print(first_student < first_Lecturer)
print(first_student.average_value < first_Lecturer.average)

print(first_student.average_value >= second_Lecturer.average)

print(second_student.average_value > second_Lecturer.average)

print(first_Lecturer.average < second_Lecturer.average)



students_list = [first_student, second_student]
lecturers_list = [first_Lecturer, second_Lecturer]


def get_average_students_mark(data, course):
    total = []
    for el in data:
        total.append(sum(el.grades[course]) / len(el.grades[course]))
    print(f'Средняя оценка студентов по курсу {course}: {sum(total) / len(total)}')


def get_average_lecturers_mark(data, course):
    total = []
    for el in data:
        total.append(sum(el.grades[course]) / len(el.grades[course]))
    print(f'Средняя оценка лекторов по курсу {course}: {sum(total) / len(total)}')


get_average_students_mark(students_list, 'Python')
get_average_students_mark(students_list, 'Git')

get_average_lecturers_mark(lecturers_list, 'Python')
get_average_lecturers_mark(lecturers_list, 'Git')