from typing import List, Optional
from pydantic import BaseModel

class Skill(BaseModel):
    name: str
    level: int  # 1-5のスキルレベル
    category: str
    icon: Optional[str] = None
    description: Optional[str] = None
    
    class Config:
        schema_extra = {
            "example": {
                "name": "React",
                "level": 4,
                "category": "フロントエンド",
                "icon": "react",
                "description": "ReactとNext.jsを使用した複数のプロジェクト開発経験あり"
            }
        }

class SkillCategory(BaseModel):
    name: str
    skills: List[Skill]

class SkillList(BaseModel):
    categories: List[SkillCategory] 
