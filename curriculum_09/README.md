# curriculum_09 / PythonWeb開発（FastAPI）

| フォルダ / ファイル | 種別 | 対応章 |
|---|---|---|
| 01_web_api/shakyou_web_api.py | 写経 | 01. WebAPIとは・全体像 |
| 02_fastapi_setup/shakyou_fastapi_setup.py | 写経 | 02. FastAPIのセットアップ |
| 03_pydantic/shakyou_pydantic.py | 写経 | 03. Pydanticによるデータ検証 |
| 04_sqlalchemy/shakyou_sqlalchemy/ | 写経（4ファイル） | 04. SQLAlchemyとDB連携 |
| 05_routing/shakyou_routing.py | 写経 | 05. ルーティングと設計 |
| 06_jwt/shakyou_jwt.py | 写経 | 06. JWT認証 |
| 07_unit_test/test_unit.txt | 記述テスト | 07. 単元総合テスト |

## 実行方法（04_sqlalchemy以降）
```bash
cd curriculum_09/04_sqlalchemy/shakyou_sqlalchemy
pip install fastapi uvicorn sqlalchemy psycopg2-binary
uvicorn main:app --reload
# → http://localhost:8000/docs
```
