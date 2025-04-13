from pydantic import BaseModel
from typing import List, Optional, Dict

class ScreenshotBase(BaseModel):
    url: str
    caption: Optional[str] = None

class ScreenshotCreate(ScreenshotBase):
    pass

class Screenshot(ScreenshotBase):
    id: int
    
    class Config:
        orm_mode = True

class WorkBase(BaseModel):
    title: str
    description: str
    thumbnail: str
    category: Optional[str] = None
    duration: Optional[str] = None
    role: Optional[str] = None
    learnings: Optional[str] = None

class WorkCreate(WorkBase):
    technologies: List[str]
    screenshots: List[ScreenshotCreate] = []
    github_url: Optional[str] = None
    demo_url: Optional[str] = None
    blog_url: Optional[str] = None

class WorkLinks(BaseModel):
    github: Optional[str] = None
    demo: Optional[str] = None
    blog: Optional[str] = None

class Work(WorkBase):
    id: str
    technologies: List[str]
    screenshots: List[Screenshot] = []
    links: Optional[WorkLinks] = None
    
    class Config:
        orm_mode = True

class WorkListResponse(BaseModel):
    works: List[Work] 
