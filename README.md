# Portfolio API

FastAPIとSupabaseを使用したポートフォリオサイト用のバックエンドAPI

## 機能

- **Works API**: プロジェクト作品の情報を取得するAPI
- **Skills API**: スキル情報を取得するAPI
- **About API**: プロフィール情報を取得するAPI
- **Contact API**: 問い合わせフォームからのメッセージを受け取るAPI

## 環境構築

### 前提条件

- Python 3.10以上
- Supabaseアカウントとプロジェクト

### ローカル開発環境の構築

1. 仮想環境の作成と有効化

```bash
python -m venv venv
source venv/bin/activate  # Windowsの場合: venv\Scripts\activate
```

2. 依存パッケージのインストール

```bash
pip install -r requirements.txt
```

3. 環境変数ファイルの作成

```bash
# .envファイルを作成し、以下の変数を設定
# Supabase設定
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-supabase-api-key
DATABASE_URL=postgresql://postgres:your-password@db.your-project.supabase.co:5432/postgres

# APIの設定
API_PREFIX=/api
BACKEND_CORS_ORIGINS=["http://localhost:3000"]

# メール設定
EMAILS_ENABLED=False  # メール送信を有効にする場合はTrueに設定
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password
EMAIL_RECIPIENT=your-email@gmail.com
```

4. 開発サーバーの起動

```bash
python run.py
# または
uvicorn app.main:app --reload
```

5. APIドキュメントへのアクセス

ブラウザで以下のURLにアクセスすると、Swagger UIのAPIドキュメントが表示されます。
- http://localhost:8000/docs

## API仕様

### スキル API

- `GET /api/skills` - すべてのスキルとカテゴリを取得
- `GET /api/skills?category={category}` - 特定のカテゴリのスキルを取得
- `GET /api/skills/categories` - スキルカテゴリの一覧を取得

### プロジェクト作品 API

- `GET /api/works` - すべてのプロジェクト作品を取得
- `GET /api/works/{id}` - 特定のプロジェクト作品の詳細を取得

### プロフィール API

- `GET /api/about` - プロフィール情報を取得

### 問い合わせ API

- `POST /api/contact` - 問い合わせメッセージを送信

## デプロイ (Render)

1. GitHubリポジトリの作成とコードのプッシュ
2. Renderで新しいWebサービスを作成
   - リポジトリ連携
   - ビルドコマンド: `pip install -r requirements.txt`
   - 起動コマンド: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - 環境変数の設定（`.env`ファイルの内容）

## Supabase設定

Supabaseに以下のテーブルを作成する必要があります：

1. `skill_categories` - スキルカテゴリ
2. `skills` - スキル
3. `works` - プロジェクト作品
4. `screenshots` - スクリーンショット
5. `technologies` - 技術スタック
6. `work_technologies` - プロジェクトと技術スタックの関連付け
7. `abouts` - プロフィール情報
8. `educations` - 学歴情報
9. `experiences` - 職歴情報
10. `social_media` - SNS情報
11. `contact_messages` - 問い合わせメッセージ

詳細なスキーマはコードの`models`ディレクトリを参照してください。 
