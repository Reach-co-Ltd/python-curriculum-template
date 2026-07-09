# 10章 02. 写経
# ファイル: app/battle.py
from app.errors.exceptions import InvalidStatusError

def calculate_damage(attack, defense):
    if defense < 0:
        raise InvalidStatusError("防御力は0以上でなければなりません")

    damage = attack - defense

    if damage <= 0:
        return 1
    return damage
