'''Zad. 1 Napisać program proszący użytkownika o imię i rok urodzenia, a następnie obliczający i wypisujący jego wiek. 
Przykładowe wykonanie: 
Podaj swoje imię: 
Siemomysł 
Podaj rok urodzenia: 
1989 
Siemomysł, masz 33 lata.'''
import pytest
from unittest.mock import patch
from io import StringIO

@patch('builtins.input', side_effect=["Siemomysł", "1989"])
@patch('sys.stdout', new_callable=StringIO)
def test_poprawny_wiek(mock_stdout, mock_input):
    # Wywołanie kodu z pliku
    with patch('builtins.input', mock_input):
        with patch('sys.stdout', mock_stdout):
            exec(open('l7/l7_z1.py').read())

    output = mock_stdout.getvalue().strip()
    expected_output = "Siemomysł, masz 35 lat."
    assert output == expected_output, f"Oczekiwano: '{expected_output}', otrzymano: '{output}'"
    # print(f"Oczekiwano: '{expected_output}', otrzymano: '{output}'")

@patch('builtins.input', side_effect=["Anna", "2000"])
@patch('sys.stdout', new_callable=StringIO)
def test_inny_wiek(mock_stdout, mock_input):
    # Wywołanie kodu z pliku
    with patch('builtins.input', mock_input):
        with patch('sys.stdout', mock_stdout):
            exec(open('l7/l7_z1.py').read())

    output = mock_stdout.getvalue().strip()
    expected_output = "Anna, masz 24 lat."
    assert output == expected_output, f"Oczekiwano: '{expected_output}', otrzymano: '{output}'"

@patch('builtins.input', side_effect=["Jan", "2024"])
@patch('sys.stdout', new_callable=StringIO)
def test_wiek_zero(mock_stdout, mock_input):
    # Wywołanie kodu z pliku
    with patch('builtins.input', mock_input):
        with patch('sys.stdout', mock_stdout):
            exec(open('l7/l7_z1.py').read())

    output = mock_stdout.getvalue().strip()
    expected_output = "Jan, masz 0 lat."
    assert output == expected_output, f"Oczekiwano: '{expected_output}', otrzymano: '{output}'"
