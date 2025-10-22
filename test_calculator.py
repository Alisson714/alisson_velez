import pytest
from calculator import add

def test_add_positive_numbers():
    assert add(2, 3) == 6

def test_add_negative_numbers():
    assert add(-1, -1) == -2

def test_add_zero():
    assert add(0, 5) == 5

def test_integration_cli():
    import subprocess
    import sys
    result = subprocess.run([sys.executable, 'calculator.py', '2', '3'], capture_output=True, text=True)
    assert "The sum of 2.0 and 3.0 is 5.0" in result.stdout