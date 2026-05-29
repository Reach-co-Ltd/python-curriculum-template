"""
task_manager.py
役割: タスクのCRUDロジック

アプリ制作②の task_manager.py からの発展版です。
「自分のタスクだけ操作できる」という employee_id による管理が追加されています。

アプリ制作②との対応:
  add_task()    → POST   /tasks
  get_tasks()   → GET    /tasks  （今回は employee_id フィルター追加）
  toggle_task() → PATCH  /tasks/{id}/toggle （今回は所有権チェック追加）
  delete_task() → DELETE /tasks/{id}        （今回は所有権チェック追加）
"""

from collections import defaultdict
from datetime import date
from sqlalchemy.orm import Session
from . import models, schemas


def get_task(db: Session, task_id: int) -> models.Task | None:
    """IDでタスクを1件取得する（変更不要）"""
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def get_tasks(
    db:          Session,
    employee_id: int,
    task_date:   date | None = None,
    done:        bool | None = None,
) -> list[models.Task]:
    """
    自分のタスク一覧を取得する。

    TODO: 以下の手順で実装してください
      1. db.query(models.Task).filter(Task.employee_id == employee_id) で自分のタスクだけに絞る
      2. task_date が指定されていれば日付でさらに絞り込む
      3. done が指定されていれば完了状態で絞り込む
      4. .order_by(models.Task.id).all() で返す

    ヒント:
        q = db.query(models.Task).filter(
            models.Task.employee_id == employee_id
        )
        if task_date is not None:
            q = q.filter(models.Task.task_date == task_date)
        if done is not None:
            q = q.filter(models.Task.done == done)
        return q.order_by(models.Task.id).all()
    """
    # TODO: get_tasks() を実装してください
    pass


def add_task(
    db:          Session,
    task_in:     schemas.TaskCreate,
    employee_id: int,
) -> models.Task:
    """
    タスクを追加してDBに保存する。

    TODO: 以下の手順で実装してください
      1. models.Task(title=..., task_date=..., employee_id=...) でオブジェクト作成
      2. db.add(db_task)
      3. db.commit()
      4. db.refresh(db_task)  ← DBが付与したidを取得するために必要
      5. return db_task
    """
    # TODO: add_task() を実装してください
    pass


def toggle_task(
    db:          Session,
    task_id:     int,
    employee_id: int,
):
    """
    完了・未完了を切り替える。

    戻り値のパターン:
      None       → タスクが存在しない（→ 404）
      "forbidden" → 他人のタスク（→ 403）
      Task       → 成功（→ 200）

    TODO: 以下の手順で実装してください
      1. get_task(db, task_id) でタスクを取得する
      2. None なら None を return
      3. db_task.employee_id != employee_id なら "forbidden" を return
      4. db_task.done = not db_task.done で反転
      5. db.commit() → db.refresh(db_task) → return db_task

    ヒント: delete_task() と同じパターンです。先に delete_task() を実装すると参考になります。
    """
    # TODO: toggle_task() を実装してください
    pass


def update_task(
    db:          Session,
    task_id:     int,
    task_in:     schemas.TaskUpdate,
    employee_id: int,
):
    """
    タスクを更新する（タイトル・完了フラグ・実施日）。

    戻り値のパターン: None / "forbidden" / Task（toggle_task と同じ）

    TODO: 以下の手順で実装してください
      1. get_task で取得 → None / forbidden チェック
      2. task_in.title が None でなければ db_task.title を更新
      3. task_in.done が None でなければ db_task.done を更新
      4. task_in.task_date が None でなければ db_task.task_date を更新
      5. db.commit() → db.refresh(db_task) → return db_task
    """
    # TODO: update_task() を実装してください
    pass


def delete_task(
    db:          Session,
    task_id:     int,
    employee_id: int,
):
    """
    タスクを削除する。

    戻り値のパターン: None / "forbidden" / 削除したTask

    TODO: 以下の手順で実装してください
      1. get_task(db, task_id) でタスクを取得する
      2. None なら None を return
      3. db_task.employee_id != employee_id なら "forbidden" を return
      4. db.delete(db_task) でセッションから削除
      5. db.commit() で削除を確定
      6. return db_task（削除前の情報を返す）

    ヒント:
        db_task = get_task(db, task_id)
        if db_task is None:
            return None
        if db_task.employee_id != employee_id:
            return "forbidden"
        db.delete(db_task)
        db.commit()
        return db_task
    """
    # TODO: delete_task() を実装してください
    pass


# ── 以下は変更不要（ダッシュボード用）────────────────

def get_all_summary(db: Session) -> list[schemas.EmployeeTaskSummary]:
    """全社員のタスク件数サマリーを返す（変更不要）"""
    employees = (
        db.query(models.Employee).filter(models.Employee.is_active == True).all()
    )
    result = []
    for emp in employees:
        tasks = db.query(models.Task).filter(models.Task.employee_id == emp.id).all()
        done_count = sum(1 for t in tasks if t.done)
        result.append(
            schemas.EmployeeTaskSummary(
                employee_id=emp.id,
                name=emp.name,
                department=emp.department,
                total=len(tasks),
                done=done_count,
                undone=len(tasks) - done_count,
            )
        )
    return result


def get_dashboard(
    db: Session, date_from: date, date_to: date
) -> list[schemas.DashboardRow]:
    """全社員の日付別タスクを返す（変更不要）"""
    employees = (
        db.query(models.Employee)
        .filter(models.Employee.is_active == True)
        .order_by(models.Employee.id)
        .all()
    )
    tasks = (
        db.query(models.Task)
        .filter(
            models.Task.task_date >= date_from,
            models.Task.task_date <= date_to,
        )
        .all()
    )
    task_map: dict[int, dict[str, list[schemas.DashboardTask]]] = defaultdict(
        lambda: defaultdict(list)
    )
    for t in tasks:
        if t.task_date:
            task_map[t.employee_id][t.task_date.isoformat()].append(
                schemas.DashboardTask(title=t.title, done=t.done)
            )
    return [
        schemas.DashboardRow(
            employee_id=emp.id,
            name=emp.name,
            department=emp.department,
            tasks_by_date=dict(task_map[emp.id]),
        )
        for emp in employees
    ]
