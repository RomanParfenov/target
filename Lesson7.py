from pprint import pprint
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):

        if isinstance(lecturer, Lecturer) \
                and grade in range(0, 11) \
                and course in lecturer.courses_attached \
                and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print('Ошибка!')

    def __str__(self):
        if self.grades:
            sum_of_grades = count = 0
            for course_name, grades_list in self.grades.items():
                sum_of_grades += sum(grade for grade in grades_list)
                count += len(grades_list)
            average_mark = round(sum_of_grades / count, 1)
        else:
            average_mark = None

        return 'Имя: {name}\nФамилия: {surname}\nСредняя оценка за домашние задания: ' \
               '{average_mark}\nКурсы в процессе изучения: {courses_in_progress}\nЗавершенные курсы: {courses_finished}\n'\
            .format(
                name=self.name,
                surname=self.surname,
                average_mark=average_mark,
                courses_in_progress=', '.join(self.courses_in_progress),
                courses_finished=', '.join(self.finished_courses)
        )


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.grades = {}
        super(Lecturer, self).__init__(name, surname)

    def __str__(self):
        if self.grades:
            sum_of_grades = count = 0
            for course_name, grades_list in self.grades.items():
                sum_of_grades += sum(grade for grade in grades_list)
                count += len(grades_list)
            average_mark = round(sum_of_grades / count, 1)
        else:
            average_mark = None

        return 'Имя: {name}\nФамилия: {surname}\nСредняя оценка за лекции: {average_mark}\n'.format(
            name=self.name, surname=self.surname, average_mark=average_mark
        )


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return 'Имя: {name}\nФамилия: {surname}\n'.format(
            name=self.name, surname=self.surname
        )


# Ethereum creators
student_1 = Student('Vitalik', 'Buterin', 'male')
student_2 = Student('Anthony ', 'Di Iorio', 'male')


lecturer_1 = Lecturer('Gvido', 'Van Rossum')
lecturer_2 = Lecturer('Satoshi', 'Nakamoto')


lecturer_1.courses_attached += ['Python']
lecturer_2.courses_attached += ['Cryptography and Cryptocurrencies', 'Python']

student_1.courses_in_progress += ['Python', 'Cryptography and Cryptocurrencies']
student_2.courses_in_progress += ['Python', 'Cryptography and Cryptocurrencies']

reviewer_1 = Reviewer('Gavin ', 'Wood')
reviewer_2 = Reviewer('Adam', 'Back')

reviewer_1.courses_attached += ['Cryptography and Cryptocurrencies', 'Python']
reviewer_2.courses_attached += ['Cryptography and Cryptocurrencies']


reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_2.rate_hw(student_1, 'Cryptography and Cryptocurrencies', 8)
reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_2, 'Python', 6)
reviewer_1.rate_hw(student_2, 'Cryptography and Cryptocurrencies', 9)
reviewer_2.rate_hw(student_2, 'Cryptography and Cryptocurrencies', 8)


student_1.rate_lecturer(lecturer_1, 'Python', 7)
student_2.rate_lecturer(lecturer_1, 'Python', 5)
student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_2, 'Python', 10)
student_2.rate_lecturer(lecturer_2, 'Python', 9)
student_2.rate_lecturer(lecturer_2, 'Cryptography and Cryptocurrencies', 9)

print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(reviewer_2)


def students_avg_grade(students_list, course):
    sum_of_grades = count = 0
    for student in students_list:
        if course in student.grades:
            sum_of_grades += sum(student.grades[course])
            count += len(student.grades[course])
    if count:
        print(round(sum_of_grades / count, 1))
    else:
      # Отсутствие оценок
        print('Ошибка!')


def lecturers_avg_grade(lecturers_list, course):
    sum_of_grades = count = 0
    for lecturer in lecturers_list:
        if course in lecturer.grades:
            sum_of_grades += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    if count:
        print(round(sum_of_grades / count, 1))
    else:
        # Отсутствие оценок
        print('Ошибка!')

students_avg_grade([student_1, student_2], 'Python')
lecturers_avg_grade([lecturer_1, lecturer_2], 'Python')



