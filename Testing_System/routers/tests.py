from fastapi import APIRouter, HTTPException
from models import Test, ResponseMessage
from database import add_test, get_test, get_all_tests

router = APIRouter(prefix="/tests", tags=["Tests"])

@router.post("/", response_model=Test)
def create_test(test: Test):
    if test.id in get_all_tests():
        raise HTTPException(status_code=400, detail="Test ID already exists")
    return add_test(test)

@router.get("/{test_id}/", response_model=Test)
def read_test(test_id: int):
    test = get_test(test_id)
    if not test:
        raise HTTPException(status_code=404, detail="Test not found")
    return test

@router.get("/", response_model=list[Test])
def read_all_tests():
    return get_all_tests()
