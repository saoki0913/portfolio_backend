import uvicorn
import os
from dotenv import load_dotenv

# 環境変数の読み込み
load_dotenv()

if __name__ == "__main__":
    # 開発サーバーの起動
    uvicorn.run(
        "app.main:app", 
        host="0.0.0.0", 
        port=int(os.getenv("PORT", 8000)), 
        reload=True
    ) 
