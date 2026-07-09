# 10章 06. 単元総合テスト - 確認テスト（問題文）
# [①]〜[⑤]の（）に入るコードと、選択問題[Q1]〜[Q3]の答えを answers_06.txt に記入してください。
# ファイル名: tests/（）_auth.py ← [①] pytestが検出できる名前にすること

import （）  # [②] pytestをインポート
from app.auth import validate_password

# fixture: テスト前の前準備
@pytest.（）  # [③]
def sample_passwords():
    return {"strong": "my_secure_pass", "short": "abc"}

# parametrize: 複数パターンを1つのテスト関数で検証する
@pytest.mark.（）("test_pass,expected", [  # [④]
    ("my_secure_pass", True),   # 正常系: 十分に長い
    ("12345678", True),         # 境界値: ちょうど8文字
    ("short", False),           # 異常系: 7文字以下
    ("admin1234", False),       # 異常系: adminを含む
])
def test_password_strength(test_pass, expected):
    actual = validate_password(test_pass)
    （） actual == expected  # [⑤] assertで期待値と比較する

# 例外テスト
def test_invalid_raises():
    with pytest.raises(ValueError):  # このブロック内でValueErrorが出るはず
        validate_password(None)

# yieldを使ったfixture: 前準備と後片付けをセットにする
@pytest.fixture
def temp_file(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("テストデータ")
    yield test_file  # テスト関数にファイルパスを渡す
    # ここより下はテスト終了後に自動で実行される


# ===================================================
# 選択問題（answers_06.txt に記入）
# ===================================================
# [Q1] pytestが自動でテストファイルとして検出するファイル名は？
# A: test_*.py または *_test.py
# B: check_*.py または *_check.py

# [Q2] 複数パターンのテストを効率よく行うデコレータは？
# A: @pytest.fixture  B: @pytest.mark.parametrize  C: @pytest.mark.loop

# [Q3] fixtureでテストデータを渡しつつ後片付けも行うキーワードは？
# A: return  B: yield  C: pass
