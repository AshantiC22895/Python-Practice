'''| Feature           | Description                                   |
| ----------------- | --------------------------------------------- |
| Add Student       | Input name, roll no, marks, and store in file |
| View All Students | Read and display records from file            |
| Search by Roll No | Find and show a specific student              |
| Update Record     | Modify a student’s record                     |
| Delete Record     | Remove a student from the file                |
'''

FILENAME = "students.txt"

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    with open(FILENAME, "a") as file:
        file.write(f"{roll},{name},{marks}\n")
    print("Student added successfully.")

def view_students():
    print("\n--- All Student Records ---")
    with open(FILENAME, "r") as file:
        for line in file:
            roll, name, marks = line.strip().split(",")
            print(f"Roll No: {roll} | Name: {name} | Marks: {marks}")

def search_student():
    search_roll = input("Enter Roll No to Search: ")
    found = False
    with open(FILENAME, "r") as file:
        for line in file:
            roll, name, marks = line.strip().split(",")
            if roll == search_roll:
                print(f"Found: {roll} | {name} | {marks}")
                found = True
                break
    if not found:
        print("Student not found.")

def delete_student():
    delete_roll = input("Enter Roll No to Delete: ")
    lines = []
    deleted = False
    with open(FILENAME, "r") as file:
        lines = file.readlines()
    with open(FILENAME, "w") as file:
        for line in lines:
            roll, _, _ = line.strip().split(",")
            if roll != delete_roll:
                file.write(line)
            else:
                deleted = True
    print("Deleted successfully." if deleted else "Roll No not found.")

def menu():
    while True:
        print("\n1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")

menu()
