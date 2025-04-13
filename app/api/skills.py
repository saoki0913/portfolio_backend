from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db, supabase
from app.schemas.skill import SkillCategory, SkillListResponse

router = APIRouter(prefix="/skills", tags=["skills"])

@router.get("", response_model=SkillListResponse)
def get_all_skills(category: str = None, db: Session = Depends(get_db)):
    try:
        # Supabaseからデータを取得
        query = supabase.table("skill_categories").select("*")
        if category:
            query = query.eq("name", category)
        
        response = query.execute()
        categories = response.data
        
        # 各カテゴリのスキルを取得
        for cat in categories:
            skills_response = supabase.table("skills").select("*").eq("category_id", cat["id"]).execute()
            cat["skills"] = skills_response.data
        
        return {"categories": categories}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/categories", response_model=List[str])
def get_skill_categories(db: Session = Depends(get_db)):
    try:
        response = supabase.table("skill_categories").select("name").execute()
        return [cat["name"] for cat in response.data]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 
