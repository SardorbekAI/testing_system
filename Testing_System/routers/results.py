from fastapi import APIRouter, HTTPException
from models import TestResult, ResponseMessage
from database import (
    add_test_result, get_results_by_student, get_results_by_test,
    get_test_average_score, get_test_highest_score
)

router = APIRouter(prefix="/results", tags=["Results"])

@router.post("/", response_model=TestResult)
def submit_test_result(result: TestResult):
    return add_test_result(result)

@router.get("/student/{student_id}/", response_model=list[TestResult])
def get_student_results(student_id: int):
    results = get_results_by_student(student_id)
    if not results:
        raise HTTPException(status_code=404, detail="No results found for this student")
    return results

@router.get("/test/{test_id}/", response_model=list[TestResult])
def get_test_results(test_id: int):
    results = get_results_by_test(test_id)
    if not results:
        raise HTTPException(status_code=404, detail="No results found for this test")
    return results

@router.get("/test/{test_id}/average", response_model=float)
def get_test_average(test_id: int):
    avg_score = get_test_average_score(test_id)
    if avg_score is None:
        raise HTTPException(status_code=404, detail="No results available to calculate average")
    return avg_score

@router.get("/test/{test_id}/highest", response_model=int)
def get_test_highest(test_id: int):
    highest_score = get_test_highest_score(test_id)
    if highest_score is None:
        raise HTTPException(status_code=404, detail="No results available to determine highest score")
    return highest_score
