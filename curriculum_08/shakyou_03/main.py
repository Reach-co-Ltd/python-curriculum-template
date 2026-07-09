# 08章 03. 既存コードの読解と実装 - 制作課題
# ファイル: main.py
# curriculum_08/shakyou_03/ フォルダ内のこのファイルに写経してください

# 別ファイルからCharacterクラスをインポートします
from characters import Character

# 正常なキャラクター生成
hero = Character("勇者", 100, 50)
hero.show_status()
