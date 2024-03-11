class StudentManagement:
    def __init__(self):
        # Initialize dictionary to store student information
        self.students = {}

    def signup(self, student_id, password, name, phone, email):
        if student_id in self.students:
            print("Student ID already exists. Please choose a different one.")
        else:
            self.students[student_id] = {'password': password, 'name': name, 'email': email, 'phone': phone}
            print("Account created successfully.")

    def login(self, student_id, password):
        if student_id in self.students and self.students[student_id]['password'] == password:
            print("Login successful.\nWelcome,", self.students[student_id]['name'])
            return True
        else:
            print("Invalid student ID or password.")
            return False

    def disp_student_info(self, student_id):
        # Display the information if student id is present in the dictionary
        if student_id in self.students:
            student_info = self.students[student_id]
            print(f"Student ID: {student_id}")
            print(f"Name: {student_info['name']}")
            print(f"Phone: {student_info['phone']}")
            print(f"Email: {student_info['email']}")
        else:
            print("Student ID not found.")


student_manage = StudentManagement()

# Sign up
student_manage.signup(101, 'password@123', 'Sam', 1234567890, 'sam@mail.com')

# Login
if student_manage.login(101, 'password@123'):
    # Get student information
    student_manage.disp_student_info(101)
