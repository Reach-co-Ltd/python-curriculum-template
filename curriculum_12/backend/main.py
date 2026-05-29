# ============================================================
# ファイル: backend/main.py
# 役割: FastAPI アプリの起動・ルーティング・CORS 設定
# ============================================================
# 実装の順番:
#   手順1: lifespan（テーブル自動作成）を実装する
#   手順2: CORS 設定を追加する
#   手順3: GET /tasks を実装する
#   手順4: POST /tasks を実装する
#   手順5: PATCH /tasks/{id}/toggle を実装する
#   手順6: DELETE /tasks/{id} を実装する
#
# 1つ実装するたびに http://localhost:8000/docs で確認してください
# ============================================================

from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from .database import engine, get_db
from .models import Base
from .schemas import TaskCreate, TaskResponse
from . import task_manager


# 手順1: lifespan を実装する
# アプリ起動時に Base.metadata.create_all(bind=engine) を呼ぶことで
# テーブルが自動作成される。これがないとテーブルが存在せずエラーになる
@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(lifespan=lifespan)


# 手順2: CORS 設定を追加する
# フロントエンド（http://localhost:3000）からのリクエストを許可する
# これがないとブラウザがリクエストをブロックしてしまう
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


# 手順3: GET /tasks を実装する
# アプリ制作①の show_tasks() に対応するエンドポイント
@app.get("/tasks", response_model=list[TaskResponse])
def list_tasks(db: Session = Depends(get_db)):
    # TODO: task_manager.get_tasks(db) を呼んで返す
    pass


# 手順4: POST /tasks を実装する
# アプリ制作①の add_task() に対応するエンドポイント
# status_code=201 → 作成成功は 200 ではなく 201 を返す
@app.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task(task_in: TaskCreate, db: Session = Depends(get_db)):
    # TODO: task_manager.add_task(db, task_in) を呼んで返す
    pass


# 手順5: PATCH /tasks/{task_id}/toggle を実装する
# アプリ制作①の toggle_task() に対応するエンドポイント
@app.patch("/tasks/{task_id}/toggle", response_model=TaskResponse)
def toggle_task(task_id: int, db: Session = Depends(get_db)):
    # TODO: task_manager.toggle_task(db, task_id) を呼ぶ
    # task_manager が None を返した場合 = ID が存在しない → 404 を返す
    #
    # ヒント:
    #   db_task = task_manager.toggle_task(db, task_id)
    #   if db_task is None:
    #       raise HTTPException(status_code=404, detail=f"ID:{task_id} のタスクが見つかりません")
    #   return db_task
    pass


# 手順6: DELETE /tasks/{task_id} を実装する
# アプリ制作①の delete_task() に対応するエンドポイント
# status_code=204 → 削除成功はレスポンスボディなし
@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    # TODO: task_manager.delete_task(db, task_id) を呼ぶ
    # task_manager が None を返した場合 = ID が存在しない → 404 を返す
    pass
