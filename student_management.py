class Student: 
    def __init__(self, student_id, name, gender, age, course):
        self.student_id = student_id
        self.name = name
        self.gender = gender
        self.age = age
        self.course = course

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Gender: {self.gender}, Age: {self.age}, Course: {self.course}"

# List to store student records
list_students = []

def add_student():
    student_id = input("Enter Student ID: ").title()
    student_name = input("Enter Student Name: ").title()
    student_gender = input("Enter Student Gender: ").title()
    student_age = int(input("Enter Student Age: "))
    student_course = input("Enter Student Course: ").title()

    new_student = Student(student_id, student_name, student_gender, student_age, student_course)
    list_students.append(new_student)
    
    print()
    print("Student added successfully.")

def load_students_from_file(filename="students.txt"): 
    try: 
        with open(filename, "r") as file:
            for line in file:
                student_id, student_name, student_gender, student_age, student_course = line.strip().split(", ")
                new_student = Student(student_id, student_name, student_gender, student_age, student_course)
                list_students.append(new_student)
                print("Welcome back! Loaded existing student records.")
    except FileNotFoundError:
        print(f"No existing file named {filename} found. Starting with an empty student list.")

def view_students():

    if not list_students:
        print("No students found.")
        return
    print("--- List of Students ---")
    for index, student in enumerate(list_students, 1):
        print(f"{index}. {student}")

def search_student():
    search_keyword = input("Enter student details to search. ")
    found_students = [student for student in list_students if search_keyword.lower() in str(student).lower()]

    if found_students:
        print("--- Search Results ---")
        for index, student in enumerate(found_students, 1):
            print(f"{index}. {student}")
    
    else:
        print("No matching student found.")

def save_students_to_file(filename="students.txt"):
    with open(filename, "w") as file:
        for student in list_students:
            # save in CSV format for easier parsing instead of using __str__ or (str(student))
            file.write(f"{student.student_id}, {student.name}, {student.gender}, {student.age}, {student.course}\n")
        print(f"Students saved to {filename} successfully.")

def delete_student():
    student_to_delete = input("Enter student ID to delete: ")
    if not list_students:
        print("No students found.")
        return
    
    for student in list_students:
        if student.student_id == student_to_delete:
            list_students.remove(student)
            print(f"Student with ID {student_to_delete} has been deleted.")
            return
        else:
            print(f"No student found with ID {student_to_delete}")
            return
        
def update_student():
    student_to_update = input("Enter student ID to update: ")

    if not list_students:
        print("No students found.")
        return
    
    for student in list_students:
        if student.student_id == student_to_update:
            print("""
                What do you want to update?
                  0. ID
                  1. Name
                  2. Gender
                  3. Age
                  4. Course
                """)
            user_choice = input("Enter your choice (0-4): ")

            match user_choice:
                case "0":
                    new_id = input("Enter new ID:")
                    student.student_id = new_id
                case "1":
                    new_name = input("Enter new Name:")
                    student.name = new_name
                case "2":
                    new_gender = input("Enter new Gender:")
                    student.gender = new_gender
                case "3":
                    new_age = input("Enter new Age:")
                    student.age = new_age
                case "4":
                    new_course = input("Enter new Course:")
                    student.course = new_course
                case _:
                    print("Invalid choice.")
            print("Student record updated successfully.")

def exit_program() :
    print("""Save your changes before exiting.
          1. Save and Exit
          2. Exit without Saving
          3. Cancel
          """)
    
    user_choice = input("Enter your choice (1-3): ")

    match user_choice:
        case "1":
            save_students_to_file("students.txt")
            print("Saving changes and exiting the program.")
            exit()

        case "2":
            print("Exiting without saving changes.")
            exit()

        case "3":
            print("Canceling exit.")
            return
        case _:
            print("Invalid choice. Please enter a number between 1 and 3.")
       
# load existing students from file at the start of the program
load_students_from_file("students.txt")

while True:
    print("""
    Student Management System
        1. Add Student.
        2. View Students.
        3. Search Student.
        4. Save Students to File.
        5. Delete Student.
        6. Update Student.
        7. Exit.
    """)

    # get user input
    user_choice = input("Enter your choice (1-7): ")

    match user_choice:
        case "1":
            add_student()
        case "2":
            view_students()
        case "3":
            search_student()
        case "4":
            save_students_to_file("students.txt")
        case "5":
            delete_student()
        case "6":
            update_student()
        case "7":
            exit_program()
        case _:
            print("Invalid choice. Please enter a number between 1 and 7.")
