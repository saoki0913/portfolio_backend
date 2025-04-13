from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db, supabase
from app.schemas.hero import TimelineItem, TimelineItemResponse, HeroIntroduction, HeroIntroductionResponse

# prefixの設定
router = APIRouter(prefix="/hero", tags=["hero"])

@router.get("/introduction", response_model=List[HeroIntroduction])
def get_hero_introduction(db: Session = Depends(get_db)):
    try:
        # Supabaseから自己紹介テキストを取得
        response = supabase.table("hero_introduction").select("*").execute()
        
        if not response.data:
            # データがない場合はデフォルト値を返す
            return [{
                "id": "default",
                "content": "早稲田大学創造理工学研究科の修士1年生として、AIロボティクスの研究に従事。また、長期インターンでWebエンジニアとしてAIを活用したwebアプリケーション開発に努める。"
            }]
            
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/timeline", response_model=List[TimelineItem])
def get_timeline_items(db: Session = Depends(get_db)):
    try:
        # Supabaseからタイムラインアイテムを取得（並び順指定）
        response = supabase.table("timeline_items").select("*").order("sort_order").execute()
        
        if not response.data:
            # データがない場合はデフォルト値を返す
            return [
                {
                    "id": "default-1",
                    "period": "2018.4 - 2021.3",
                    "title": "早稲田高等学校",
                    "sort_order": 1
                },
                {
                    "id": "default-2",
                    "period": "2021.4 - 2024.3",
                    "title": "早稲田大学 創造理工学部 総合機械工学科",
                    "subtitle": "学士課程",
                    "sort_order": 2
                },
                {
                    "id": "default-3",
                    "period": "2024.10 - 現在",
                    "title": "株式会社インテリジェントフォース",
                    "subtitle": "AIソリューション事業部 - AIエンジニア",
                    "sort_order": 3
                },
                {
                    "id": "default-4",
                    "period": "2025.2 - 現在",
                    "title": "株式会社EQUES",
                    "subtitle": "製薬業界向けSaaS - バックエンドエンジニア",
                    "sort_order": 4
                },
                {
                    "id": "default-5",
                    "period": "2025.4 - 現在",
                    "title": "早稲田大学 創造理工学研究科 総合機械工学専攻",
                    "subtitle": "修士課程 - 菅野研究室 認知ロボティクス研究",
                    "sort_order": 5
                }
            ]
            
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 
