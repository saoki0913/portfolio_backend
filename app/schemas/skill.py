from pydantic import BaseModel
from typing import List, Optional

class SkillBase(BaseModel):
    name: str
    level: int
    icon: Optional[str] = None
    description: Optional[str] = None

class SkillCreate(SkillBase):
    category: str

class Skill(SkillBase):
    id: int
    category: str
    
    class Config:
        orm_mode = True

class SkillCategoryBase(BaseModel):
    name: str

class SkillCategoryCreate(SkillCategoryBase):
    pass

class SkillCategory(SkillCategoryBase):
    id: int
    skills: List[Skill] = []
    
    class Config:
        orm_mode = True

class SkillListResponse(BaseModel):
    categories: List[SkillCategory] 
