import pytest
from unittest.mock import patch
from io import StringIO

@patch('builtins.input', side_effect=["Ala ma kota"])
@patch('sys.stdout', new_callable=StringIO)
def test_policz_wystapienia(mock_stdout, mock_input):
    # Wywołanie kodu z pliku
    with patch('builtins.input', mock_input):
        with patch('sys.stdout', mock_stdout):
            exec(open('l9/l9_z6.py').read())

    output = mock_stdout.getvalue().strip()
    expected_output = "{'a': 4, 'l': 1, 'm': 1, 'k': 1, 'o': 1, 't': 1}"
    assert output == expected_output, \
        f"Oczekiwano: '{expected_output}', otrzymano: '{output}'"
    print("test_policz_wystapienia przeszedł pomyślnie")

@patch('builtins.input', side_effect=["Python jest super"])
@patch('sys.stdout', new_callable=StringIO)
def test_policz_wystapienia_inne_znaki(mock_stdout, mock_input):
    # Wywołanie kodu z pliku
    with patch('builtins.input', mock_input):
        with patch('sys.stdout', mock_stdout):
            exec(open('l9/l9_z6.py').read())

    output = mock_stdout.getvalue().strip()
    expected_output = "{'p': 2, 'y': 1, 't': 2, 'h': 1, 'o': 1, 'n': 1, 'j': 1, 'e': 2, 's': 2, 'u': 1, 'r': 1}"
    assert output == expected_output, \
        f"Oczekiwano: '{expected_output}', otrzymano: '{output}'"
    print("test_policz_wystapienia_inne_znaki przeszedł pomyślnie")

@patch('builtins.input', side_effect=[""])
@patch('sys.stdout', new_callable=StringIO)
def test_policz_wystapienia_pusty_tekst(mock_stdout, mock_input):
    # Wywołanie kodu z pliku
    with patch('builtins.input', mock_input):
        with patch('sys.stdout', mock_stdout):
            exec(open('l9/l9_z6.py').read())

    output = mock_stdout.getvalue().strip()
    expected_output = "{}"
    assert output == expected_output, \
        f"Oczekiwano: '{expected_output}', otrzymano: '{output}'"
    print("test_policz_wystapienia_pusty_tekst przeszedł pomyślnie")
