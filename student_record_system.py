# Student Record Management System

students = []   # List to store all student dictionaries


# ---------------------- Utility Functions ----------------------

def calculate_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 75:
        return 'B'
    elif average >= 60:
        return 'C'
    elif average >= 50:
        return 'D'
    else:
        return 'F'


def find_student(roll_number):
    for student in students:
        if student['roll'] == roll_number:
            return student
    return None


# ---------------------- Core Functions ----------------------

def add_student():
    roll = input("Enter Roll Number: ")

    # Bonus: Prevent duplicate roll numbers
    if find_student(roll):
        print("⚠ Student with this Roll Number already exists!")
        return

    name = input("Enter Student Name: ")

    marks = []
    for i in range(1, 6):
        mark = float(input(f"Enter marks for Subject {i}: "))
        marks.append(mark)

    total = sum(marks)
    average = total / 5
    grade = calculate_grade(average)

    student = {
        "name": name,
        "roll": roll,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }

    students.append(student)
    print("✅ Student added successfully!")


def view_all_students():
    if not students:
        print("No student records found.")
        return

    print("\n----- All Students -----")
    for student in students:
        print(f"""
Name     : {student['name']}
Roll No  : {student['roll']}
Marks    : {student['marks']}
Total    : {student['total']}
Average  : {student['average']:.2f}
Grade    : {student['grade']}
------------------------------
""")


def search_student():
    roll = input("Enter Roll Number to search: ")
    student = find_student(roll)

    if student:
        print("\nStudent Found:")
        print(f"""
Name     : {student['name']}
Roll No  : {student['roll']}
Marks    : {student['marks']}
Total    : {student['total']}
Average  : {student['average']:.2f}
Grade    : {student['grade']}
""")
    else:
        print("❌ Student not found.")


def class_statistics():
    if not students:
        print("No data available.")
        return

    total_students = len(students)
    class_average = sum(s['average'] for s in students) / total_students

    highest = max(students, key=lambda x: x['total'])
    lowest = min(students, key=lambda x: x['total'])

    print("\n----- Class Statistics -----")
    print(f"Total Students : {total_students}")
    print(f"Class Average  : {class_average:.2f}")
    print(f"Highest Scorer : {highest['name']} ({highest['total']})")
    print(f"Lowest Scorer  : {lowest['name']} ({lowest['total']})")

    # Bonus: Grade Distribution
    grade_count = {}
    for s in students:
        grade = s['grade']
        grade_count[grade] = grade_count.get(grade, 0) + 1

    print("\nGrade Distribution:")
    for grade, count in grade_count.items():
        print(f"{grade} : {count}")


def update_marks():
    roll = input("Enter Roll Number to update marks: ")
    student = find_student(roll)

    if not student:
        print("❌ Student not found.")
        return

    new_marks = []
    for i in range(1, 6):
        mark = float(input(f"Enter new marks for Subject {i}: "))
        new_marks.append(mark)

    student['marks'] = new_marks
    student['total'] = sum(new_marks)
    student['average'] = student['total'] / 5
    student['grade'] = calculate_grade(student['average'])

    print("✅ Marks updated successfully!")


def sort_students():
    if not students:
        print("No student data available.")
        return

    sorted_list = sorted(students, key=lambda x: x['total'], reverse=True)

    print("\n----- Students Sorted by Total Marks -----")
    for s in sorted_list:
        print(f"{s['name']} ({s['roll']}) - Total: {s['total']}")


# ---------------------- Main Menu ----------------------

def main():
    while True:
        print("""
===== Student Record Management System =====
1. Add Student
2. View All Students
3. Search Student
4. Class Statistics
5. Update Student Marks
6. Sort Students by Total Marks
7. Exit
""")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_all_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            class_statistics()
        elif choice == '5':
            update_marks()
        elif choice == '6':
            sort_students()
        elif choice == '7':
            print("Exiting program... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()