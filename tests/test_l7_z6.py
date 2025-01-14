import pytest
from unittest.mock import patch
from io import StringIO

@patch('builtins.input', side_effect=["4"])
@patch('sys.stdout', new_callable=StringIO)
def test_liczba_parzysta(mock_stdout, mock_input):
    exec(open('l7/l7_z6.py').read())
    output = mock_stdout.getvalue().strip()
    assert output == "Liczba 4 jest parzysta.", f"Oczekiwano: 'Liczba 4 jest parzysta.', otrzymano: '{output}'"

@patch('builtins.input', side_effect=["7"])
@patch('sys.stdout', new_callable=StringIO)
def test_liczba_nieparzysta(mock_stdout, mock_input):
    exec(open('l7/l7_z6.py').read())
    output = mock_stdout.getvalue().strip()
    assert output == "Liczba 7 jest nieparzysta.", f"Oczekiwano: 'Liczba 7 jest nieparzysta.', otrzymano: '{output}'"

@patch('builtins.input', side_effect=["0"])
@patch('sys.stdout', new_callable=StringIO)
def test_liczba_zero(mock_stdout, mock_input):
    exec(open('l7/l7_z6.py').read())
    output = mock_stdout.getvalue().strip()
    assert output == "Liczba 0 jest parzysta.", f"Oczekiwano: 'Liczba 0 jest parzysta.', otrzymano: '{output}'"
