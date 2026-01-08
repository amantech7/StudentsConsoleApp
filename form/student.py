

# function to create a student
def create_student(first_name, middle_name, last_name, dob, age, gender, email, phone, desired_course, city, country):
    return {
        "first_name": first_name,
        "middle_name": middle_name,
        "last_name": last_name,
        "dob": dob,
        "age": age,
        "gender": gender,
        "email": email,
        "phone": phone,
        "desired_course": desired_course,
        "city": city,
        "country": country
    }
