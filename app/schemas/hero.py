from pydantic import BaseModel, Field
from typing import Optional, List


class HeroIntroduction(BaseModel):
    """自己紹介テキスト"""
    id: str
    content: str
    
    class Config:
        from_attributes = True


class HeroIntroductionResponse(BaseModel):
    """自己紹介テキストのレスポンス"""
    data: List[HeroIntroduction]


class TimelineItem(BaseModel):
    """経歴タイムラインの項目"""
    id: str
    period: str
    title: str
    subtitle: Optional[str] = None
    sort_order: int
    
    class Config:
        from_attributes = True


class TimelineItemResponse(BaseModel):
    """タイムラインアイテムのレスポンス"""
    data: List[TimelineItem] 
