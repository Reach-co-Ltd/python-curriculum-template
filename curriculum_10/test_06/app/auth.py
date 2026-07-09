# 10章 06. 単元総合テスト - 確認テスト（問題文）
# ファイル: app/auth.py
# （前章までの validate_password 関数を再利用する想定）

def validate_password(password):
    if password is None:
        raise ValueError("パスワードが指定されていません")
    if len(password) < 8:
        return False
    if "admin" in password:
        return False
    return True
