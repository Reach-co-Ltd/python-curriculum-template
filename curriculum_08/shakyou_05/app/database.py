# DB操作をこのファイルにまとめます。
# SQLインジェクション対策として「パラメータバインディング」を必ず使います。

import sqlite3
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from security import get_password_hash, sanitize_input
from errors.exceptions import InvalidInputError

# DBファイルの保存場所を定数で定義します
DB_PATH = "secure_app.db"


def init_db():
    # DBとテーブルを初期化します。アプリ起動時に1回だけ呼びます。
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            hashed_password TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# ==================================================
# 対策3：SQLインジェクション対策（パラメータバインディング）
# ==================================================
# SQLインジェクションとは：
#   ユーザーの入力をそのままSQL文に埋め込むと、
#   攻撃者が「' OR '1'='1'--」のような文字列を入力することで
#   全ユーザーのデータを取得したりできてしまう攻撃です
#
# 対策：
#   SQL文の中に ? を書いておき、値は別のタプルで渡します
#   こうすることで、入力値は絶対にSQL命令として解釈されません

def create_user(username: str, plain_password: str):
    if not username or not plain_password:
        raise InvalidInputError("ユーザー名とパスワードは必須です")

    # パスワードはハッシュ化してから保存します（平文で保存しない）
    hashed_pw = get_password_hash(plain_password)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # ?がプレースホルダーです。値はタプルで別渡しにします。
    # これがSQLインジェクション対策の核心です。
    cursor.execute(
        "INSERT INTO users (username, hashed_password) VALUES (?, ?)",
        (username, hashed_pw)
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id


def find_user(username: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 危険な書き方（絶対にやってはいけない）：
    # sql = "SELECT * FROM users WHERE username='" + username + "'"
    # → 攻撃者が「' OR '1'='1'--」を入力すると全件取得されてしまう

    # 安全な書き方（パラメータバインディング）：
    # ?を使うことで、どんな文字列が来てもSQL命令として解釈されない
    cursor.execute(
        "SELECT id, username, hashed_password FROM users WHERE username = ?",
        (username,)
    )
    result = cursor.fetchone()
    conn.close()
    return result


def save_comment(raw_content: str):
    # コメントはXSS対策としてエスケープしてから保存します
    safe_content = sanitize_input(raw_content)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 保存もパラメータバインディングを使います
    cursor.execute(
        "INSERT INTO comments (content) VALUES (?)",
        (safe_content,)
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id


def get_all_comments():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, content FROM comments")
    results = cursor.fetchall()
    conn.close()
    return results
