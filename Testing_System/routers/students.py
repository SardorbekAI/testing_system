from fastapi import APIRouter, HTTPException
from models import Student, ResponseMessage
from database import add_student, get_student, get_all_students, delete_student

router = APIRouter(prefix="/students", tags=["Students"])

@router.post("/", response_model=Student)
def create_student(student: Student):
    if student.id in get_all_students():
        raise HTTPException(status_code=400, detail="Student ID already exists")
    return add_student(student)

@router.get("/{student_id}/", response_model=Student)
def read_student(student_id: int):
    student = get_student(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.get("/", response_model=list[Student])
def read_all_students():
    return get_all_students()

@router.delete("/{student_id}/", response_model=ResponseMessage)
def remove_student(student_id: int):
    student = delete_student(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return ResponseMessage(message="Student deleted successfully")
