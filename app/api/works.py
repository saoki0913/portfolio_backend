from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db, supabase
from app.schemas.work import Work, WorkListResponse

# prefixが正しく設定されているか確認
router = APIRouter(prefix="/works", tags=["works"])

@router.get("", response_model=WorkListResponse)
def get_all_works(db: Session = Depends(get_db)):
    try:
        # Supabaseからプロジェクト一覧を取得
        works_response = supabase.table("works").select("*").execute()
        works = works_response.data
        
        # 各プロジェクトの詳細情報を取得
        for work in works:
            # 技術スタックを取得
            techs_response = supabase.table("work_technologies").select("technology").eq("work_id", work["id"]).execute()
            work["technologies"] = [tech["technology"] for tech in techs_response.data]
            
            # スクリーンショットを取得
            screenshots_response = supabase.table("screenshots").select("*").eq("work_id", work["id"]).execute()
            work["screenshots"] = screenshots_response.data
            
            # リンク情報を整形
            work["links"] = {
                "github": work.get("github_url"),
                "demo": work.get("demo_url"),
                "blog": work.get("blog_url")
            }
        
        return {"works": works}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{work_id}", response_model=Work)
def get_work_by_id(work_id: str, db: Session = Depends(get_db)):
    try:
        # Supabaseから特定のプロジェクトを取得
        work_response = supabase.table("works").select("*").eq("id", work_id).single().execute()
        
        if not work_response.data:
            raise HTTPException(status_code=404, detail="作品が見つかりません")
            
        work = work_response.data
        
        # 技術スタックを取得
        techs_response = supabase.table("work_technologies").select("technology").eq("work_id", work_id).execute()
        work["technologies"] = [tech["technology"] for tech in techs_response.data]
        
        # スクリーンショットを取得
        screenshots_response = supabase.table("screenshots").select("*").eq("work_id", work_id).execute()
        work["screenshots"] = screenshots_response.data
        
        # リンク情報を整形
        work["links"] = {
            "github": work.get("github_url"),
            "demo": work.get("demo_url"),
            "blog": work.get("blog_url")
        }
        
        return work
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 
