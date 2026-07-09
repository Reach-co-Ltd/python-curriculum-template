"""
test_auth.py
認証APIのテスト（05章で実装）

テスト仕様書の「POST /auth/login」セクションを見ながら実装してください。

【実行方法】
docker compose exec backend pytest backend/tests/test_auth.py -v

【conftest.py のヘルパー関数（使い方の復習）】
・make_user(db, name, email, password) → テスト用ユーザーを作る
・get_token(client, email, password)   → ログインしてトークンを取得する
・auth(token)                          → {"Authorization": "Bearer {token}"} を返す

【なぜ本物のDBではなくテスト専用のDBを使うのか】
conftest.pyがテストのたびにテーブルを作り直し、終わったら消している。
これにより「前のテストで作ったユーザーが残っていて、
今回のテストの結果が変わってしまう」という事故を防いでいる。
テストは何度実行しても同じ結果になることが重要。
"""

from .conftest import make_user, get_token, auth


class TestLogin:
    """POST /auth/login のテスト"""

    def test_正常ログインでトークンが返る(self, client, db):
        """
        【例】テスト仕様書ケース1: 正常ログイン

        この1つだけ例として実装してあります。
        残りのテストはこのパターンを参考に自分で書いてください。
        """
        # 準備: テスト用ユーザーを作る
        make_user(db, "田中", "tanaka@test.com", "pass1234")

        # 実行: ログインAPIを叩く
        res = client.post(
            "/auth/login",
            data={"username": "tanaka@test.com", "password": "pass1234"}
        )

        # 確認: 200 と access_token が返ること
        assert res.status_code == 200
        assert "access_token" in res.json()

    def test_パスワード間違いで401(self, client, db):
        """
        テスト仕様書ケース2: PW間違い
        TODO: 自分で実装してください
          - 準備: ユーザーを作る
          - 実行: 間違ったパスワードでログインする
          - 確認: 401 が返ること
        """
        # TODO: ここにテストを実装してください
        pass

    def test_未登録メールで401(self, client):
        """
        テスト仕様書ケース3: 未登録メール
        TODO: 自分で実装してください
          - 準備: ユーザーを作らない（未登録状態）
          - 実行: 存在しないメールアドレスでログインする
          - 確認: 401 が返ること
        """
        # TODO: ここにテストを実装してください
        pass

    def test_トークンなしでmeは401(self, client):
        """
        認証共通テスト: トークンなしは401
        TODO: 自分で実装してください
          - 実行: Authorizationヘッダーなしで GET /auth/me を叩く
          - 確認: 401 が返ること
        """
        # TODO: ここにテストを実装してください
        pass

    def test_ログイン後にme情報が取得できる(self, client, db):
        """
        正常系テスト: ログイン後にGET /auth/me で自分の情報が返る
        TODO: 自分で実装してください
          - 準備: ユーザーを作る
          - 実行: ログイン → トークンを使って GET /auth/me を叩く
          - 確認: 200 と自分のメールアドレスが返ること
        """
        # TODO: ここにテストを実装してください
        pass
