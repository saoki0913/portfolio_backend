from typing import List, Optional, Dict
from pydantic import BaseModel, HttpUrl

class Link(BaseModel):
    github: Optional[str] = None
    demo: Optional[str] = None
    blog: Optional[str] = None

class Technology(BaseModel):
    name: str
    icon: Optional[str] = None

class Screenshot(BaseModel):
    url: str
    caption: Optional[str] = None

class Work(BaseModel):
    id: str
    title: str
    description: str
    thumbnail: str
    category: str
    featured: bool = False
    technologies: List[str]
    links: Optional[Link] = None
    screenshots: Optional[List[Screenshot]] = None
    duration: Optional[str] = None
    role: Optional[str] = None
    learnings: Optional[str] = None
    
    class Config:
        schema_extra = {
            "example": {
                "id": "portfolio",
                "title": "ポートフォリオサイト",
                "description": "React、Next.js、Tailwind CSSで開発した個人ポートフォリオサイト",
                "thumbnail": "/projects/portfolio.jpg",
                "category": "Web開発",
                "featured": True,
                "technologies": ["React", "Next.js", "TypeScript", "Tailwind CSS"],
                "links": {
                    "github": "https://github.com/username/portfolio",
                    "demo": "https://portfolio.example.com"
                },
                "screenshots": [
                    {"url": "/projects/portfolio-1.jpg", "caption": "ホームページ"}
                ],
                "duration": "2023年9月 - 現在",
                "role": "フルスタック開発者",
                "learnings": "モダンなWebフロントエンド技術とレスポンシブデザインについて学びました。"
            }
        }

class WorkList(BaseModel):
    works: List[Work] 
