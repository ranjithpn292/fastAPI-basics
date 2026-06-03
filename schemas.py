from pydantic import BaseModel
from typing import Optional


class Employee(BaseModel):
    name: str
    role: str
    salary: int


class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = None
    salary: Optional[int] = None