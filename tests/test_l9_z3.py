import pytest
from unittest.mock import patch
from io import StringIO

@patch('builtins.input', side_effect=["3", "10", "5", "13"])
@patch('sys.stdout', new_callable=StringIO)
def test_podstawowe_operacje(mock_stdout, mock_input):
    # Wywołanie kodu z pliku
    with patch('builtins.input', mock_input):
        with patch('sys.stdout', mock_stdout):
            exec(open('l9/l9_z3.py').read())

    output = mock_stdout.getvalue().strip().split('\n')
    assert output[0] == "Lista: [10, 5, 13]", f"Oczekiwano: 'Lista: [10, 5, 13]', otrzymano: '{output[0]}'"
    assert output[1] == "Najmniejsza wartość: 5", f"Oczekiwano: 'Najmniejsza wartość: 5', otrzymano: '{output[1]}'"
    assert output[2] == "Największa wartość: 13", f"Oczekiwano: 'Największa wartość: 13', otrzymano: '{output[2]}'"
    print("test_podstawowe_operacje przeszedł pomyślnie")

@patch('builtins.input', side_effect=["0"])
@patch('sys.stdout', new_callable=StringIO)
def test_bledna_wartosc(mock_stdout, mock_input):
    # Wywołanie kodu z pliku
    with patch('builtins.input', mock_input):
        with patch('sys.stdout', mock_stdout):
            exec(open('l9/l9_z3.py').read())

    output = mock_stdout.getvalue().strip()
    assert output == "Błędna wartość, wprowadź liczbę większą niż 0.", f"Oczekiwano: 'Błędna wartość, wprowadź liczbę większą niż 0.', otrzymano: '{output}'"
    print("test_bledna_wartosc przeszedł pomyślnie")

@patch('builtins.input', side_effect=["3", "a", "5", "13"])
@patch('sys.stdout', new_callable=StringIO)
def test_niepoprawna_wartosc(mock_stdout, mock_input):
    # Wywołanie kodu z pliku
    with patch('builtins.input', mock_input):
        with patch('sys.stdout', mock_stdout):
            exec(open('l9/l9_z3.py').read())

    output = mock_stdout.getvalue().strip()
    assert output == "Błędna wartość, wprowadź liczbę całkowitą.", f"Oczekiwano: 'Błędna wartość, wprowadź liczbę całkowitą.', otrzymano: '{output}'"
    print("test_niepoprawna_wartosc przeszedł pomyślnie")
