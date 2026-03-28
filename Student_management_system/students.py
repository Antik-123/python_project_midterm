# students.py
import json
from rich.console import Console
from rich.table import Table

console = Console()

# ***************** Entity ************************
class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def update_marks(self, new_marks):
        self.marks = new_marks

# *********************** Storage *****************************
class Storage:
    FILE_NAME = "students.json"

    @staticmethod
    def save(students):
        data = [{"name": s.name, "roll": s.roll_number, "marks": s.marks} for s in students]
        with open(Storage.FILE_NAME, "w") as f:
            json.dump(data, f)

    @staticmethod
    def load():
        students = []
        try:
            with open(Storage.FILE_NAME, "r") as f:
                data = json.load(f)
                for s in data:
                    students.append(Student(s["name"], s["roll"], s["marks"]))
        except FileNotFoundError:
            pass
        return students

# ************************** Manager ***************************
class StudentManager:
    all_students = Storage.load()

    @classmethod
    def add_student(cls, name, roll, marks):
        student = Student(name, roll, marks)
        cls.all_students.append(student)
        Storage.save(cls.all_students)

    @classmethod
    def find_student(cls, keyword):
        """Exact match by roll number or full name"""
        keyword = keyword.strip().lower()
        for s in cls.all_students:
            if s.roll_number.lower() == keyword or s.name.lower() == keyword:
                return s
        return None

    @classmethod
    def update_student(cls, roll, marks):
        student = cls.find_student(roll)
        if student:
            student.update_marks(marks)
            Storage.save(cls.all_students)
            return True
        return False

    @classmethod
    def delete_student(cls, roll):
        student = cls.find_student(roll)
        if student:
            cls.all_students.remove(student)
            Storage.save(cls.all_students)
            return True
        return False

    @classmethod
    def sort_students(cls, key):
        key = key.strip().lower()
        if key == "roll":
            cls.all_students.sort(key=lambda s: s.roll_number)
            Storage.save(cls.all_students)
            return True
        elif key == "marks":
            cls.all_students.sort(key=lambda s: s.marks, reverse=True)
            Storage.save(cls.all_students)
            return True
        return False

    @classmethod
    def show_all(cls, students=None):
        if students is None:
            students = cls.all_students
        if not students:
            console.print("[red]No students found[/red]")
            return
        table = Table(title="Student Records")
        table.add_column("Roll Number", style="cyan")
        table.add_column("Name", style="magenta")
        table.add_column("Marks", justify="right", style="green")
        for s in students:
            table.add_row(s.roll_number, s.name, str(s.marks))
        console.print(table)