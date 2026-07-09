# 08章 04. 単元総合テスト - 確認テスト（問題文）
# ファイル: characters.py

from errors.exceptions import OutOfMPError

class Character:
    def __init__(self, name: （）, hp: （）, mp: （）):  # [②][③]
        self.name = name
        self.hp = hp
        self.mp = mp  # hpと同じくインスタンス変数に直接代入する

    def use_magic(self, cost: int):
        if self.mp （） cost:  # [④] MPがcostより少ない場合
            （） OutOfMPError(self.name + "はMPが足りない！")  # [⑤] 例外を発生させる
        self.mp = self.mp - cost
        print(self.name + "は魔法を使った！残りMP:" + str(self.mp))
