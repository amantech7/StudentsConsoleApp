from form.questions import ask_student_details
from utils.display import show_student

#  list to store all students
students = []

def main():
    print("Student Registration Form:-")

    while True:
        student = ask_student_details()
        students.append(student)

        more = input("Do you want to add another student? (yes/no): ").lower()
        if more != "yes":
            break

    print("\nRegistration Completed\n")

    # print all students
    for student in students:
        show_student(student)

    print("Total Students Registered: " + str(len(students)))


if __name__ == "__main__":
    main()
