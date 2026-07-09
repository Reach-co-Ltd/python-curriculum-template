# 08章 03. 既存コードの読解と実装 - 制作課題
# ファイル: characters.py
# curriculum_08/shakyou_03/ フォルダ内のこのファイルに写経してください

class Character:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        # ステータスを辞書型で管理します
        self.stats = {"mp": mp}

    def show_status(self):
        print("ステータス表示:" + self.name + "HP:" + str(self.hp) + "MP:" + str(self.stats["mp"]))
