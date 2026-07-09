# 10章 01. 写経
# ファイル: tests/test_sales.py
from app.sales import calculate_total_amount

def test_calculate_total_amount():
    test_price = 1000
    test_quantity = 3
    expected_amount = 3300

    actual_amount = calculate_total_amount(test_price, test_quantity)

    assert actual_amount == expected_amount
