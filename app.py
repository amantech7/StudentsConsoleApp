from form.questions import ask_student_details
from utils.display import show_student
from utils.show_all_student import show_all_students
from utils.student_count import show_total_count

#  list to store all students
students = []

def main():
    print("Student Registration Form:-")

    # Initial registration
    student = ask_student_details()
    students.append(student)

    print("\nRegistration Completed\n")
    
    print("Hello " + student["first_name"])
    print("You are registered below are your details\n")

    show_student(student) 

    show_total_count(students)

    # Menu loop
    while True:
        print("Choose an option:")
        print("1. Add More Students")
        print("2. Show All Students")
        print("3. Show Total Registered Students")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == "1":
            student = ask_student_details()
            students.append(student)
            print("\nRegistration Completed\n")
            show_student(student)

        elif choice == "2":
            show_all_students(students)

        elif choice == "3":
            show_total_count(students)

        elif choice == "4":
            print("\nExiting the program.")
            break

        else:
            print("Invalid choice, please select 1, 2, 3, or 4.\n")


if __name__ == "__main__":
    main()
