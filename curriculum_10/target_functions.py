# curriculum_10 / テスト対象の関数（変更不要）
# このファイルは変更しないでください
# 01〜04の写経問題でこのファイルの関数をテストします

def calculate_total_amount(price: int, quantity: int) -> int:
    """単価と数量から税込合計金額（10%）を返す"""
    if price < 0 or quantity < 0:
        raise ValueError("価格と数量は0以上でなければなりません")
    return int(price * quantity * 1.1)

def validate_password(password: str) -> bool:
    """パスワード強度を判定する（8文字以上かつadminを含まない）"""
    if len(password) < 8:
        return False
    if "admin" in password:
        return False
    return True

def contains_error_log(filepath: str) -> bool:
    """ファイルにERRORが含まれているか判定する"""
    with open(filepath, "r", encoding="utf-8") as f:
        return "ERROR" in f.read()
