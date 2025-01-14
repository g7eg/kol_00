import pytest
from io import StringIO
from unittest.mock import patch

@patch('sys.stdout', new_callable=StringIO)
def test_kombinacje_ksiazek(mock_stdout):
    exec(open('l8/l8_z7.py').read())
    output = mock_stdout.getvalue().strip().split("\n")
    
    expected_output = [
        "1 2 3", "1 2 4", "1 2 5", "1 3 4", "1 3 5", "1 4 5",
        "2 3 4", "2 3 5", "2 4 5", "3 4 5"
    ]
    
    assert output == expected_output, f"Oczekiwano:\n{expected_output},\notrzymano:\n{output}"
