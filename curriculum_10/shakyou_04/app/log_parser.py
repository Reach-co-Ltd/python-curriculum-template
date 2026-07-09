# 10章 04. 写経
# ファイル: app/log_parser.py
def contains_error_log(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    if "ERROR" in content:
        return True
    return False
