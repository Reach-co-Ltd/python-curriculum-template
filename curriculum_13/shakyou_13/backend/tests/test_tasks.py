"""
test_tasks.py
タスクAPIのテスト（05章で実装）

テスト仕様書のタスク関連ケースを見ながら自分で設計・実装してください。

【実行方法】
docker compose exec backend pytest backend/tests/test_tasks.py -v

【テスト仕様書で確認すべき範囲（研修範囲）】
・POST /tasks  → 正常追加・空文字422・未認証401・他人タスク操作403
・GET  /tasks  → 0件・1件・複数件・自分のタスクのみ・未認証401
・PATCH toggle → 完了切り替え・他人403・存在しないID404
・DELETE       → 正常削除・他人403・存在しないID404

【全てのテストが「準備→実行→確認」の3ステップである理由】
実務のテストは必ずこの型で書く。
「準備」で必要なデータ（ユーザーやタスク）を用意し、
「実行」でAPIを実際に叩き、
「確認」でassertを使って期待通りかを検証する。
この型を崩さずに書くことで、後から他の人が読んでも
「何をテストしているか」が一目でわかるようになる。
"""

from .conftest import make_user, get_token, auth


class TestCreateTask:
    """POST /tasks のテスト"""

    def test_正常追加(self, client, db):
        """
        テスト仕様書ケース1: 正常追加

        TODO: 自分で実装してください
          - 確認すること: 201 / title / done=false / idが返ること
        """
        # TODO: ここにテストを実装してください
        pass

    def test_空文字は422(self, client, db):
        """
        テスト仕様書ケース2: 空文字
        TODO: 空文字のtitleを送ると422になることを確認してください
        """
        # TODO: ここにテストを実装してください
        pass

    def test_未認証は401(self, client):
        """
        認証テスト: Authorizationヘッダーなしは401
        TODO: トークンなしでPOSTすると401になることを確認してください
        """
        # TODO: ここにテストを実装してください
        pass


class TestGetTasks:
    """GET /tasks のテスト"""

    def test_自分のタスクのみ返る(self, client, db):
        """
        データ所有権テスト: 自分のタスクだけが返ること

        TODO: 以下の手順で実装してください
          1. 田中さんと佐藤さんの2人を作る
          2. 田中さんのトークンでタスクを追加する
          3. 佐藤さんのトークンでタスクを追加する
          4. 田中さんのトークンで GET /tasks を叩く
          5. 田中のタスクが含まれ、佐藤のタスクが含まれないことを確認する
        """
        # TODO: ここにテストを実装してください
        pass

    def test_0件のとき空配列(self, client, db):
        """
        TODO: タスクが0件のとき [] が返ることを確認してください
        """
        # TODO: ここにテストを実装してください
        pass

    def test_未認証は401(self, client):
        """TODO: トークンなしで GET /tasks を叩くと 401 になること"""
        # TODO: ここにテストを実装してください
        pass


class TestToggleTask:
    """PATCH /tasks/{id}/toggle のテスト"""

    def test_完了切り替え(self, client, db):
        """
        TODO: タスクを追加してtoggleすると done が True になることを確認してください
        """
        # TODO: ここにテストを実装してください
        pass

    def test_他人のタスクは403(self, client, db):
        """
        データ所有権テスト: 他人のタスクをtoggleすると403

        TODO: 以下の手順で実装してください
          1. 田中さんのタスクを作る
          2. 佐藤さんのトークンでtoggleを叩く
          3. 403 が返ることを確認する
        """
        # TODO: ここにテストを実装してください
        pass

    def test_存在しないIDは404(self, client, db):
        """TODO: 存在しないID(999など)をtoggleすると404になること"""
        # TODO: ここにテストを実装してください
        pass


class TestDeleteTask:
    """DELETE /tasks/{id} のテスト"""

    def test_正常削除(self, client, db):
        """TODO: タスクを削除して204が返り、一覧から消えることを確認してください"""
        # TODO: ここにテストを実装してください
        pass

    def test_他人のタスクは403(self, client, db):
        """TODO: 他人のタスクをdeleteすると403になること"""
        # TODO: ここにテストを実装してください
        pass

    def test_存在しないIDは404(self, client, db):
        """TODO: 存在しないIDをdeleteすると404になること"""
        # TODO: ここにテストを実装してください
        pass
