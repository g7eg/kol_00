import pytest
from unittest.mock import patch
from io import StringIO

@patch('builtins.input', side_effect=["10"])
@patch('sys.stdout', new_callable=StringIO)
def test_podzielne_przez_10(mock_stdout, mock_input):
    exec(open('l8/l8_z4.py').read())
    output = mock_stdout.getvalue().strip().split("\n")
    expected_output = ["50", "60", "70", "80", "90", "100"]
    assert output == expected_output, f"Oczekiwano: {expected_output}, otrzymano: {output}"

@patch('builtins.input', side_effect=["7"])
@patch('sys.stdout', new_callable=StringIO)
def test_podzielne_przez_7(mock_stdout, mock_input):
    exec(open('l8/l8_z4.py').read())
    output = mock_stdout.getvalue().strip().split("\n")
    expected_output = ["56", "63", "70", "77", "84", "91", "98"]
    assert output == expected_output, f"Oczekiwano: {expected_output}, otrzymano: {output}"

@patch('builtins.input', side_effect=["1"])
@patch('sys.stdout', new_callable=StringIO)
def test_podzielne_przez_1(mock_stdout, mock_input):
    exec(open('l8/l8_z4.py').read())
    output = mock_stdout.getvalue().strip().split("\n")
    expected_output = [str(i) for i in range(50, 101)]
    assert output == expected_output, f"Oczekiwano: {expected_output}, otrzymano: {output}"

@patch('builtins.input', side_effect=["0"])
@patch('sys.stdout', new_callable=StringIO)
def test_podzielne_przez_0(mock_stdout, mock_input):
    exec(open('l8/l8_z4.py').read())
    output = mock_stdout.getvalue().strip()
    assert output == "Błąd: Liczba k musi być większa od zera.", f"Oczekiwano: 'Błąd: Liczba k musi być większa od zera.', otrzymano: '{output}'"
