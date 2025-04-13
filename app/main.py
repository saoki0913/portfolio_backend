from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api import skills, works, about, contact, hero


app = FastAPI(
    title="Portfolio API",
    description="ポートフォリオサイト用のRESTful API",
    version="1.0.0"
)

# CORSミドルウェアの設定
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# ルートAPIエンドポイント
@app.get("/")
def read_root():
    return {"message": "Welcome to Portfolio API"}

# API ルーターの登録
app.include_router(skills.router, prefix=settings.API_PREFIX)
app.include_router(works.router, prefix=settings.API_PREFIX)
app.include_router(about.router, prefix=settings.API_PREFIX)
app.include_router(contact.router, prefix=settings.API_PREFIX)
app.include_router(hero.router, prefix=settings.API_PREFIX) 
