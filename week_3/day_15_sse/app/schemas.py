from pydantic import BaseModel, Field
import datetime

class NotifyRequest(BaseModel):
    message: str = Field(min_length=1, max_length=100)

class NotifyResponse(BaseModel):
    id: int
    message: str
    created_at: datetime.datetime