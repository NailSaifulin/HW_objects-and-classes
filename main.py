class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Расчёт средней оценки у студентов
    def meangrade(self, course_input=None):
        sum_hw = 0
        counter = 0
        for course, grade in self.grades.items():
            if course_input == None or (course_input != None and course == course_input):
                sum_hw += sum(grade) / len(grade)
                counter += 1
        return round(sum_hw / counter, 2)

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.meangrade()}' \
              f'\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('не является студентом')
            return
        return self.meangrade() < other.meangrade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    # Расчёт средней оценки у лекторов
    def meangrade(self, course_input=None):
        sum_hw = 0
        counter = 0
        for course, grade in self.grades.items():
            if course_input == None or (course_input != None and course == course_input):
                sum_hw += sum(grade) / len(grade)
                counter += 1
        return round(sum_hw / counter, 2)

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.meangrade()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('не является лектором')
            return
        return self.meangrade() < other.meangrade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


# Расчёт средней оценки по списку студентов
def grade_course_student(list_student, course_student):
    sum_grade = 0
    counter_grade = 0
    for iteration_student in list_student:
        if isinstance(iteration_student, Student) and course_student in iteration_student.grades:
            sum_grade += iteration_student.meangrade(course_student)
            counter_grade += 1
    return round(sum_grade / counter_grade, 2)


# Расчёт средней оценки по списку лекторов
def grade_course_lecture(list_lectures, course_lecture):
    sum_grade = 0
    counter_grade = 0
    for iteration_lecture in list_lectures:
        if isinstance(iteration_lecture, Lecturer) and course_lecture in iteration_lecture.grades:
            sum_grade += iteration_lecture.meangrade(course_lecture)
            counter_grade += 1
    return round(sum_grade / counter_grade, 2)


# -----------------------------------------------------------------------------------------------------------#

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']

best_student1 = Student('William', 'Spenser', 'your_gender')
best_student1.courses_in_progress += ['Python']
best_student1.courses_in_progress += ['Java']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Java']

cool_mentor1 = Reviewer('Nick', 'Diaz')
cool_mentor1.courses_attached += ['Python']
cool_mentor1.courses_attached += ['Java']

cool_mentor2 = Lecturer('Fill', 'Collins')
cool_mentor2.courses_attached += ['Python']
cool_mentor2.courses_attached += ['Java']

cool_mentor3 = Lecturer('Francys', 'Nganu')
cool_mentor3.courses_attached += ['Python']
cool_mentor3.courses_attached += ['Java']

cool_mentor.rate_hw(best_student, 'Python', 9)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 7)

cool_mentor.rate_hw(best_student, 'Java', 9)
cool_mentor.rate_hw(best_student, 'Java', 10)
cool_mentor.rate_hw(best_student, 'Java', 10)

cool_mentor.rate_hw(best_student1, 'Python', 8)
cool_mentor.rate_hw(best_student1, 'Python', 9)
cool_mentor.rate_hw(best_student1, 'Python', 7)

cool_mentor.rate_hw(best_student1, 'Java', 10)
cool_mentor.rate_hw(best_student1, 'Java', 9)
cool_mentor.rate_hw(best_student1, 'Java', 10)

best_student.rate_hw(cool_mentor2, 'Java', 10)
best_student.rate_hw(cool_mentor2, 'Java', 9)
best_student.rate_hw(cool_mentor2, 'Java', 10)

best_student.rate_hw(cool_mentor2, 'Python', 10)
best_student.rate_hw(cool_mentor2, 'Python', 9)
best_student.rate_hw(cool_mentor2, 'Python', 10)

best_student1.rate_hw(cool_mentor3, 'Java', 10)
best_student1.rate_hw(cool_mentor3, 'Java', 10)
best_student1.rate_hw(cool_mentor3, 'Java', 10)

best_student1.rate_hw(cool_mentor3, 'Python', 10)
best_student1.rate_hw(cool_mentor3, 'Python', 9)
best_student1.rate_hw(cool_mentor3, 'Python', 7)


print(best_student)
print(best_student > best_student1)
list_student_for_grade = [best_student, best_student1]
print(grade_course_student(list_student_for_grade, 'Java'))

print()
print(cool_mentor2)
print(cool_mentor2 > cool_mentor3)
list_lecturer_for_grade = [cool_mentor2, cool_mentor3]
print(grade_course_lecture(list_lecturer_for_grade, 'Java'))
