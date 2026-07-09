# ============================================================
# test_tasks.py - タスク API のテスト
# ============================================================
# 実行方法:
#   docker compose exec backend pytest backend/tests/ -v
#
# テストの書き方:
#   1. client.post/get/patch/delete で API を叩く
#   2. assert res.status_code == 期待するステータスコード
#   3. assert res.json()["キー"] == 期待する値
# ============================================================


class TestCreateTask:

    def test_正常追加(self, client):
        # TODO: タイトルを指定して POST /tasks を叩き
        #       ステータスコード 201 が返ること
        #       レスポンスに id・title・done が含まれること を確認する
        pass

    def test_空文字は422(self, client):
        # TODO: title="" を送ると 422 が返ることを確認する
        pass

    def test_未認証は401(self, client):
        # ※ curriculum_12 では認証なしでOK（curriculum_13 で追加）
        # このテストはスキップしてよい
        pass


class TestGetTasks:

    def test_タスクなしで空配列(self, client):
        # TODO: GET /tasks を叩くと [] が返ることを確認する
        pass

    def test_追加後に一覧に含まれる(self, client):
        # TODO: タスクを追加してから GET /tasks を叩き
        #       追加したタスクが含まれることを確認する
        pass


class TestToggleTask:

    def test_完了切り替え(self, client):
        # TODO: タスクを追加 → PATCH /tasks/{id}/toggle → done が True になること
        #       もう一度 toggle → done が False に戻ること を確認する
        pass

    def test_存在しないIDは404(self, client):
        # TODO: PATCH /tasks/999/toggle を叩くと 404 が返ることを確認する
        pass


class TestDeleteTask:

    def test_正常削除(self, client):
        # TODO: タスクを追加 → DELETE /tasks/{id} → 204 が返ること
        #       その後 GET /tasks で一覧に含まれないことを確認する
        pass

    def test_存在しないIDは404(self, client):
        # TODO: DELETE /tasks/999 を叩くと 404 が返ることを確認する
        pass
