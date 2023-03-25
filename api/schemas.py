from pydantic import BaseModel


class APIRequest(BaseModel):
    data: str
