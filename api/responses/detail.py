from pydantic import BaseModel


class DetailMessage(BaseModel):
    message: str
