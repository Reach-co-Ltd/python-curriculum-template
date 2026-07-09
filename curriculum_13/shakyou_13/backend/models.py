"""
models.py
役割: データベースのテーブル定義（SQLAlchemy ORM）

ER図を見ながら Employee と Task の2つのクラスを実装してください。

【ER図との対応】
・ER図の employees テーブル → Employee クラス
・ER図の tasks テーブル     → Task クラス
・employees ||--o{ tasks   → ForeignKey + relationship で表現

【システム全体の中でのこのファイルの位置づけ】
このファイルは「DBに保存されるデータの形そのもの」を定義する、
システムの一番土台の部分。schemas.py（API入出力の形）や
task_manager.py（CRUD処理）は、全てこのmodels.pyのクラスを前提に作られる。
つまり、ここが間違っていると後の全工程に影響するため、
実装後は必ずSwaggerUIで動作確認してから次に進むこと。
"""

from datetime import date, datetime
from sqlalchemy import Boolean, Date, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Employee(Base):
    # TODO ①: テーブル名を "employees" に設定する
    # ヒント: __tablename__ = "employees"
    __tablename__ = "employees"

    # TODO ②: ER図を見て以下のカラムを定義する
    # ・id          → Integer / PK / index=True
    # ・name        → String(100) / nullable=False
    # ・email       → String(255) / nullable=False / unique=True
    # ・department  → String(100) / nullable=True（NULL可）
    # ・hashed_password → String(255) / nullable=False
    # ・is_admin    → Boolean / default=False / nullable=False
    # ・is_active   → Boolean / default=True  / nullable=False
    # ・created_at  → DateTime(timezone=True) / server_default=func.now()
    #
    # 書き方の例:
    # id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    pass

    # TODO ③: Task との relationship を定義する（実装後に追加）
    # ヒント: tasks: Mapped[list["Task"]] = relationship("Task", back_populates="employee")
    pass


class Task(Base):
    # TODO ④: テーブル名を "tasks" に設定する
    __tablename__ = "tasks"

    # TODO ⑤: ER図を見て以下のカラムを定義する
    # ・id          → Integer / PK / index=True
    # ・title       → String(255) / nullable=False
    # ・done        → Boolean / default=False / nullable=False
    # ・task_date   → Date / nullable=True（NULL可・IMP-001で追加）
    # ・employee_id → Integer / ForeignKey("employees.id") / nullable=False
    # ・created_at  → DateTime(timezone=True) / server_default=func.now()
    pass

    # TODO ⑥: Employee との relationship を定義する（実装後に追加）
    # ヒント: employee: Mapped["Employee"] = relationship("Employee", back_populates="tasks")
    pass
