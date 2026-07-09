# curriculum_05 / SQL基礎 / 写経問題
# バックログの写経内容に従って実装してください
# 実行: python 01_basic_sql.py

import sqlite3

conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

# TODO 1: tasks テーブルを作成する（id / title / done）


# TODO 2: 3件 INSERT する


# TODO 3: 全件 SELECT して表示する


# TODO 4: id=1 の done を 1 に UPDATE する


# TODO 5: id=3 を DELETE する


cursor.execute("SELECT * FROM tasks")
for row in cursor.fetchall():
    print(row)

conn.close()
