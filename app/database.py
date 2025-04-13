from supabase import create_client, Client
from app.core.config import settings

# Supabaseクライアント - REST APIを通じてアクセス
supabase: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

# 互換性のためのダミーDB接続セッション
def get_db():
    # DBは使用せず、Supabaseクライアントを直接使うため
    # ここではダミーセッションを提供
    class DummyDB:
        def close(self):
            pass
    
    db = DummyDB()
    try:
        yield db
    finally:
        pass  # クローズは不要 
