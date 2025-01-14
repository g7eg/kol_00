import pytest
from io import StringIO
from unittest.mock import patch

@patch('builtins.input', side_effect=["3", "10", "5", "13"])
@patch('sys.stdout', new_callable=StringIO)
def test_poprawne_wprowadzenie(mock_stdout, mock_input):
    exec(open('l9/l9_z1.py').read())
    output = mock_stdout.getvalue().strip().split("\n")
    expected_output = [
        "Ile chcesz wprowadzić liczb?",
        "Podaj liczbę:", "Podaj liczbę:", "Podaj liczbę:",
        "Lista: [10, 5, 13]"
    ]
    assert output == expected_output, f"Oczekiwano:\n{expected_output},\notrzymano:\n{output}"

@patch('builtins.input', side_effect=["0"])
@patch('sys.stdout', new_callable=StringIO)
def test_zerowa_ilosc(mock_stdout, mock_input):
    exec(open('l9/l9_z1.py').read())
    output = mock_stdout.getvalue().strip()
    expected_output = "Ile chcesz wprowadzić liczb?\nBłędna wartość, wprowadź liczbę większą niż 0."
    assert output == expected_output, f"Oczekiwano:\n{expected_output},\notrzymano:\n{output}"

@patch('builtins.input', side_effect=["abc"])
@patch('sys.stdout', new_callable=StringIO)
def test_bledna_wartosc(mock_stdout, mock_input):
    exec(open('l9/l9_z1.py').read())
    output = mock_stdout.getvalue().strip()
    expected_output = "Ile chcesz wprowadzić liczb?\nBłędna wartość, wprowadź liczbę całkowitą."
    assert output == expected_output, f"Oczekiwano:\n{expected_output},\notrzymano:\n{output}"
