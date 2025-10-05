import os

doc_path = os.path.expanduser("~/Documents/StudentRecords")

if not os.path.exists(doc_path):
    os.makedirs(doc_path)

def register_student():
    print("\n==== Register Student ====")
    student_no = input("Enter Student No.: ")
    last_name = input("Enter Last Name: ")
    first_name = input("Enter First Name: ")
    middle_initial = input("Enter Middle Initial: ")
    program = input("Enter Program: ")
    age = input("Enter Age: ")
    gender = input("Enter Gender: ")
    birthday = input("Enter Birthday (MM/DD/YYYY): ")
    contact_no = input("Enter Contact No.: ")

    data = [
        f"Student No.: {student_no}",
        f"Full Name: {last_name}, {first_name} {middle_initial}.",
        f"Program: {program}",
        f"Age: {age}",
        f"Gender: {gender}",
        f"Birthday: {birthday}",
        f"Contact No.: {contact_no}",
    ]

    file_path = os.path.join(doc_path, f"{student_no}.txt")

    with open(file_path, "w") as file:
        for line in data:
            file.write(line + "\n")

    print("\n Student record saved successfully!\n")


def open_student_record():
    print("\n==== Open Student Record ====")
    student_no = input("Enter Student No.: ")

    file_path = os.path.join(doc_path, f"{student_no}.txt")

    try:
        with open(file_path, "r") as file:
            print("\n--- Student Record ---")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("\nStudent record not found.\n")


def exit_program():
    print("\nExiting program. Thank you for using Student Records System!\n")


def main():
    while True:
        print("===== Student Records Menu =====")
        print("1. Register Student")
        print("2. Open Student Record")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register_student()
        elif choice == "2":
            open_student_record()
        elif choice == "3":
            exit_program()
            break
        else:
            print("\n Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()
