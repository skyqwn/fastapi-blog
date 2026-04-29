from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from pydantic.dataclasses import dataclass

class BlogInput(BaseModel):
    title: str = Field(..., min_length=2, max_length=2000)
    author: str = Field(..., max_length=100)
    content: str = Field(..., min_length=2, max_length=4000)
    image_loc: Optional[str] = Field(None, max_length=4000)

class Blog(BlogInput):
    id: int
    modified_dt: datetime

class BlogData(BaseModel):
    id: int
    title: str
    author_id: int
    author: str | None = None
    email: str | None = None
    content: str
    modified_dt: datetime
    image_loc: str | None = None