import pytest
from io import StringIO
from unittest.mock import patch

@patch('sys.stdout', new_callable=StringIO)
def test_kwadrat_10x10(mock_stdout):
    exec(open('l8/l8_z6.py').read())
    output = mock_stdout.getvalue().strip()
    
    expected_output = "\n".join(["*" * 10 for _ in range(10)])
    
    assert output == expected_output, f"Oczekiwano:\n{expected_output},\notrzymano:\n{output}"
