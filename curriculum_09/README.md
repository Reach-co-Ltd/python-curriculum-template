# curriculum_09 / PythonWeb開発（FastAPI）

## 提出ファイル構成

```
curriculum_09/
├── shakyou_01/              ← 01. WebAPIとは・基本API
│   └── shakyou_01.py
├── shakyou_02/              ← 02. パスパラメータ・クエリパラメータ
│   └── shakyou_01.py
├── shakyou_03/              ← 03. Pydanticによるデータ検証
│   └── shakyou_01.py
├── shakyou_04/              ← 04. SQLAlchemyとDB連携
│   └── sqlalchemy_app/
│       ├── main.py
│       ├── models.py
│       ├── database.py
│       └── schemas.py
├── shakyou_05/              ← 05. ルーティングと設計
│   └── fastapi_app/
│       ├── main.py
│       └── routers/
│           └── tasks.py
├── shakyou_06/              ← 06. JWT認証
│   └── jwt_app/
│       └── shakyou_01.py
└── test_07/                 ← 07. 単元総合テスト（記述）
    └── test_unit.txt
```

## 実行方法
```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-jose[cryptography] passlib[bcrypt]

# 04章以降
cd curriculum_09/shakyou_04/sqlalchemy_app
uvicorn main:app --reload
```
