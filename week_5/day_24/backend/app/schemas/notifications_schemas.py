from pydantic import BaseModel, ConfigDict, Field
import datetime

class notification_create(BaseModel):
    title: str = Field(min_length=1)
    server_message: str = Field(min_length=1)
    not_type: str = Field(min_length=1)


class notification_response(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    not_id: int
    title: str
    server_message: str
    not_type: str
    created_at: datetime.datetime