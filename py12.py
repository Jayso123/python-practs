class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def get_courses(self):
        return [course.name for course in self.courses]


class Teacher:
    def __init__(self, name, teacher_id):
        self.name = name
        self.teacher_id = teacher_id
        self.courses = []

    def assign_course(self, course):
        self.courses.append(course)

    def get_courses(self):
        return [course.name for course in self.courses]


class Course:
    def __init__(self, name, course_code):
        self.name = name
        self.course_code = course_code
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def get_students(self):
        return [student.name for student in self.students]

    def get_teachers(self):
        return [teacher.name for teacher in self.teachers]


student1 = Student("chhagan", "S101")
student2 = Student("mangu", "S102")

teacher1 = Teacher("Mr. prince", "T001")
teacher2 = Teacher("Mr. dhruvil", "T002")

course1 = Course("python 101", "Py101")
course2 = Course("OS 101", "OS101")

course1.add_student(student1)
course1.add_student(student2)
course1.add_teacher(teacher1)

course2.add_student(student1)
course2.add_teacher(teacher2)

student1.enroll(course1)
student1.enroll(course2)
student2.enroll(course1)

print(f"{student1.name} is enrolled in: {student1.get_courses()}")
print(f"{teacher1.name} teaches: {teacher1.get_courses()}")
print(f"{course1.name} has students: {course1.get_students()}")
