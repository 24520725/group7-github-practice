# Updated by Thanh Canh
from student import StudentManager
from utils import clear_screen, press_enter_to_continue
def main():
    manager = StudentManager()
    while True:
        clear_screen()
        print("=== STUDENT MANAGEMENT ===")
        print("1. Add student")
        print("2. Display all students")
        print("3. Search student")
        print("4. Exit")
        choice = input("Choose: ")
        if choice == "1":
            name = input("Enter name: ")
            student_id = input("Enter student ID: ")
            score = float(input("Enter score: "))
            manager.add_student(name, student_id, score)
            print("Added!")
            press_enter_to_continue()
        elif choice == "2":
            students = manager.get_all()
            if not students:
                print("No students.")
            else:
                for s in students:
                    print(s)
            press_enter_to_continue()
        elif choice == "3":
            keyword = input("Enter name or ID to search: ")
            results = manager.search(keyword)
            if not results:
                print("Not found.")
            else:
                for s in results:
                    print(s)
            press_enter_to_continue()
        elif choice == "4":
            print("Goodbye!")
            break
if __name__ == "__main__":
    main()