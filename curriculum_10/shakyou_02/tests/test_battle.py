# 10章 02. 写経
# ファイル: tests/test_battle.py
import pytest
from app.battle import calculate_damage
from app.errors.exceptions import InvalidStatusError

def test_calculate_damage_normal():
    assert calculate_damage(100, 20) == 80
    assert calculate_damage(10, 50) == 1

def test_calculate_damage_negative_defense():
    with pytest.raises(InvalidStatusError, match="防御力は0以上でなければなりません"):
        calculate_damage(100, -10)
