import json
import os
from dataclasses import dataclass, field
from typing import List

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
STUDENTS_FILE = os.path.join(DATA_DIR, 'students.json')

@dataclass
class Student:
    id: str
    name: str
    major: str
    enrolled_courses: List[str] = field(default_factory=list)
    completed_courses: List[str] = field(default_factory=list)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'major': self.major,
            'enrolled_courses': self.enrolled_courses,
            'completed_courses': self.completed_courses,
        }

    @staticmethod
    def from_json(data: dict) -> 'Student':
        return Student(
            id=data.get('id', ''),
            name=data.get('name', ''),
            major=data.get('major', 'Undeclared'),
            enrolled_courses=data.get('enrolled_courses', data.get('enrolledCourses', [])) or [],
            completed_courses=data.get('completed_courses', data.get('completedCourses', [])) or [],
        )


def load_students():
    if not os.path.exists(STUDENTS_FILE):
        return []
    with open(STUDENTS_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return [Student.from_json(item) for item in data]


def save_students(students):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(STUDENTS_FILE, 'w', encoding='utf-8') as f:
        json.dump([s.to_json() for s in students], f, indent=2)


def create_student_profile():
    print('--- Create New Student Profile ---')
    student_id = input('Student ID: ').strip()
    if not student_id:
        print('[!] Student ID cannot be empty.')
        return

    students = load_students()
    if any(s.id == student_id for s in students):
        print('[!] Student ID already exists.')
        return

    name = input('Full Name : ').strip()
    if not name:
        print('[!] Name cannot be empty.')
        return

    major = input('Major     : ').strip() or 'Undeclared'

    student = Student(student_id, name, major)
    students.append(student)
    save_students(students)

    print('[✓] New student profile created:')
    print(f'  {student}')


if __name__ == '__main__':
    create_student_profile()
