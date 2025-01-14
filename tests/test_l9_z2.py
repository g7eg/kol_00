import pytest
from io import StringIO
from unittest.mock import patch

# Test poprawnego wprowadzenia liczb
@patch('builtins.input', side_effect=["3", "2", "3", "4"])
@patch('sys.stdout', new_callable=StringIO)
def test_poprawne_wprowadzenie(mock_stdout, mock_input):
    exec(open('l9/l9_z2.py').read())
    
    output = mock_stdout.getvalue().strip().split("\n")
    expected_output = [
        "Lista: [2, 3, 4]",
        "Suma: 9"
    ]
    assert output[-2:] == expected_output, f"Oczekiwano:\n{expected_output},\notrzymano:\n{output[-2:]}"

# Test gdy użytkownik podaje 0 jako liczbę do wprowadzenia
@patch('builtins.input', side_effect=["0"])
@patch('sys.stdout', new_callable=StringIO)
def test_zerowa_ilosc(mock_stdout, mock_input):
    exec(open('l9/l9_z2.py').read())
    
    output = mock_stdout.getvalue().strip()
    assert "Błędna wartość, wprowadź liczbę większą niż 0." in output, f"Oczekiwano komunikatu o błędnej wartości, otrzymano:\n{output}"

# Test, gdy użytkownik wprowadza błędną wartość
@patch('builtins.input', side_effect=["abc"])
@patch('sys.stdout', new_callable=StringIO)
def test_bledna_wartosc(mock_stdout, mock_input):
    exec(open('l9/l9_z2.py').read())
    
    output = mock_stdout.getvalue().strip()
    assert "Błędna wartość, wprowadź liczbę całkowitą." in output, f"Oczekiwano komunikatu o błędnej wartości, otrzymano:\n{output}"
