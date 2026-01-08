def main():
    print("Student Registration Form:-")

    students = [] 

    while True:
      
    #   
        student = {
            "first_name": input("Enter First Name: "),
            "last_name": input("Enter Last Name: "),
            "age": input("Enter Age: "),
            "gender": input("Enter Gender: "),
            "email": input("Enter Email: "),
            "phone": input("Enter Phone: "),
            "course": input("Enter Course: "),
            "city": input("Enter City: "),
            "country": input("Enter Country: ")
        }

       
        students.append(student)

       
        more = input("Do you want to add another student? (yes/no): ").lower()
        if more != "yes":
            break

   
    print("\n Registration Completed")


# show registered students
    for student in students:
        print("Hello " + student["first_name"])
        print("You are registered below are your details\n")
        print("First Name: " + student["first_name"])
        print("Last Name: " + student["last_name"])
        print("Age: " + student["age"])
        print("Gender: " + student["gender"])
        print("Email: " + student["email"])
        print("Phone: " + student["phone"])
        print("Course: " + student["course"])
        print("City: " + student["city"])
        print("Country: " + student["country"])
        print() 


if __name__ == "__main__":
    main()
