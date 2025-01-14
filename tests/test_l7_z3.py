import pytest
from unittest.mock import patch
from io import StringIO
import math

@patch('builtins.input', side_effect=["5"])
@patch('sys.stdout', new_callable=StringIO)
def test_obliczenia_poprawne(mock_stdout, mock_input):
    # Wywołanie kodu z pliku
    with patch('builtins.input', mock_input):
        with patch('sys.stdout', mock_stdout):
            exec(open('l7/l7_z3.py').read())

    output = mock_stdout.getvalue().strip().split('\n')
    expected_area = math.pi * 5 ** 2
    expected_circumference = 2 * math.pi * 5
    assert output[0] == f"Pole koła: {expected_area}", f"Oczekiwano: 'Pole koła: {expected_area}', otrzymano: '{output[0]}'"
    assert output[1] == f"Obwód koła: {expected_circumference}", f"Oczekiwano: 'Obwód koła: {expected_circumference}', otrzymano: '{output[1]}'"
    print("test_obliczenia_poprawne przeszedł pomyślnie")

@patch('builtins.input', side_effect=["-5"])
@patch('sys.stdout', new_callable=StringIO)
def test_promien_ujemny(mock_stdout, mock_input):
    # Wywołanie kodu z pliku
    with patch('builtins.input', mock_input):
        with patch('sys.stdout', mock_stdout):
            exec(open('l7/l7_z3.py').read())

    output = mock_stdout.getvalue().strip()
    assert output == "Błąd: Promień nie może być ujemny.", f"Oczekiwano: 'Błąd: Promień nie może być ujemny.', otrzymano: '{output}'"
    print("test_promien_ujemny przeszedł pomyślnie")

@patch('builtins.input', side_effect=["0"])
@patch('sys.stdout', new_callable=StringIO)
def test_promien_zero(mock_stdout, mock_input):
    # Wywołanie kodu z pliku
    with patch('builtins.input', mock_input):
        with patch('sys.stdout', mock_stdout):
            exec(open('l7/l7_z3.py').read())

    output = mock_stdout.getvalue().strip().split('\n')
    expected_area = math.pi * 0 ** 2
    expected_circumference = 2 * math.pi * 0
    assert output[0] == f"Pole koła: {expected_area}", f"Oczekiwano: 'Pole koła: {expected_area}', otrzymano: '{output[0]}'"
    assert output[1] == f"Obwód koła: {expected_circumference}", f"Oczekiwano: 'Obwód koła: {expected_circumference}', otrzymano: '{output[1]}'"
    print("test_promien_zero przeszedł pomyślnie")
