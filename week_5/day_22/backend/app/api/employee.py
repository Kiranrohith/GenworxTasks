from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.crud import create_employee, get_employees
from app.database import get_db
from app.schemas import EmployeeCreate, EmployeeResponse

router = APIRouter(prefix="/employees", tags=["employees"])


@router.get("", response_model=list[EmployeeResponse])
def read_employees(db: Session = Depends(get_db)):
    return get_employees(db)


@router.post("", response_model=EmployeeResponse, status_code=status.HTTP_201_CREATED)
def create_employee_record(employee: EmployeeCreate, db: Session = Depends(get_db)):
    return create_employee(db, employee)
