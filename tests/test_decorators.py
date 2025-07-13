import pytest
import time
from src.decorators import add_logfile

def test_add_logfile(capsys):
    @add_logfile()
    def my_function(a, b):
        return a / b
    my_function(10, 2)
    capture = capsys.readouterr()
    output = capture.out
    assert 'my_function ok' in output
    assert 'start time' in output
    assert 'finish time' in output

def test_add_logfile_in_file(tmp_path):
    log_file = tmp_path / "test_logs.txt"
    @add_logfile(filename=str(log_file))
    def my_function(a, b):
        return a + b
    my_function(10, 2)
    assert log_file.exists()
    content = log_file.read_text(encoding='utf-8')
    assert "my_function ok" in content

def test_add_logfile_errors(capsys):
    @add_logfile()
    def my_function(a, b):
        return a / b
    my_function(10, 0)
    capture = capsys.readouterr()
    output = capture.out
    assert 'my_function error' in output
    assert 'division by zero' in output
    assert 'input' in output
