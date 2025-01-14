import pytest
from unittest.mock import patch
from io import StringIO

@patch('builtins.input', side_effect=["5", "3"])
@patch('sys.stdout', new_callable=StringIO)
def test_a_wieksze_od_b(mock_stdout, mock_input):
    # Wywołanie kodu z pliku
    with patch('builtins.input', mock_input):
        with patch('sys.stdout', mock_stdout):
            exec(open('l7/l7_z4.py').read())

    output = mock_stdout.getvalue().strip()
    assert output == "Liczba 5.0 jest większa od 3.0.", f"Oczekiwano: 'Liczba 5.0 jest większa od 3.0.', otrzymano: '{output}'"
    print("test_a_wieksze_od_b przeszedł pomyślnie")

@patch('builtins.input', side_effect=["2", "4"])
@patch('sys.stdout', new_callable=StringIO)
def test_b_wieksze_od_a(mock_stdout, mock_input):
    # Wywołanie kodu z pliku
    with patch('builtins.input', mock_input):
        with patch('sys.stdout', mock_stdout):
            exec(open('l7/l7_z4.py').read())

    output = mock_stdout.getvalue().strip()
    assert output == "Liczba 4.0 jest większa od 2.0.", f"Oczekiwano: 'Liczba 4.0 jest większa od 2.0.', otrzymano: '{output}'"
    print("test_b_wieksze_od_a przeszedł pomyślnie")

@patch('builtins.input', side_effect=["7", "7"])
@patch('sys.stdout', new_callable=StringIO)
def test_liczby_rowne(mock_stdout, mock_input):
    # Wywołanie kodu z pliku
    with patch('builtins.input', mock_input):
        with patch('sys.stdout', mock_stdout):
            exec(open('l7/l7_z4.py').read())

    output = mock_stdout.getvalue().strip()
    assert output == "Liczby są sobie równe.", f"Oczekiwano: 'Liczby są sobie równe.', otrzymano: '{output}'"
    print("test_liczby_rowne przeszedł pomyślnie")
