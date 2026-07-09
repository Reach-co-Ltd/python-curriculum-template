# 10章 03. 写経
# ファイル: tests/test_auth.py
import pytest
from app.auth import validate_password

@pytest.mark.parametrize("test_pass,expected", [
    ("my_secure_pass", True),
    ("12345678", True),
    ("short", False),
    ("1234567", False),
    ("admin1234", False),
])
def test_validate_password_strength(test_pass, expected):
    actual = validate_password(test_pass)
    assert actual == expected
