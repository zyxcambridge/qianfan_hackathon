# models.py
from pydantic import BaseModel

class UserAnswers(BaseModel):
    string: str