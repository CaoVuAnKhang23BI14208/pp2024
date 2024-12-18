class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob


class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name
        self.marks = {}


class SchoolManagement:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_no_of_students(self):
        return int(input("Enter number of students: "))

    def input_student_info(self):
        number = self.input_no_of_students()
        for _ in range(number):
            student_id = input("Enter student id: ")
            student_name = input("Enter student name: ")
            student_dob = input("Enter student DOB: ")
            self.students.append(Student(student_id, student_name, student_dob))
            print()

    def input_no_of_courses(self):
        return int(input("Enter number of courses: "))

    def input_course_info(self):
        number = self.input_no_of_courses()
        for _ in range(number):
            course_id = input("Enter course id: ")
            course_name = input("Enter course name: ")
            self.courses.append(Course(course_id, course_name))

    def input_marks(self):
        course_id = input("Enter course id: ")
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if not course:
            print("Invalid course id!")
            return

        for student in self.students:
            mark = float(input(f"Enter mark for {student.name}, id: {student.student_id}: "))
            course.marks[student.student_id] = mark

    def list_courses(self):
        for course in self.courses:
            print(f"Course id: {course.course_id} - name: {course.name}")

    def list_students(self):
        for student in self.students:
            print(f"Student id: {student.student_id} - name: {student.name} - DOB: {student.dob}")

    def show_marks(self):
        course_id = input("Enter course id: ")
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if not course:
            print("Invalid course id!")
            return

        for student in self.students:
            mark = course.marks.get(student.student_id, "No mark")
            print(f"Student id: {student.student_id} - name: {student.name} - mark: {mark}")

    def main_menu(self):
        while True:
            print("1. Input number of students")
            print("2. Input student information")
            print("3. Input number of courses")
            print("4. Input course information")
            print("5. Input marks for students")
            print("6. List courses")
            print("7. List students")
            print("8. Show student marks")
            print("9. Exit")

            option = int(input("Your option: "))

            if option == 1:
                self.input_no_of_students()
            elif option == 2:
                self.input_student_info()
            elif option == 3:
                self.input_no_of_courses()
            elif option == 4:
                self.input_course_info()
            elif option == 5:
                self.input_marks()
            elif option == 6:
                self.list_courses()
            elif option == 7:
                self.list_students()
            elif option == 8:
                self.show_marks()
            elif option == 9:
                print("Exiting...")
                break
            else:
                print("Invalid option!")


if __name__ == "__main__":
    system = SchoolManagement()
    system.main_menu()
