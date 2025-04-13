import os
import json
from dotenv import load_dotenv
from supabase import create_client, Client

# 環境変数の読み込み
load_dotenv()

# Supabase接続
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

def create_tables():
    """Supabaseにテーブルを作成する"""
    
    print("Supabaseテーブル作成スクリプト")
    try:
        # スキルカテゴリの作成
        supabase.table("skill_categories").insert([
            {"name": "フロントエンド"},
            {"name": "バックエンド"},
            {"name": "デザイン"},
            {"name": "DevOps"},
            {"name": "その他"}
        ]).execute()
        print("スキルカテゴリを作成しました")
    except Exception as e:
        print(f"スキルカテゴリ作成エラー: {str(e)}")
    
    # サンプルスキル追加
    try:
        # フロントエンドカテゴリのIDを取得
        cat_response = supabase.table("skill_categories").select("id").eq("name", "フロントエンド").execute()
        if cat_response.data:
            frontend_cat_id = cat_response.data[0]["id"]
            
            # スキルの追加
            supabase.table("skills").insert([
                {"name": "React", "level": 85, "category_id": frontend_cat_id, "icon": "react.svg"},
                {"name": "TypeScript", "level": 80, "category_id": frontend_cat_id, "icon": "typescript.svg"},
                {"name": "Next.js", "level": 75, "category_id": frontend_cat_id, "icon": "nextjs.svg"}
            ]).execute()
            print("サンプルスキルを追加しました")
    except Exception as e:
        print(f"スキル追加エラー: {str(e)}")
    
    # サンプルプロフィール追加
    try:
        # プロフィール情報の追加
        about_response = supabase.table("abouts").insert({
            "name": "青木 駿介",
            "title": "フルスタック開発者",
            "summary": "Webアプリケーション開発に情熱を持つエンジニアです。",
            "profile_image": "/images/profile.jpg",
            "bio": "3年間のWeb開発経験を持つフルスタック開発者です。UI/UXデザインからバックエンド開発、インフラ構築まで幅広いスキルを持っています。"
        }).execute()
        
        if about_response.data:
            about_id = about_response.data[0]["id"]
            
            # 学歴情報の追加
            supabase.table("educations").insert({
                "institution": "早稲田大学",
                "degree": "学士",
                "field": "機械工学",
                "start_date": "2021-04-01",
                "end_date": "2025-03-31",
                "about_id": about_id
            }).execute()
            
            # 職歴情報の追加
            supabase.table("experiences").insert({
                "company": "株式会社インテリジェントフォース",
                "position": "AIエンジニア",
                "start_date": "2024-10-01",
                "description": "AI開発とバックエンド開発を担当",
                "achievements": json.dumps(["Azureを活用したRAGの開発", "スケジュール管理システムの開発"]),
                "about_id": about_id
            }).execute()
            
            # SNS情報の追加
            supabase.table("social_media").insert([
                {"platform": "GitHub", "url": "https://github.com/example", "about_id": about_id},
                {"platform": "Twitter", "url": "https://twitter.com/example", "about_id": about_id}
            ]).execute()
            
            print("サンプルプロフィールを追加しました")
    except Exception as e:
        print(f"プロフィール追加エラー: {str(e)}")
    
    # サンプルプロジェクト追加
    try:
        # プロジェクト情報の追加
        work_response = supabase.table("works").insert({
            "id": "sample-project",
            "title": "サンプルプロジェクト",
            "description": "これはサンプルプロジェクトの説明です。",
            "thumbnail": "/images/projects/sample.jpg",
            "category": "Webアプリ",
            "duration": "2022年4月 - 2022年6月",
            "role": "フロントエンド開発者",
            "github_url": "https://github.com/example/sample",
            "demo_url": "https://example.com"
        }).execute()
        
        if work_response.data:
            work_id = work_response.data[0]["id"]
            
            # スクリーンショットの追加
            supabase.table("screenshots").insert([
                {"url": "/images/projects/sample-1.jpg", "caption": "ホーム画面", "work_id": work_id},
                {"url": "/images/projects/sample-2.jpg", "caption": "機能紹介", "work_id": work_id}
            ]).execute()
            
            # 使用技術の追加
            supabase.table("work_technologies").insert([
                {"work_id": work_id, "technology": "React"},
                {"work_id": work_id, "technology": "TypeScript"},
                {"work_id": work_id, "technology": "Node.js"}
            ]).execute()
            
            print("サンプルプロジェクトを追加しました")
    except Exception as e:
        print(f"プロジェクト追加エラー: {str(e)}")

if __name__ == "__main__":
    create_tables() 
