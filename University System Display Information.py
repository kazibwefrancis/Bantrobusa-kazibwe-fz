# University System Display Information

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        print(f"Student - Name: {self.name}, Age: {self.age}, ID: {self.student_id}")

class Lecturer(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_info(self):
        print(f"Lecturer - Name: {self.name}, Age: {self.age}, Subject: {self.subject}")

class Staff(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position

    def display_info(self):
        print(f"Staff - Name: {self.name}, Age: {self.age}, Position: {self.position}")

# Example usage:
people = [
    Student("Francis", 20, "S123"),
    Lecturer("Dr. Jemimah", 45, "Mathematics"),
    Staff("Max", 35, "Administrator")
]

for person in people:
    person.display_info()
