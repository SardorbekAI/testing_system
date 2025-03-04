from typing import Dict, List
from models import Student, Test, TestResult

# Ma’lumotlarni xotirada saqlash uchun lug‘atlar
students_db: Dict[int, Student] = {}
tests_db: Dict[int, Test] = {}
results_db: List[TestResult] = []

# Student qo‘shish
def add_student(student: Student):
    students_db[student.id] = student
    return student

# Studentni olish
def get_student(student_id: int):
    return students_db.get(student_id)

# Barcha studentlarni olish
def get_all_students():
    return list(students_db.values())

# Studentni o‘chirish
def delete_student(student_id: int):
    return students_db.pop(student_id, None)

# Test qo‘shish
def add_test(test: Test):
    tests_db[test.id] = test
    return test

# Testni olish
def get_test(test_id: int):
    return tests_db.get(test_id)

# Barcha testlarni olish
def get_all_tests():
    return list(tests_db.values())

# Test natijasini qo‘shish
def add_test_result(result: TestResult):
    results_db.append(result)
    student = students_db.get(result.student_id)
    if student:
        student.submitted_tests.append(result.test_id)
    return result

# Talabaning barcha natijalarini olish
def get_results_by_student(student_id: int):
    return [r for r in results_db if r.student_id == student_id]

# Test uchun barcha natijalarni olish
def get_results_by_test(test_id: int):
    return [r for r in results_db if r.test_id == test_id]

# Test bo‘yicha o‘rtacha ballni hisoblash
def get_test_average_score(test_id: int):
    test_results = get_results_by_test(test_id)
    if not test_results:
        return None
    return sum(r.score for r in test_results) / len(test_results)

# Test bo‘yicha eng yuqori ballni olish
def get_test_highest_score(test_id: int):
    test_results = get_results_by_test(test_id)
    if not test_results:
        return None
    return max(r.score for r in test_results)
