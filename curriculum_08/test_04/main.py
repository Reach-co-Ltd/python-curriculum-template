# 08章 04. 単元総合テスト - 確認テスト（問題文）
# ファイル: main.py

import logging
from characters import Character
from errors.exceptions import OutOfMPError

logging.basicConfig(level=logging.（）)  # [⑥]

hero = Character("勇者", 100, 10)

try:
    hero.use_magic(15)
except OutOfMPError as e:
    logging.（）("魔法の発動に失敗:" + str(e))  # [⑦]


# ===================================================
# 穴埋め知識問題（answers_04.txt に記入）
# ===================================================

# [⑧] ユーザーのパスワードをDBに保存するとき、正しい方法はどちらですか？
# A: パスワードをそのまま保存する
# B: パスワードを（）化してから保存する

# [⑨] OAuth2などの認可フローで、認証成功後にクライアントへ発行される
# 「有効期限付きの認証済み証明書」を何と呼ぶ？
# →（）トークン

# [⑩] SQLインジェクションを防ぐため、SQLの骨格とデータを分離し
# ?のようなプレースホルダーに値を後から渡す手法を何と呼ぶ？
# →パラメータ（）
