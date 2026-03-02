from main import users, courses, registrations, Registration
from datetime import datetime

# ===============================
# HELPER FUNCTION
# ===============================

def find_user(username):
    for user in users:
        if user.username == username:
            return user
    return None

def show_courses():
    print("\nAvailable Courses:")
    for course in courses:
        print(course.course_id, "-", course.title, "-", course.instructor_name)

def register_course(user):
    show_courses()

    try:
        course_id = int(input("Enter Course ID: "))
    except ValueError:
        print("Invalid input.")
        return

    for course in courses:
        if course.course_id == course_id:

            reg_id = len(registrations) + 1

            new_registration = Registration(
                reg_id,
                user.get_user_id(),
                course.course_id,
                "active",
                datetime.now()
            )

            registrations.append(new_registration)

            print("Registration successful!")
            return

    print("Course not found.")

# ===============================
# MAIN MENU
# ===============================

def main_menu():

    while True:

        print("\n===== COURSE MANAGEMENT SYSTEM =====")
        print("1. Login")
        print("2. View Courses")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            username = input("Username: ")
            password = input("Password: ")

            user = find_user(username)

            if user and user.check_password(password):

                print("Login successful!")

                if user.role == "student":
                    register_course(user)
                else:
                    print("Admins cannot register for courses.")

            else:
                print("Invalid credentials.")

        elif choice == "2":
            show_courses()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


# ===============================
# ENTRY POINT
# ===============================

if __name__ == "__main__":
    main_menu()