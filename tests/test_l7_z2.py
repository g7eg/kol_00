import pytest
from unittest.mock import patch
from io import StringIO
import math

@patch('builtins.input', side_effect=["3", "4"])
@patch('sys.stdout', new_callable=StringIO)
def test_podstawowe_operacje(mock_stdout, mock_input):
    # Wywołanie kodu z pliku
    with patch('builtins.input', mock_input):
        with patch('sys.stdout', mock_stdout):
            exec(open('l7/l7_z2.py').read())

    output = mock_stdout.getvalue().strip().split('\n')
    assert output[0] == "Suma: 7.0", f"Oczekiwano: 'Suma: 7.0', otrzymano: '{output[0]}'"
    assert output[1] == "Różnica: -1.0", f"Oczekiwano: 'Różnica: -1.0', otrzymano: '{output[1]}'"
    assert output[2] == "Iloczyn: 12.0", f"Oczekiwano: 'Iloczyn: 12.0', otrzymano: '{output[2]}'"
    assert output[3] == "Iloraz: 0.75", f"Oczekiwano: 'Iloraz: 0.75', otrzymano: '{output[3]}'"
    assert output[4] == f"Pierwiastek z (a + b): {math.sqrt(7)}", f"Oczekiwano: 'Pierwiastek z (a + b): {math.sqrt(7)}', otrzymano: '{output[4]}'"
    assert output[5] == "a do potęgi b: 81.0", f"Oczekiwano: 'a do potęgi b: 81.0', otrzymano: '{output[5]}'"
    assert output[6] == "b do potęgi a: 64.0", f"Oczekiwano: 'b do potęgi a: 64.0', otrzymano: '{output[6]}'"
    print("test_podstawowe_operacje przeszedł pomyślnie")

@patch('builtins.input', side_effect=["-3", "-4"])
@patch('sys.stdout', new_callable=StringIO)
def test_ujemne_liczby(mock_stdout, mock_input):
    # Wywołanie kodu z pliku
    with patch('builtins.input', mock_input):
        with patch('sys.stdout', mock_stdout):
            exec(open('l7/l7_z2.py').read())

    output = mock_stdout.getvalue().strip().split('\n')
    assert output[0] == "Suma: -7.0", f"Oczekiwano: 'Suma: -7.0', otrzymano: '{output[0]}'"
    assert output[1] == "Różnica: 1.0", f"Oczekiwano: 'Różnica: 1.0', otrzymano: '{output[1]}'"
    assert output[2] == "Iloczyn: 12.0", f"Oczekiwano: 'Iloczyn: 12.0', otrzymano: '{output[2]}'"
    assert output[3] == "Iloraz: 0.75", f"Oczekiwano: 'Iloraz: 0.75', otrzymano: '{output[3]}'"
    assert output[4] == "Pierwiastek z (a + b): undefined", f"Oczekiwano: 'Pierwiastek z (a + b): undefined', otrzymano: '{output[4]}'"
    assert output[5] == "a do potęgi b: 0.012345679012345678", f"Oczekiwano: 'a do potęgi b: 0.012345679012345678', otrzymano: '{output[5]}'"
    assert output[6] == "b do potęgi a: -0.015625", f"Oczekiwano: 'b do potęgi a: -0.015625', otrzymano: '{output[6]}'"
    print("test_ujemne_liczby przeszedł pomyślnie")

@patch('builtins.input', side_effect=["5", "0"])
@patch('sys.stdout', new_callable=StringIO)
def test_zero(mock_stdout, mock_input):
    # Wywołanie kodu z pliku
    with patch('builtins.input', mock_input):
        with patch('sys.stdout', mock_stdout):
            exec(open('l7/l7_z2.py').read())

    output = mock_stdout.getvalue().strip().split('\n')
    assert output[0] == "Suma: 5.0", f"Oczekiwano: 'Suma: 5.0', otrzymano: '{output[0]}'"
    assert output[1] == "Różnica: 5.0", f"Oczekiwano: 'Różnica: 5.0', otrzymano: '{output[1]}'"
    assert output[2] == "Iloczyn: 0.0", f"Oczekiwano: 'Iloczyn: 0.0', otrzymano: '{output[2]}'"
    assert output[3] == "Iloraz: undefined", f"Oczekiwano: 'Iloraz: undefined', otrzymano: '{output[3]}'"
    assert output[4] == f"Pierwiastek z (a + b): {math.sqrt(5)}", f"Oczekiwano: 'Pierwiastek z (a + b): {math.sqrt(5)}', otrzymano: '{output[4]}'"
    assert output[5] == "a do potęgi b: 1.0", f"Oczekiwano: 'a do potęgi b: 1.0', otrzymano: '{output[5]}'"
    assert output[6] == "b do potęgi a: 0.0", f"Oczekiwano: 'b do potęgi a: 0.0', otrzymano: '{output[6]}'"
    print("test_zero przeszedł pomyślnie")
