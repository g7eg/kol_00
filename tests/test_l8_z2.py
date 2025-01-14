import pytest
from unittest.mock import patch
from io import StringIO

@patch('builtins.input', side_effect=["5"])
@patch('sys.stdout', new_callable=StringIO)
def test_liczby_dodatnie(mock_stdout, mock_input):
    exec(open('l8/l8_z2.py').read())
    output = mock_stdout.getvalue().strip().split("\n")
    expected_output = [str(i) for i in range(6)]
    assert output == expected_output, f"Oczekiwano: {expected_output}, otrzymano: {output}"

@patch('builtins.input', side_effect=["0"])
@patch('sys.stdout', new_callable=StringIO)
def test_liczba_zero(mock_stdout, mock_input):
    exec(open('l8/l8_z2.py').read())
    output = mock_stdout.getvalue().strip()
    assert output == "0", f"Oczekiwano: '0', otrzymano: '{output}'"

@patch('builtins.input', side_effect=["-3"])
@patch('sys.stdout', new_callable=StringIO)
def test_liczba_ujemna(mock_stdout, mock_input):
    exec(open('l8/l8_z2.py').read())
    output = mock_stdout.getvalue().strip()
    assert output == "Błąd: Liczba y musi być większa lub równa 0.", f"Oczekiwano: 'Błąd: Liczba y musi być większa lub równa 0.', otrzymano: '{output}'"
