"""
main.py
役割: FastAPIアプリの起動・全エンドポイント・CORS設定

【実装の進め方】
03章（タスクAPI）: schemas.py・task_manager.py を実装してから
                   このファイルのタスク関連TODOを実装する
04章（認証・JWT）: auth.py を理解してから
                   ログインエンドポイントと Depends を追加する

【重要】
・Depends(get_current_user) は04章で追加します
・03章の時点ではエンドポイントは実装済み（認証なし状態）で動作確認できます

【システム全体の中でのこのファイルの位置づけ】
リクエストが最初に到達する「玄関」の役割。
main.py自身はDB操作もビジネスロジックも持たず、
「URLとHTTPメソッドを見て、対応するtask_managerの関数を呼び、
 戻り値をHTTPステータスコードに変換する」ことだけを担当する。
この「薄さ」を保つことが設計上の狙いで、
将来もし管理画面やバッチ処理など別の入口を追加しても、
task_manager.py以下のロジックはそのまま再利用できる。
"""

from contextlib import asynccontextmanager
from datetime import date

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .auth import (create_access_token, get_current_admin,
                   get_current_user, get_password_hash, verify_password)
from .database import SessionLocal, engine, get_db
from .models import Base, Employee
from .schemas import (DashboardRow, EmployeeCreate, EmployeePublic,
                      EmployeeResponse, EmployeeTaskSummary, EmployeeUpdate,
                      TaskCreate, TaskResponse, TaskUpdate, TokenResponse)
from . import task_manager
from .seed import seed_employees


@asynccontextmanager
async def lifespan(app: FastAPI):
    """起動時にテーブル自動作成・シードデータ投入（変更不要）"""
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        seed_employees(db)
    finally:
        db.close()
    yield


