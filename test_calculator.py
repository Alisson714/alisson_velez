import pytest
from calculator import add

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -1) == -2

def test_add_zero():
    assert add(0, 5) == 5

def test_integration_cli():
    import subprocess
    import sys
    result = subprocess.run([sys.executable, 'calculator.py', '2', '3'], capture_output=True, text=True)
    assert result.returncode == 0
    assert "5.0" in result.stdout