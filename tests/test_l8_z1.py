import pytest
from unittest.mock import patch
from io import StringIO

@patch('builtins.input', side_effect=["1", "-22", "8", "-3.5", "13", "end"])
@patch('sys.stdout', new_callable=StringIO)
def test_poprawna_srednia(mock_stdout, mock_input):
    exec(open('l8/l8_z1.py').read())
    output = mock_stdout.getvalue().strip().split("\n")[-1]
    assert output == "Średnia arytmetyczna wynosi: -0.7", f"Oczekiwano: 'Średnia arytmetyczna wynosi: -0.7', otrzymano: '{output}'"

@patch('builtins.input', side_effect=["end"])
@patch('sys.stdout', new_callable=StringIO)
def test_end_na_poczatku(mock_stdout, mock_input):
    exec(open('l8/l8_z1.py').read())
    output = mock_stdout.getvalue().strip()
    assert output == "Błąd: 'end' nie może być pierwszą podaną wartością.", f"Oczekiwano: 'Błąd: 'end' nie może być pierwszą podaną wartością.', otrzymano: '{output}'"

@patch('builtins.input', side_effect=["1.5", "2.5", "3", "end"])
@patch('sys.stdout', new_callable=StringIO)
def test_poprawna_srednia_z_liczb_dodatnich(mock_stdout, mock_input):
    exec(open('l8/l8_z1.py').read())
    output = mock_stdout.getvalue().strip().split("\n")[-1]
    assert output == "Średnia arytmetyczna wynosi: 2.3333333333333335", f"Oczekiwano: 'Średnia arytmetyczna wynosi: 2.3333333333333335', otrzymano: '{output}'"

@patch('builtins.input', side_effect=["abc", "4", "end"])
@patch('sys.stdout', new_callable=StringIO)
def test_niepoprawna_wartosc(mock_stdout, mock_input):
    exec(open('l8/l8_z1.py').read())
    output = mock_stdout.getvalue().strip().split("\n")
    assert output[-2] == "Błąd: Wprowadzono nieprawidłową wartość.", f"Oczekiwano: 'Błąd: Wprowadzono nieprawidłową wartość.', otrzymano: '{output[-2]}'"
    assert output[-1] == "Średnia arytmetyczna wynosi: 4.0", f"Oczekiwano: 'Średnia arytmetyczna wynosi: 4.0', otrzymano: '{output[-1]}'"

@patch('builtins.input', side_effect=["0", "-1", "1", "end"])
@patch('sys.stdout', new_callable=StringIO)
def test_srednia_rownosci_zero(mock_stdout, mock_input):
    exec(open('l8/l8_z1.py').read())
    output = mock_stdout.getvalue().strip().split("\n")[-1]
    assert output == "Średnia arytmetyczna wynosi: 0.0", f"Oczekiwano: 'Średnia arytmetyczna wynosi: 0.0', otrzymano: '{output}'"
