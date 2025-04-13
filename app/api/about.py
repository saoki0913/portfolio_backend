from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import json

from app.database import get_db, supabase
from app.schemas.about import About

router = APIRouter(prefix="/about", tags=["about"])

@router.get("", response_model=About)
def get_about_info(db: Session = Depends(get_db)):
    try:
        # Supabaseからプロフィール情報を取得
        about_response = supabase.table("abouts").select("*").limit(1).single().execute()
        
        if not about_response.data:
            raise HTTPException(status_code=404, detail="プロフィール情報が見つかりません")
            
        about = about_response.data
        about_id = about["id"]
        
        # 教育情報を取得
        education_response = supabase.table("educations").select("*").eq("about_id", about_id).execute()
        about["education"] = education_response.data
        
        # 職歴情報を取得
        experience_response = supabase.table("experiences").select("*").eq("about_id", about_id).execute()
        experiences = experience_response.data
        
        # 実績を文字列からリストに変換
        for exp in experiences:
            if exp.get("achievements") and isinstance(exp["achievements"], str):
                try:
                    exp["achievements"] = json.loads(exp["achievements"])
                except:
                    exp["achievements"] = exp["achievements"].split(",")
        
        about["experience"] = experiences
        
        # SNS情報を取得
        social_media_response = supabase.table("social_media").select("*").eq("about_id", about_id).execute()
        about["social_media"] = social_media_response.data
        
        return about
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 
