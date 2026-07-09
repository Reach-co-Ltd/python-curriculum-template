# ============================================================
# ファイル: backend/schemas.py
# 役割: リクエスト・レスポンスの型定義（Pydantic）
# ============================================================
# 実装の順番:
#   手順1: TaskCreate を実装する（リクエストで受け取る形）
#   手順2: TaskResponse を実装する（APIが返す形）
# ============================================================

from datetime import datetime

# TODO: pydantic から BaseModel, Field をインポートする
# TODO: pydantic から field_validator もインポートする（スペースのみを弾く場合）


# TODO: TaskCreate を実装する
# 役割: POST /tasks のリクエストボディの型定義
# アプリ制作①の「if title.strip() == '': return」に相当する処理を
# Pydantic の Field(min_length=1) が自動でやってくれる
#
# class TaskCreate(BaseModel):
#     title: str = Field(..., min_length=1, max_length=255)
#     # Field(...) の「...」は「必須」を意味する
#     # min_length=1 → 空文字を送ると 422 エラーが自動で返る


# TODO: TaskResponse を実装する
# 役割: API が返すタスクデータの型定義
# model_config = {"from_attributes": True} がないと
# SQLAlchemy のオブジェクトを Pydantic に変換できない
#
# class TaskResponse(BaseModel):
#     id:         int
#     title:      str
#     done:       bool
#     created_at: datetime
#     model_config = {"from_attributes": True}
