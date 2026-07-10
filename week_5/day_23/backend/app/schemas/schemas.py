from datetime import datetime

from pydantic import BaseModel, ConfigDict


class EmployeeCreate(BaseModel):
    emp_name: str
    designation: str | None = None


class EmployeeResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    emp_id: int
    emp_name: str
    designation: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
