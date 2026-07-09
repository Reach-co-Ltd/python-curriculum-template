# ============================================================
# ファイル: backend/database.py
# 役割: PostgreSQLへの接続設定
# アプリ制作①の file_handler.py に対応する層
# ============================================================
# 実装の順番:
#   手順1: import文を書く
#   手順2: DATABASE_URL を .env から読み込む
#   手順3: engine と SessionLocal を作成する
#   手順4: get_db() 関数を実装する
# ============================================================

import os

# TODO: sqlalchemy から create_engine をインポートする
# TODO: sqlalchemy.orm から sessionmaker をインポートする


# TODO: os.getenv() を使って DATABASE_URL を読み込む
# デフォルト値: "postgresql://todouser:todopass@db:5432/tododb"
# ※ ホスト名は "db"（docker-compose.yml のサービス名）。localhost ではない
DATABASE_URL = None  # ← ここを実装する


# TODO: create_engine() を使って engine を作成する
# engine = ...

# TODO: sessionmaker() を使って SessionLocal を作成する
# SessionLocal = ...


def get_db():
    # TODO: DBセッションを yield するジェネレータ関数を実装する
    #
    # 実装の流れ:
    #   1. db = SessionLocal() でセッションを作る
    #   2. try: の中で yield db する
    #   3. finally: の中で db.close() する
    #
    # なぜ finally を使うのか:
    #   エラーが起きてもセッションを確実にクローズするためです
    #   セッションが開きっぱなしになると DB の接続数が上限に達して止まります
    pass
