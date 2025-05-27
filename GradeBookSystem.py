FILENAME = "grades.txt"
def add_student():
    roll_number = input("Enter Roll number: ")
    student = input("Enter name(First and Last): ")
    grade = input("Enter Grade: ")
    with open (FILENAME,"a") as file:
        file.write(f"{roll_number},{student},{grade}\n")
        print("Added Students Successfully")
        
def view_student():
    print("\n Student Grade Book System")
    with open (FILENAME , "r") as file:
        line = file.readlines()
        if not line:
            print("No Student Found")
            return
        for i, line in enumerate(line, start=1):
            if line.strip():
                try:
                    roll_number, student, grade = line.strip().split(",")
                    print(f"{i}. Roll: {roll_number}, Student: {student}, Grades: {grade}\n")
                except ValueError:
                    print(f"{i}. Skipping malformed task: {line.strip()}")
                    
def search_roll():
    print("\n Search Student Roll Number")
    roll_number = input("Enter Roll Number to Search: ")
    with open (FILENAME, "r") as file:
        line = file.readlines()
        if not line:
            print("No Number Found")
            return
        for i, line in enumerate(line):
            if line.strip():
                try:
                    roll_number = line.strip().split(",")
                    print(f"{i}. Roll: {roll_number}\n")
                except ValueError:
                    print(f"{i}. Skipping malformed task: {line.strip()}")
                    
def update_student():
    roll_number = input("Enter Roll number: ")
    student = input("Enter name(First and Last): ")
    grade = input("Enter Grade: ")
    with open (FILENAME,"w") as file:
        file.write(f"{roll_number},{student},{grade}\n")
        print("Updated Students Successfully")
        
def delete_record():
    with open(FILENAME, "r") as file:
        lines = file.readlines()

    delete = input("What would you like to delete (roll number): ")

    # Create a new list without the line matching the roll number to delete
    new_lines = []
    for line in lines:
        # Assuming each line starts with roll_number,
        if not line.startswith(delete + ","):
            new_lines.append(line)

    with open(FILENAME, "w") as file:
        file.writelines(new_lines)

    print("Deleted record was successfully removed.")

    
    
    
            
    
    
def menu():
    while True:#loops the menu
        print("1. Add Student Records")
        print("2. View all Students")
        print("3. Search Students by Roll Number")
        print("4. Update Student Marks")
        print("5. Delete a Student Record")
        print("6. Exit")
    
        choice = input("Enter choice: ")
    
        if choice == "1":
            add_student()
        elif choice == "2":
            view_student()
        elif choice == "3":
            search_roll()
        elif choice == "4":
                update_student()
        elif choice == "5":
                delete_record()
        elif choice == "6":
            print("GoodBye")   
menu()
    
        
        
    