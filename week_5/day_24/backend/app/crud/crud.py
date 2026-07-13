from sqlalchemy.orm import Session

from app.models.models import Employee
from app.schemas import EmployeeCreate


def get_employees(db: Session):
    return db.query(Employee).order_by(Employee.emp_id).all()


def create_employee(db: Session, employee_data: EmployeeCreate):
    employee = Employee(
        emp_name=employee_data.emp_name,
        designation=employee_data.designation,
    )
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee
