# ============================================================
# ファイル: backend/models.py
# 役割: データベースのテーブル定義
# アプリ制作①の辞書 {"id", "title", "done"} がそのままカラムになっている
# ============================================================
# 実装の順番:
#   手順1: import文を書く
#   手順2: Base クラスを定義する
#   手順3: Task クラスのカラムを定義する
# ============================================================

from datetime import datetime

# TODO: sqlalchemy から Boolean, DateTime, Integer, String, func をインポートする
# TODO: sqlalchemy.orm から DeclarativeBase, Mapped, mapped_column をインポートする


# TODO: DeclarativeBase を継承した Base クラスを定義する
# class Base(DeclarativeBase):
#     pass


# TODO: Task クラスを実装する
# アプリ制作①の辞書との対応:
#   {"id": 1}        → id カラム（Integer・主キー）
#   {"title": "..."}  → title カラム（String(255)・NOT NULL）
#   {"done": False}  → done カラム（Boolean・デフォルトFalse）
#   （新規追加）      → created_at カラム（DateTime・自動設定）
#
# class Task(Base):
#     __tablename__ = "tasks"
#
#     id:         Mapped[int]      = mapped_column(Integer, primary_key=True, index=True)
#     title:      Mapped[str]      = mapped_column(String(255), nullable=False)
#     done:       Mapped[bool]     = mapped_column(Boolean, default=False, nullable=False)
#     created_at: Mapped[datetime] = mapped_column(
#         DateTime(timezone=True), server_default=func.now(), nullable=False
#     )
