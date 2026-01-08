from datetime import datetime
from form.student import create_student

def is_valid_name(name):
    for ch in name:
        if not (ch.isalpha() or ch == " "):
            return False
    return True


def ask_student_details():

    while True:
        first_name = input("Enter First Name: ").strip()
        if first_name != "" and is_valid_name(first_name):
            break
        print("First Name is required and must contain only letters.")

    while True:
        middle_name = input("Enter Middle Name (optional): ").strip()
        if middle_name == "" or is_valid_name(middle_name):
            break
        print("Middle Name must contain only letters.")

    while True:
        last_name = input("Enter Last Name: ").strip()
        if last_name != "" and is_valid_name(last_name):
            break
        print("Last Name is required and must contain only letters.")


# date of birth validation
    while True:
        dob = input("Enter Date of Birth (DD-MM-YYYY): ").strip()
        try:
            dob_date = datetime.strptime(dob, "%d-%m-%Y")
            if dob_date > datetime.now():
                print("Date of birth cannot be in the future.")
            else:
                break
        except ValueError:
            print("Invalid date format. Use DD-MM-YYYY.")

    while True:
        age = input("Enter Age: ").strip()
        if age.isdigit() and int(age) > 0:
            break
        print("Age must be a valid positive number.")

    while True:
        gender = input("Enter Gender (Male/Female/Other): ").strip()
        if gender.lower() in ["male", "female", "other"]:
            break
        print("Gender must be Male, Female, or Other.")

    while True:
        email = input("Enter Email: ").strip()
        if "@" in email and "." in email:
            break
        print("Invalid Email format..")

    while True:
        phone = input("Enter Phone Number: ").strip()
        if phone.isdigit() and len(phone) == 10:
            break
        print("Enter a valid 10-digit phone number.")

    while True:
        desired_course = input("Enter Desired Course: ").strip()
        if desired_course != "":
            break
        print("Desired Course is required.")

    while True:
        city = input("Enter City: ").strip()
        if city != "":
            break
        print("City is required.")

    while True:
        country = input("Enter Country: ").strip()
        if country != "":
            break
        print("Country is required.")

    return create_student(
        first_name, middle_name, last_name, dob, age, gender, email, phone, desired_course, city, country
    )
