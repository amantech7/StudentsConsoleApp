from form.student import create_student

def ask_student_details():

    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    age = input("Enter Age: ")

    gender = input("Enter Gender: ")
    email = input("Enter Email: ")
    
    phone = input("Enter Phone: ")
    course = input("Enter Course: ")
    city = input("Enter City: ")
    country = input("Enter Country: ")

    return create_student(
        first_name, last_name, age, gender, email, phone, course, city, country
    )
