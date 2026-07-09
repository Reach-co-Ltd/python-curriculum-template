# ============================================================
# conftest.py - テスト共通設定（変更不要）
# ============================================================
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.main import app
from backend.database import get_db
from backend.models import Base

# テスト用 DB は SQLite インメモリ
# → Docker（PostgreSQL）なしでテストできる
# → テストのたびに空の状態から始まる
TEST_DB_URL = "sqlite:///:memory:"
engine_test = create_engine(TEST_DB_URL, connect_args={"check_same_thread": False})
SessionTest  = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)


def override_get_db():
    db = SessionTest()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine_test)
    yield
    Base.metadata.drop_all(bind=engine_test)


@pytest.fixture
def client():
    return TestClient(app)
