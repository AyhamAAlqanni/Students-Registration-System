# 📘 Student Registration System

# Description
This Python program implements a simple Student Registration System for managing students, courses, and grades. The program allows the user to add students, courses, grades, and generate student transcripts while maintaining data persistence through text files. GPA is automatically calculated and updated upon adding new grades.

The system is modular, structured using object-oriented programming (OOP), and stores data in three text files to avoid redundancy.

# Features

- ✔️ Add new students (with unique IDs).
- ✔️ Add new courses (with unique course numbers).
- ✔️ Add new grades (validates student ID and course number).
- ✔️ Automatically updates GPA after adding grades.
- ✔️ Print student transcripts (includes GPA and course history).
- ✔️ Modify student information (name or mobile number).
- ✔️ Delete a student (removes grades too).
- ✔️ Input validation for all menu options.

# File Structure

- HW2.py – Main Python file containing all functionality and menu interface.
- Student_Class.py – Defines the Student class.
- Course_Class.py – Defines the Course class.
- Grade_Class.py – Defines the Grade class.
- Files/Students.txt – Stores students' data.
- Files/Courses.txt – Stores courses' data.
- Files/Grades.txt – Stores students' grades.

# 💡 GPA Calculation
- Grades are converted to points:

Grade	Points
A	    4
B	    3
C	    2
D	    1
F	    0

- GPA is calculated as: GPA = (sum of (grade points × course credits)) / (sum of credits)

# 💻 How to Run

1. Place all files (HW2.py, class files, and Files folder) in the same directory.
2. Open a terminal and run: python HW2.py

# 🔒 Notes
1. Only grades A, B, C, D, F are accepted.
2. Mobile number is formatted automatically (e.g., 1234567890 → (123)456-7890).
3. The program handles invalid input types and prompts again if necessary.

# 📎 Author
Developed by Ayham Alqanni