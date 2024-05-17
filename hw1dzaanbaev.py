class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"Name: {self.fullname}, Age: {self.age}, Married: {self.is_married}")


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def calculate_average_mark(self):
        total_marks = sum(self.marks.values())
        return total_marks / len(self.marks)


class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience, base_salary):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.base_salary = base_salary

    def calculate_salary(self):
        bonus = 0
        if self.experience > 3:
            bonus = (self.experience - 3) * 0.05 * self.base_salary
        return self.base_salary + bonus


def create_students():
    students = []
    student1 = Student("John Doe", 18, False, {"Math": 90, "Science": 85, "History": 88})
    student2 = Student("Jane Smith", 17, False, {"Math": 95, "Science": 92, "History": 85})
    student3 = Student("Alice Johnson", 19, False, {"Math": 88, "Science": 90, "History": 91})
    students.extend([student1, student2, student3])
    return students


def print_student_info(students):
    for student in students:
        student.introduce_myself()
        print("Marks:")
        for subject, mark in student.marks.items():
            print(f"{subject}: {mark}")
        average_mark = student.calculate_average_mark()
        print(f"Average Mark: {average_mark}\n")


teacher = Teacher("Mr. Smith", 35, True, 5, 50000)
teacher.introduce_myself()
print(f"Salary: {teacher.calculate_salary()}\n")

students = create_students()
print_student_info(students)
