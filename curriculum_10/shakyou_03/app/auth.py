# 10章 03. 写経
# ファイル: app/auth.py
def validate_password(password):
    if len(password) < 8:
        return False
    if "admin" in password:
        return False
    return True
