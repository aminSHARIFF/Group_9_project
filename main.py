# ==================================
#            CLASSES
# ==================================

class User:
    def __init__(self, user_id, username, password, role):
        self.__user_id = user_id
        self.username = username
        self.__password = password
        self.role = role

    def check_password(self, password):
        #boolean comparison
        return self.__password == password


class Admin(User):
    def __init__(self, user_id, username, password):
        super().__init__(user_id, username, password, "admin")


class Student(User):
    def __init__(self, user_id, username, password):
        super().__init__(user_id, username, password, "student")
        self.enrolled_courses = []


class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name


# ==================================
#         SYSTEM CLASS
# ==================================

class System:

    def __init__(self):
        self.users = []
        self.courses = []

        # Pre-created users
        admin1 = Admin(1, "admin", "1234")
        student1 = Student(2, "ali", "1111")

        self.users.append(admin1)
        self.users.append(student1)

    # ---------------------------
    # LOGIN
    # ---------------------------
    #its job is To check if the entered username and password match a user in the system.
    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.check_password(password):
                return user
        return None

    # ---------------------------
    # CREATE COURSE
    # ---------------------------
    def create_course(self, course_id, course_name):
        new_course = Course(course_id, course_name)
        self.courses.append(new_course)

    # ---------------------------
    # GET COURSES
    # ---------------------------
    def get_courses(self):
        return self.courses

    # ---------------------------
    # ENROLL STUDENT
    # ---------------------------
    def enroll_student(self, student, course_id):

        for course in self.courses:
            if course.course_id == course_id:
                student.enrolled_courses.append(course)
                return True

        return False





