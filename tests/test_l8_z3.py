import pytest
from unittest.mock import patch
from io import StringIO

@patch('builtins.input', side_effect=["3", "7"])
@patch('sys.stdout', new_callable=StringIO)
def test_przedzial_poprawny(mock_stdout, mock_input):
    exec(open('l8/l8_z3.py').read())
    output = mock_stdout.getvalue().strip().split("\n")
    expected_output = [str(i) for i in range(3, 8)]
    assert output == expected_output, f"Oczekiwano: {expected_output}, otrzymano: {output}"

@patch('builtins.input', side_effect=["5", "5"])
@patch('sys.stdout', new_callable=StringIO)
def test_przedzial_pojedyncza_liczba(mock_stdout, mock_input):
    exec(open('l8/l8_z3.py').read())
    output = mock_stdout.getvalue().strip()
    assert output == "5", f"Oczekiwano: '5', otrzymano: '{output}'"

@patch('builtins.input', side_effect=["7", "3"])
@patch('sys.stdout', new_callable=StringIO)
def test_przedzial_odwrotny(mock_stdout, mock_input):
    exec(open('l8/l8_z3.py').read())
    output = mock_stdout.getvalue().strip()
    assert output == "Błąd: Liczba x musi być mniejsza lub równa liczbie y.", f"Oczekiwano: 'Błąd: Liczba x musi być mniejsza lub równa liczbie y.', otrzymano: '{output}'"
