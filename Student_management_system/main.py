# ******************************main.py************************************************************
from students import StudentManager, console

class CLIController:
    @staticmethod
    def run():
        while True:
            console.print("\n[bold yellow]===== Student Management System =====[/bold yellow]")
            console.print("1. Add Student")
            console.print("2. Update Marks")
            console.print("3. Delete Student")
            console.print("4. Show All Students")
            console.print("5. Search Student")
            console.print("6. Sort Students")
            console.print("7. Exit")

            choice = input("Enter your option (1-7): ")

            if choice == '1':
                name = input("Enter student name: ")
                roll = input("Enter student roll number: ")
                marks = int(input("Enter marks: "))
                StudentManager.add_student(name, roll, marks)
                console.print(f"[green]Student {name} added successfully![/green]")

            elif choice == '2':
                roll = input("Enter student roll number to update: ")
                marks = int(input("Enter new marks: "))
                if StudentManager.update_student(roll, marks):
                    console.print("[green]Marks updated successfully![/green]")
                else:
                    console.print("[red]Student not found.[/red]")

            elif choice == '3':
                roll = input("Enter student roll number to delete: ")
                if StudentManager.delete_student(roll):
                    console.print("[green]Student deleted successfully![/green]")
                else:
                    console.print("[red]Student not found.[/red]")

            elif choice == '4':
                StudentManager.show_all()

            elif choice == '5':
                keyword = input("Enter exact name or roll number to search: ")
                student = StudentManager.find_student(keyword)
                if student:
                    StudentManager.show_all([student])
                else:
                    console.print("[red]No matching student found.[/red]")

            elif choice == '6':
                while True:
                    key = input("Sort by 'roll' or 'marks': ").strip().lower()
                    if StudentManager.sort_students(key):
                        console.print(f"[green]Students sorted by {key} successfully.[/green]")
                        StudentManager.show_all()
                        break
                    else:
                        console.print("[red]Invalid sort key. Enter 'roll' or 'marks'[/red]")

            elif choice == '7':
                console.print("[bold yellow]Goodbye![/bold yellow]")
                break

            else:
                console.print("[red]Invalid choice. Please try again.[/red]")

# ***********************Entry point******************************************
if __name__ == "__main__":
    CLIController.run()