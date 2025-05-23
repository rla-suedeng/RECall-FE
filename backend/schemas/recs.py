from pydantic import BaseModel
from datetime import date
from typing import Optional
from enum import Enum

class CategoryEnum(str, Enum):
    childhood = "childhood"
    family = "family"
    travel = "travel"
    special = "special"
    etc = "etc"


class RecBase(BaseModel):
    r_id:int
    file: str
    

class RecCreate(BaseModel):
    content:Optional[str] = None
    title:str
    file: str
    r_date: Optional[date] = None
    category: CategoryEnum

    model_config = {
        "from_attributes": True
    }
    

class RecDetailGet(RecBase):
    content:Optional[str] = None
    title:str
    r_date: Optional[date] = None
    category: CategoryEnum
    author_name : Optional[str] = None
    
    model_config = {
        "from_attributes": True
    }
    

class RecUpdate(BaseModel):
    title:Optional[str] = None
    content: Optional[str] = None
    file: Optional[str]= None
    r_date: Optional[date] = None
    category: Optional[CategoryEnum]= None






