"""
database.py
役割: PostgreSQL への接続設定と Session の管理

アプリ制作②の database.py と同じ構造です。
環境変数 DATABASE_URL から接続先を読み込みます。
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# .env の DATABASE_URL を読み込む（変更不要）
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://todouser:todopass@db:5432/tododb"
)

# engine と SessionLocal は変更不要
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """
    FastAPIの Depends() で使うDBセッションのジェネレータ。

    TODO: 以下の手順で実装してください
      1. SessionLocal() でセッションを作成する
      2. try ブロックで yield db（リクエスト中はこのセッションを使う）
      3. finally ブロックで db.close()（必ずクローズする）

    ヒント:
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()
    """
    # TODO: get_db() を実装してください
    pass
