from utils.display import show_student

def show_all_students(students):
    print("\nAll Registered Students:--\n")

    student_number = 1

    for student in students:
        print()
        print("Student #" + str(student_number))
        show_student(student)
        student_number = student_number + 1

    print("Total Students Registered:", len(students))
    print()