app = FastAPI(
    title="社内タスク管理システム API",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── ヘルスチェック（変更不要）──────────────────────────
@app.get("/health")
def health():
    return {"status": "ok"}


# ══════════════════════════════════════════════════════
# 04章（認証）で実装する
# ══════════════════════════════════════════════════════

@app.post("/auth/login", response_model=TokenResponse)
def login(form_data: OAuth2PasswordRequestForm = Depends(),
          db: Session = Depends(get_db)):
    """
    ログイン・JWTトークン発行。

    TODO（04章）: 以下の手順で実装してください
      1. form_data.username（メールアドレス）でDBを検索する
      2. ユーザーが存在しない or パスワードが違う → 401 を raise する
      3. create_access_token({"sub": user.email}) でトークンを生成する
      4. TokenResponse(access_token=token) を return する

    ヒント:
        user = db.query(Employee).filter(
            Employee.email == form_data.username
        ).first()
        if not user or not verify_password(form_data.password, user.hashed_password):
            raise HTTPException(status_code=401, detail="メールアドレスまたはパスワードが違います")
        token = create_access_token({"sub": user.email})
        return TokenResponse(access_token=token)
    """
    # TODO（04章）: ログイン処理を実装してください
    pass


@app.get("/auth/me", response_model=EmployeeResponse)
def get_me(current_user: Employee = Depends(get_current_user)):
    """ログイン中のユーザー情報を返す（Dependsの組み込みは04章で確認）"""
    return current_user


# ══════════════════════════════════════════════════════
# 03章（タスクAPI）で実装する
# ══════════════════════════════════════════════════════

@app.get("/tasks", response_model=list[TaskResponse])
def list_tasks(
    task_date:    date | None = None,
    done:         bool | None = None,
    db:           Session     = Depends(get_db),
    current_user: Employee    = Depends(get_current_user),
):
    """
    自分のタスク一覧を取得する。

    TODO（03章）: task_manager.get_tasks() を呼んで結果を return してください
    ヒント: return task_manager.get_tasks(db, current_user.id, task_date, done)
    """
    # TODO: ここに実装してください
    pass


@app.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task(
    task_in:      TaskCreate,
    db:           Session  = Depends(get_db),
    current_user: Employee = Depends(get_current_user),
):
    """
    タスクを追加する。

    TODO（03章）: task_manager.add_task() を呼んで結果を return してください
    ヒント: return task_manager.add_task(db, task_in, current_user.id)
    """
    # TODO: ここに実装してください
    pass


@app.patch("/tasks/{task_id}/toggle", response_model=TaskResponse)
def toggle_task(
    task_id:      int,
    db:           Session  = Depends(get_db),
    current_user: Employee = Depends(get_current_user),
):
    """
    完了・未完了を切り替える。

    TODO（03章）: 以下の手順で実装してください
      1. task_manager.toggle_task(db, task_id, current_user.id) を呼ぶ
      2. result が None なら 404 を raise する
      3. result が "forbidden" なら 403 を raise する
      4. result を return する
    """
    # TODO: ここに実装してください
    pass


@app.patch("/tasks/{task_id}", response_model=TaskResponse)
def update_task(
    task_id:      int,
    task_in:      TaskUpdate,
    db:           Session  = Depends(get_db),
    current_user: Employee = Depends(get_current_user),
):
    """
    タスクを更新する（タイトル・完了フラグ・実施日）。

    TODO（03章）: toggle_task エンドポイントと同じパターンで実装してください
    """
    # TODO: ここに実装してください
    pass


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(
    task_id:      int,
    db:           Session  = Depends(get_db),
    current_user: Employee = Depends(get_current_user),
):
    """
    タスクを削除する。

    TODO（03章）: toggle_task エンドポイントと同じパターンで実装してください
                 204 は status_code で指定済みなので return は不要
    """
    # TODO: ここに実装してください
    pass


# ── 以下は変更不要（ダッシュボード・社員管理）──────────

@app.get("/tasks/all/summary", response_model=list[EmployeeTaskSummary])
def all_summary(
    db:           Session  = Depends(get_db),
    current_user: Employee = Depends(get_current_admin),
):
    """全社員タスクサマリー（変更不要）"""
    return task_manager.get_all_summary(db)


@app.get("/tasks/all/dashboard", response_model=list[DashboardRow])
def dashboard(
    date_from:    date,
    date_to:      date,
    db:           Session  = Depends(get_db),
    current_user: Employee = Depends(get_current_user),
):
    """全社員ダッシュボード（変更不要）"""
    return task_manager.get_dashboard(db, date_from, date_to)


@app.get("/employees", response_model=list[EmployeePublic])
def list_employees(
    db:           Session  = Depends(get_db),
    current_user: Employee = Depends(get_current_user),
):
    """社員一覧（変更不要）"""
    return db.query(Employee).filter(Employee.is_active == True).all()


@app.post("/employees", response_model=EmployeeResponse, status_code=201)
def create_employee(
    emp_in:       EmployeeCreate,
    db:           Session  = Depends(get_db),
    current_user: Employee = Depends(get_current_admin),
):
    """社員追加（変更不要）"""
    if db.query(Employee).filter(Employee.email == emp_in.email).first():
        raise HTTPException(status_code=400, detail="このメールアドレスは既に登録されています")
    emp = Employee(
        name=emp_in.name, email=emp_in.email, department=emp_in.department,
        hashed_password=get_password_hash(emp_in.password), is_admin=emp_in.is_admin,
    )
    db.add(emp)
    db.commit()
    db.refresh(emp)
    return emp


@app.delete("/employees/{employee_id}", status_code=204)
def delete_employee(
    employee_id:  int,
    db:           Session  = Depends(get_db),
    current_user: Employee = Depends(get_current_admin),
):
    """社員論理削除（変更不要）"""
    emp = db.query(Employee).filter(Employee.id == employee_id).first()
    if emp is None:
        raise HTTPException(status_code=404, detail="社員が見つかりません")
    emp.is_active = False
    db.commit()


@app.patch("/employees/me", response_model=EmployeeResponse)
def update_profile(
    emp_in:       EmployeeUpdate,
    db:           Session  = Depends(get_db),
    current_user: Employee = Depends(get_current_user),
):
    """プロフィール編集（変更不要）"""
    if emp_in.name is not None:
        current_user.name = emp_in.name
    if emp_in.department is not None:
        current_user.department = emp_in.department
    db.commit()
    db.refresh(current_user)
    return current_user
