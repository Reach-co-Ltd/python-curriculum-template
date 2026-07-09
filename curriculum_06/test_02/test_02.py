# 06章 02. 文字列操作 - 確認テスト（問題文）
# 会員管理システムにおける文字列処理の一部です。
# [①]〜[⑩]の（）に入るコードを考えて、answers_02.txt に番号ごとの答えを記入してください。
# 答え合わせが終わったら、完成したコードを shakyou_02.py に1文字ずつ書き写して実行してください。

# ===会員管理システム文字列処理===

# [①] 名前と挨拶文を結合してメッセージを作る
greeting = "こんにちは、"
name = "田中さん"
message = greeting（）name
print(message)

# [②] 区切り線を10回繰り返して表示する
line = "-"
print(line（）10)

# [③] メールアドレスの先頭3文字だけを取り出す
email = "tanaka@example.com"
print(email（）)

# [④] メールアドレスの最後の1文字を取り出す
print(email（）)

# [⑤] 入力されたメールアドレスを小文字に統一する
raw_email = "Tanaka@EXAMPLE.com"
clean_email = raw_email.（）()
print(clean_email)

# [⑥] ユーザー名に含まれる空白を取り除く
raw_name = "  田中  "
clean_name = raw_name.（）()
print(clean_name)

# [⑦] 電話番号のハイフンを削除する
phone = "090-1234-5678"
clean_phone = phone.（）("-", "")
print(clean_phone)

# [⑧] CSV形式の文字列をカンマで分割してリストにする
csv_line = "田中,25,エンジニア"
parts = csv_line.（）(",")
print(parts)

# [⑨] メールアドレスが"@example.com"で終わっているか確認する
print(email.（）("@example.com"))

# [⑩] 入力されたユーザーIDが数字だけで構成されているか確認する
user_id = "12345"
print(user_id.（）())
