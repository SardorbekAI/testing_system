from fastapi import FastAPI
from routers import students, tests, results
from pydantic import BaseModel
from typing import List, Dict
from routers import *

app = FastAPI(title="Student Testing App", description="Talabalarning test natijalarini boshqarish uchun API")

# Routerlarni ilovaga qo'shamiz
app.include_router(students.router)
app.include_router(tests.router)
app.include_router(results.router)

@app.get("/")
def home():
    return {"message": "Welcome to Student Testing App"}