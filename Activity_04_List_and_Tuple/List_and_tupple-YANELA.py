import os
for file in ["record1.txt", "record2.txt"]:
    if not os.path.exists(file):
        with open(file, "w") as f:
            pass 
records = []

# Menu Options
print("1. Open File")
print("2. Save File")
print("3. Save As File")
print("4. Show All Students Record")
print("5. Order by Last Name")
print("6. Order by Grade")
print("7. Show Student Record")
print("8. Add Record")
print("9. Edit Record")
print("10. Delete Record")
print("11. Exit")

# Default File Name
file_name = "record1.txt"

# Load Existing Records
try:
    file = open(file_name, "r")
    for line in file:
        parts = line.strip().split(",")
        student_id = int(parts[0])
        first_name = parts[1]
        last_name = parts[2]
        class_standing = float(parts[3])
        major_exam = float(parts[4])
        records.append((student_id, (first_name, last_name), class_standing, major_exam))
    file.close()
except FileNotFoundError:
    print("No existing records file found. Starting fresh.")

# Main Loop
while True:
    choice = input("Enter choice: ")
    
    # Open File
    if choice == "1":
        print("Select file to open:")
        print("1. record1.txt")
        print("2. record2.txt")
        file_choice = input("Enter choice: ")
        
        if file_choice == "1":
            file_name = "record1.txt"
        elif file_choice == "2":
            file_name = "record2.txt"
        else:
            print("Invalid choice.")
            continue
        
        try:
            file = open(file_name, "r")
            records = []
            for line in file:
                parts = line.strip().split(",")
                student_id = int(parts[0])
                first_name = parts[1]
                last_name = parts[2]
                class_standing = float(parts[3])
                major_exam = float(parts[4])
                records.append((student_id, (first_name, last_name), class_standing, major_exam))
            file.close()
            print("File opened successfully.")
        except FileNotFoundError:
            print("File not found.")
    
    # Save File
    elif choice == "2":
        file = open(file_name, "w")
        for record in records:
            file.write(f"{record[0]},{record[1][0]},{record[1][1]},{record[2]},{record[3]}\n")
        file.close()
        print("File saved successfully.")
    
    # Save As File
    elif choice == "3":
        new_file_name = input("Enter new file name: ")
        file = open(new_file_name, "w")
        for record in records:
            file.write(f"{record[0]},{record[1][0]},{record[1][1]},{record[2]},{record[3]}\n")
        file.close()
        print("File saved as", new_file_name)
    
    # Show All Student Records
    elif choice == "4": 
        print("\nAll Student Records:")
        print("{:<10} {:<15} {:<15} {:<10} {:<10}".format("ID", "First Name", "Last Name", "Standing", "Exam"))
        print("-" * 60)
        for record in records:
            print("{:<10} {:<15} {:<15} {:<10.2f} {:<10.2f}".format(record[0], record[1][0], record[1][1], record[2], record[3]))

    # Order by Last Name
    elif choice == "5":
        for i in range(len(records) - 1):
            for j in range(len(records) - i - 1):
                if records[j][1][1] > records[j + 1][1][1]:
                    records[j], records[j + 1] = records[j + 1], records[j]
        print("Records sorted by last name.")
    
    # Order by Grade
    elif choice == "6":
        for i in range(len(records) - 1):
            for j in range(len(records) - i - 1):
                grade1 = records[j][2] * 0.6 + records[j][3] * 0.4
                grade2 = records[j + 1][2] * 0.6 + records[j + 1][3] * 0.4
                if grade1 < grade2:
                    records[j], records[j + 1] = records[j + 1], records[j]
        print("Records sorted by grade.")
    
    # Show Student Record
    elif choice == "7":
        student_id = int(input("Enter Student ID: "))
        found = False
        for record in records:
            if record[0] == student_id:
                print("\nStudent Record:")
                print(f"ID: {record[0]}")
                print(f"First Name: {record[1][0]}")
                print(f"Last Name: {record[1][1]}")
                print(f"Class Standing: {record[2]:.2f}")
                print(f"Major Exam Grade: {record[3]:.2f}")
                found = True
                break
        if not found:
            print("Student not found.")

    # Add Record
    elif choice == "8":
        while True:
            student_id = input("Enter Student ID (6 digits): ")
            if student_id.isdigit() and len(student_id) == 6:
                student_id = int(student_id)
                break
            print("Invalid Student ID. Must be a 6-digit number.")
        
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        class_standing = float(input("Enter Class Standing: "))
        major_exam = float(input("Enter Major Exam Grade: "))
        records.append((student_id, (first_name, last_name), class_standing, major_exam))
        
        file = open(file_name, "w")
        for record in records:
            file.write(f"{record[0]},{record[1][0]},{record[1][1]},{record[2]},{record[3]}\n")
        file.close()
        
        print("Record added and saved.")
    
    # Edit Record
    elif choice == "9":
        student_id = int(input("Enter Student ID to edit: "))
        for i in range(len(records)):
            if records[i][0] == student_id:
                print("What would you like to edit?")
                print("1. First Name")
                print("2. Last Name")
                print("3. Class Standing")
                print("4. Major Exam Grade")
                edit_choice = input("Enter choice: ")
                
                if edit_choice == "1":
                    first_name = input("Enter New First Name: ")
                    records[i] = (records[i][0], (first_name, records[i][1][1]), records[i][2], records[i][3])
                elif edit_choice == "2":
                    last_name = input("Enter New Last Name: ")
                    records[i] = (records[i][0], (records[i][1][0], last_name), records[i][2], records[i][3])
                elif edit_choice == "3":
                    class_standing = float(input("Enter New Class Standing: "))
                    records[i] = (records[i][0], records[i][1], class_standing, records[i][3])
                elif edit_choice == "4":
                    major_exam = float(input("Enter New Major Exam Grade: "))
                    records[i] = (records[i][0], records[i][1], records[i][2], major_exam)
                else:
                    print("Invalid choice.")
                
                file = open(file_name, "w")
                for record in records:
                    file.write(f"{record[0]},{record[1][0]},{record[1][1]},{record[2]},{record[3]}\n")
                file.close()
                
                print("Record updated and saved.")
                break
        else:
            print("Student not found.")
    
    # Delete Record
    elif choice == "10":
        student_id = int(input("Enter Student ID to delete: "))
        records = [record for record in records if record[0] != student_id]
        
        file = open(file_name, "w")
        for record in records:
            file.write(f"{record[0]},{record[1][0]},{record[1][1]},{record[2]},{record[3]}\n")
        file.close()
        
        print("Record deleted and saved.")
    
    # Exit Program
    elif choice == "11":
        break
    
    else:
        print("Invalid choice.")
