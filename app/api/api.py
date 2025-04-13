from fastapi import APIRouter
from app.api.endpoints import works, skills, about, contact

api_router = APIRouter()

api_router.include_router(works.router, prefix="/works", tags=["works"])
api_router.include_router(skills.router, prefix="/skills", tags=["skills"])
api_router.include_router(about.router, prefix="/about", tags=["about"])
api_router.include_router(contact.router, prefix="/contact", tags=["contact"]) 
