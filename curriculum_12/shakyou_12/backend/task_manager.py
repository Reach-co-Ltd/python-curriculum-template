# ============================================================
# ファイル: backend/task_manager.py
# 役割: タスクの CRUD ロジック
# アプリ制作①の task_manager.py を FastAPI + SQLAlchemy 版に発展させたもの
# ============================================================
# アプリ制作①との対応:
#   show_tasks()  → get_tasks()   （GET /tasks）
#   add_task()    → add_task()    （POST /tasks）
#   toggle_task() → toggle_task() （PATCH /tasks/{id}/toggle）
#   delete_task() → delete_task() （DELETE /tasks/{id}）
# ============================================================

from sqlalchemy.orm import Session
from . import models, schemas


def get_tasks(db: Session) -> list[models.Task]:
    # TODO: Task テーブルの全件を id 順で取得して返す
    #
    # ヒント:
    #   db.query(models.Task).order_by(models.Task.id).all()
    pass


def add_task(db: Session, task_in: schemas.TaskCreate) -> models.Task:
    # TODO: タスクを DB に追加して返す
    #
    # 実装の流れ:
    #   1. db_task = models.Task(title=task_in.title) でオブジェクトを作る
    #   2. db.add(db_task) でセッションに追加する
    #   3. db.commit() で DB に保存する
    #   4. db.refresh(db_task) で DB が付与した id を取得する
    #      ※ これを忘れると id が None のまま返ってくる
    #   5. return db_task
    pass


def toggle_task(db: Session, task_id: int) -> models.Task | None:
    # TODO: 指定 ID のタスクの done を反転させて返す
    #       ID が存在しない場合は None を返す（main.py で 404 にする）
    #
    # ヒント:
    #   db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    #   if db_task is None:
    #       return None
    #   db_task.done = not db_task.done  ← アプリ制作①と全く同じ反転処理
    #   db.commit()
    #   db.refresh(db_task)
    #   return db_task
    pass


def delete_task(db: Session, task_id: int) -> models.Task | None:
    # TODO: 指定 ID のタスクを削除して返す
    #       ID が存在しない場合は None を返す（main.py で 404 にする）
    #
    # ヒント:
    #   db.delete(db_task) で削除できる
    #   toggle_task() と同じパターンで実装できる
    pass
