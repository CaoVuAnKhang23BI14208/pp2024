students = []
courses = []
marks = {}

def input_no_of_students():
    return int(input("Enter number of students")) 

def input_student_infor():
    number = input_no_of_students()
    for i in range(number):
        student_id = input('Enter student id:')
        student_name = input('Enter student name:')
        student_dob = input('Enter student dob:')
        students.append((student_id, student_name, student_dob))
        print()

def input_no_of_course():
    number = int(input('Enter number of courses'))
    return number

def input_course_infor():
    number = input_no_of_course()
    for i in range(number):
        course_id = input('Enter course id:')
        course_name = input('Enter course name')

        courses.append((course_id, course_name))
        marks[course_id] = {}

def input_marks():
    course_id = input("Enter course id:")
    for student_id, name, _  in students:
        mark = float(input(f"Enter mark for {name}, id: {student_id}:"))
        marks[course_id][student_id] = mark

def list_courses():
    for course_id, name in courses:
        print(f"Course id:{course_id} - name:{name}")

def list_students():
    for student_id, name, dob in students:
        print(f"Student id: {student_id} - name:{name} - DOB: {dob}") 

def show_marks():
    course_id = input("Enter course id:")
    for student_id, name, _ in students:
        mark = marks[course_id][student_id]
        print(f"Student id: {student_id} - name:{name} - mark: {mark}") 

def main():
    while True:
        print('1. Input number of students')
        print('2. Input student information')
        print('3. Input number of course')
        print('4. Input course informatin')
        print('5. Input marks for student')
        print('6. List courses')
        print('7. List student')
        print('8. Show student marks')
        
        option = int(input("Your option:"))

        if option == 1:
            input_no_of_students()
        elif option == 2:
            input_student_infor()
        elif option == 3:
            input_no_of_course()
        elif option == 4:
            input_course_infor()
        elif option == 5:
            input_marks()
        elif option == 6:
            list_courses()
        elif option == 7:
            list_students()
        elif option == 8:
            show_marks()
        else:
            print('Invalid')

if __name__ == "__main__":
    main()