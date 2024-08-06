def add_student(students):
    name = input("Enter the student's name: ")
    if name in students:
        print(f"{name} is already in the system.")
    else:
        students[name] = {}
        print(f"Student {name} added.")

def add_grades(students):
    name = input("Enter the student's name: ")
    if name not in students:
        print(f"Student {name} not found. Please add the student first.")
        return

    num_subjects = int(input("How many subjects do you want to add grades for? "))

    for i in range(num_subjects):
        # Determine the ordinal number (1st, 2nd, 3rd, etc.)
        if i == 0:
            ordinal = "first"
        elif i == 1:
            ordinal = "second"
        elif i == 2:
            ordinal = "third"
        else:
            ordinal = f"{i + 1}th"

        subject = input(f"Enter the {ordinal} subject: ")
        grade = float(input(f"Enter the grade for {subject}: "))

        if subject in students[name]:
            students[name][subject].append(grade)
        else:
            students[name][subject] = [grade]

        print(f"Grade {grade} added for {name} in {subject}.")

def calculate_average(students):
    name = input("Enter the student's name: ")
    if name not in students:
        print(f"Student {name} not found.")
        return

    total_sum = 0
    total_grades = 0

    for subject, grades in students[name].items():
        subject_average = sum(grades) / len(grades)
        total_sum += sum(grades)
        total_grades += len(grades)
        print(f"{subject} average for {name}: {subject_average:.2f}")

    if total_grades > 0:
        overall_average = total_sum / total_grades
        print(f"Overall average for {name}: {overall_average:.2f}")
    else:
        print(f"No grades available for {name}.")
        
def view_all_grades(students):
    for name, subjects in students.items():
        print(f"\nGrades for {name}:")
        for subject, grades in subjects.items():
            print(f"{subject}: {grades}")

def main():
    students = {}

    while True:
        print("\nStudent Grade Tracker")
        print("1. Add Student")
        print("2. Add Grades")
        print("3. Calculate Average")
        print("4. View All Grades")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student(students)
        elif choice == '2':
            add_grades(students)
        elif choice == '3':
            calculate_average(students)
        elif choice == '4':
            view_all_grades(students)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()