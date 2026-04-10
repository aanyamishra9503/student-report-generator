from grading import calculate_percentage, calculate_grade
from student import Student
from storage import save_student, fetch_all_reports
from storage import find_by_roll
from storage import delete_by_roll
from storage import update_by_roll
import logger_setup
import logging

def get_student_input():
    roll = input("Roll number: ")
    name = input("Name: ")
    class_name = input("Class: ")

    marks = {}

    for subject in ["Maths", "Physics", "Chemistry"]:
        while True:
            try:
                marks[subject] = int(input(f"{subject} marks: "))
                break
            except ValueError:
                print("Enter valid marks")

    return Student(roll, name, class_name, marks)

def generate_report():
    student = get_student_input()

    percent = calculate_percentage(student.marks)
    grade = calculate_grade(percent)

    save_student(student, percent, grade)

    logging.info(f"Report generated for Roll {student.roll}")

    print("\n--- STUDENT REPORT ---")
    print("Name:", student.name)
    print("Roll:", student.roll)
    print("Class:", student.class_name)
    print("Marks:", student.marks)
    print("Percentage:", percent)
    print("Grade:", grade)

def view_reports():
    reports = fetch_all_reports()

    if not reports:
        print("No reports found.")
        return

    print("\n--- ALL REPORTS ---")

    for r in reports:
        print(r)

def find_student():
    roll = input("Enter roll number to search: ")

    result = find_by_roll(roll)

    if result:
        print("\n--- STUDENT FOUND ---")
        print("Roll:", result[0])
        print("Name:", result[1])
        print("Class:", result[2])
        print("Maths:", result[3])
        print("Physics:", result[4])
        print("Chemistry:", result[5])
        print("Percentage:", result[6])
        print("Grade:", result[7])
    else:
        print("Student not found.")

#review

def delete_student():
    roll = input("Enter roll number to delete: ")

    student = find_by_roll(roll)

    if student:
        delete_by_roll(roll)
        print("Student deleted successfully.")
        logging.info(f"Deleted student Roll {roll}")
    else:
        print("Student not found.")

#review

def update_student():
    roll = input("Enter roll number to update: ")

    student = find_by_roll(roll)

    if not student:
        print("Student not found.")
        return

    print("Enter new details (leave blank if no new value):")

    name = input("Name [" + student[1] + "]: ")
    if name == "":
        name = student[1]

    class_name = input("Class [" + student[2] + "]: ")
    if class_name == "":
        class_name = student[2]

    # FIX: use correct CSV positions
    old_maths = student[3]
    old_physics = student[4]
    old_chem = student[5]

    maths_input = input("Maths marks [" + old_maths + "]: ")
    physics_input = input("Physics marks [" + old_physics + "]: ")
    chem_input = input("Chemistry marks [" + old_chem + "]: ")

    maths = int(maths_input) if maths_input != "" else int(old_maths)
    physics = int(physics_input) if physics_input != "" else int(old_physics)
    chemistry = int(chem_input) if chem_input != "" else int(old_chem)

    marks = {
        "Maths": maths,
        "Physics": physics,
        "Chemistry": chemistry
    }

    total = maths + physics + chemistry
    percent = total / 3
    grade = calculate_grade(percent)

    new_data = [
        roll,
        name,
        class_name,
        maths,
        physics,
        chemistry,
        percent,
        grade
    ]

    update_by_roll(roll, new_data)

    print("Student updated successfully.")


def main():
    while True:
        print("""
--- Student Report Generator ---

1. Generate student report
2. View all reports
3. Find student by roll
4. Update student
5. Delete student
6. Exit
""")

        choice = input("Enter choice: ")
        if choice == "1":
            generate_report()
        elif choice == "2":
            view_reports()
        elif choice == "3":
            find_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            logging.info("Program exited")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()