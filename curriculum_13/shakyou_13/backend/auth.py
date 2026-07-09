import os
from datetime import datetime, timedelta, timezone

import bcrypt
import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from .database import get_db
from .models import Employee

SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
ALGORITHM  = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_password_hash(password: str) -> str:
    """パスワードをbcryptでハッシュ化する"""
    pwd_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pwd_bytes, salt).decode("utf-8")


def verify_password(plain: str, hashed: str) -> bool:
    """パスワードを照合する"""
    return bcrypt.checkpw(
        plain.encode("utf-8"),
        hashed.encode("utf-8")
    )


def create_access_token(data: dict) -> str:
    """JWTトークンを生成する"""
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(
    token: str     = Depends(oauth2_scheme),
    db:    Session = Depends(get_db),
) -> Employee:
    """JWTを検証して現在のユーザーを返す"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="無効なトークンです")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="無効なトークンです")

    user = db.query(Employee).filter(Employee.email == email).first()
    if user is None or not user.is_active:
        raise HTTPException(status_code=401, detail="ユーザーが見つかりません")
    return user


def get_current_admin(
    current_user: Employee = Depends(get_current_user),
) -> Employee:
    """管理者専用エンドポイント用"""
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="管理者権限が必要です")
    return current_user
