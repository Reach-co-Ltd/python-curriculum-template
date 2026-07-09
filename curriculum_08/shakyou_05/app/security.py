# セキュリティに関係する処理をこのファイルにまとめます。
# 「パスワードのハッシュ化」と「XSS対策」の2つを担当します。

import html
import bcrypt
import sys
import os

# errorsフォルダのexceptions.pyから自分で作ったエラーをインポートします
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from errors.exceptions import WeakPasswordError, InvalidInputError


# ==================================================
# 対策1：パスワードのハッシュ化
# ==================================================
# 絶対にやってはいけないこと：
#   パスワードをそのままDBに保存すること
#   → DBが漏洩したとき、全ユーザーのパスワードが流出してしまう
#
# やるべきこと：
#   パスワードを「元に戻せない形」に変換（ハッシュ化）してから保存する
#   → 漏洩しても元のパスワードには戻せないので安全

def get_password_hash(plain_password: str) -> str:
    # まずパスワードが安全かどうかチェックします
    if len(plain_password) < 8:
        # 8文字未満の場合はWeakPasswordErrorを発生させます
        raise WeakPasswordError("パスワードは8文字以上にしてください")

    # encode("utf-8") で文字列をバイト列に変換します（bcryptに渡すために必要）
    pwd_bytes = plain_password.encode("utf-8")

    # gensalt() でランダムな「ソルト」を生成します
    # ソルトとは：同じパスワードでも毎回違うハッシュ値になるように混ぜる乱数のことです
    salt = bcrypt.gensalt()

    # hashpw() でパスワードとソルトを組み合わせてハッシュ値を作ります
    hashed = bcrypt.hashpw(pwd_bytes, salt)

    # decode("utf-8") でバイト列を文字列に戻してからreturnします
    return hashed.decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    # ログイン時に「入力されたパスワード」と「DBに保存されたハッシュ値」を照合します
    # checkpw() は内部でハッシュ化して比較するので、平文同士の比較はしません
    return bcrypt.checkpw(
        plain_password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )


# ==================================================
# 対策2：XSS対策（HTMLエスケープ）
# ==================================================
# XSSとは：
#   ユーザーが入力した文字列の中に <script> タグが含まれていると、
#   そのページを見た別のユーザーのブラウザでスクリプトが実行されてしまう攻撃です
#
# 対策：
#   保存する前にHTMLの特殊文字を無害な文字列に変換（エスケープ）します
#   <  →  &lt;
#   >  →  &gt;
#   "  →  &quot;

def sanitize_input(user_input: str) -> str:
    # 入力値が文字列かどうか確認します
    if not isinstance(user_input, str):
        raise InvalidInputError("文字列を入力してください")

    # strip() で前後の空白を除去します
    # html.escape() でHTMLの特殊文字を無害な文字列に変換します
    return html.escape(user_input.strip())
