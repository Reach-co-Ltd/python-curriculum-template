from sqlalchemy.orm import Session
from .models import Employee
from .auth import get_password_hash

INITIAL_EMPLOYEES = [
    {"name": "管理者",    "email": "admin@example.com",   "department": "システム部", "password": "admin1234", "is_admin": True},
    {"name": "田中 太郎", "email": "tanaka@example.com",  "department": "開発部",     "password": "user1234",  "is_admin": False},
    {"name": "佐藤 花子", "email": "sato@example.com",    "department": "営業部",     "password": "user1234",  "is_admin": False},
    {"name": "鈴木 次郎", "email": "suzuki@example.com",  "department": "開発部",     "password": "user1234",  "is_admin": False},
]


def seed_employees(db: Session) -> None:
    """起動時に初期アカウントを投入する（既存の場合はスキップ）"""
    for data in INITIAL_EMPLOYEES:
        exists = db.query(Employee).filter(Employee.email == data["email"]).first()
        if exists:
            continue
        emp = Employee(
            name=data["name"],
            email=data["email"],
            department=data["department"],
            hashed_password=get_password_hash(data["password"]),
            is_admin=data["is_admin"],
        )
        db.add(emp)
    db.commit()
