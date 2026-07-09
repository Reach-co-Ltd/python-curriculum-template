"""
schemas.py
役割: APIの入出力データ形式の定義（Pydantic）

リクエストボディのバリデーションと、レスポンスの形式を定義します。
機能設計書のAPI仕様（リクエスト・レスポンスの形）を見ながら実装してください。

【システム全体の中でのこのファイルの位置づけ】
models.py が「DBの中の形」なのに対し、schemas.py は「APIの外から見た形」。
この2つは似ているが役割が違う。例えばhashed_passwordはDBには保存するが、
APIのレスポンスには絶対に含めてはいけない（パスワードの漏洩になるため）。
このように「DBにある情報」と「外部に見せてよい情報」を意図的に分けるのが
schemas.pyの一番の存在意義。
"""

from datetime import date, datetime
from pydantic import BaseModel, Field


# ── タスク ──────────────────────────────────────────────

class TaskCreate(BaseModel):
    """POST /tasks のリクエストボディ"""
    # TODO: 機能設計書を見てフィールドを定義してください
    # ・title    → str / 必須 / 1文字以上255文字以下
    # ・task_date → date | None / 任意（デフォルトNone）
    #
    # ヒント: title: str = Field(..., min_length=1, max_length=255)
    pass


class TaskUpdate(BaseModel):
    """PATCH /tasks/{id} のリクエストボディ（部分更新）"""
    # TODO: 以下のフィールドを定義してください（全て任意項目）
    # ・title     → str | None / 1文字以上255文字以下
    # ・done      → bool | None
    # ・task_date → date | None
    pass


class TaskResponse(BaseModel):
    """タスクのレスポンス形式"""
    # TODO: APIが返すフィールドを定義してください
    # id / title / done / task_date / employee_id / created_at
    pass

    # SQLAlchemyモデルをPydanticに変換するための設定（変更不要）
    model_config = {"from_attributes": True}


# ── 認証 ──────────────────────────────────────────────

class TokenResponse(BaseModel):
    """ログインのレスポンス形式（変更不要）"""
    access_token: str
    token_type: str = "bearer"


# ── 社員（変更不要・auth.pyで使用）──────────────────

class EmployeeCreate(BaseModel):
    name:       str        = Field(..., min_length=1, max_length=100)
    email:      str        = Field(..., min_length=1, max_length=255)
    department: str | None = None
    password:   str        = Field(..., min_length=1)
    is_admin:   bool       = False


class EmployeePublic(BaseModel):
    id:         int
    name:       str
    department: str | None
    model_config = {"from_attributes": True}


class EmployeeResponse(BaseModel):
    id:         int
    name:       str
    email:      str
    department: str | None
    is_admin:   bool
    is_active:  bool
    created_at: datetime
    model_config = {"from_attributes": True}


class EmployeeUpdate(BaseModel):
    name:       str | None = Field(None, min_length=1, max_length=100)
    department: str | None = None


# ── ダッシュボード（変更不要）────────────────────────

class DashboardTask(BaseModel):
    title: str
    done:  bool


class DashboardRow(BaseModel):
    employee_id:   int
    name:          str
    department:    str | None
    tasks_by_date: dict[str, list[DashboardTask]]
    model_config   = {"from_attributes": True}


class EmployeeTaskSummary(BaseModel):
    employee_id: int
    name:        str
    department:  str | None
    total:       int
    done:        int
    undone:      int
    model_config = {"from_attributes": True}
