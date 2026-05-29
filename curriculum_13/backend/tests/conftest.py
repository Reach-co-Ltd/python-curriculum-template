import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.main import app
from backend.database import get_db
from backend.models import Base
from backend.auth import get_password_hash

TEST_DB_URL = "sqlite:///:memory:"
engine = create_engine(TEST_DB_URL, connect_args={"check_same_thread": False})
TestingSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def db():
    session = TestingSession()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def client():
    def override():
        s = TestingSession()
        try:
            yield s
        finally:
            s.close()
    app.dependency_overrides[get_db] = override
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()


def make_user(db, name, email, password, is_admin=False):
    from backend.models import Employee
    emp = Employee(
        name=name, email=email, department="開発部",
        hashed_password=get_password_hash(password), is_admin=is_admin,
    )
    db.add(emp)
    db.commit()
    db.refresh(emp)
    return emp


def get_token(client, email, password):
    res = client.post("/auth/login", data={"username": email, "password": password})
    return res.json()["access_token"]


def auth(token):
    return {"Authorization": f"Bearer {token}"}
