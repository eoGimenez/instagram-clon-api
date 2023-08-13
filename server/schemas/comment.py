from pydantic import BaseModel
from datetime import datetime
from typing import List
from schemas.response import ResponseDisplay

class CommentBase(BaseModel):
    username: str
    text: str
    post_id: int

class CommentDisplay(BaseModel):
    id: int
    text: str
    username: str
    responses: List[ResponseDisplay]
    timestamp: datetime
    class Config():
        from_attributes = True