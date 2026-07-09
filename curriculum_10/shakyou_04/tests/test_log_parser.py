# 10章 04. 写経
# ファイル: tests/test_log_parser.py
import pytest
import os
from app.log_parser import contains_error_log

@pytest.fixture
def dummy_log_file():
    file_name = "test_log.txt"

    with open(file_name, "w", encoding="utf-8") as f:
        f.write("INFO:System started\n")
        f.write("ERROR:Database connection failed\n")

    yield file_name

    if os.path.exists(file_name):
        os.remove(file_name)

def test_contains_error_log(dummy_log_file):
    result = contains_error_log(dummy_log_file)
    assert result == True
