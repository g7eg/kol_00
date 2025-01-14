import pytest
from unittest.mock import patch
from io import StringIO
from datetime import datetime

current_year = datetime.now().year

@patch('builtins.input', side_effect=["Siemomysł", "1989"])
@patch('sys.stdout', new_callable=StringIO)
def test_pelnoltnosc(mock_stdout, mock_input):
    # Wywołanie kodu z pliku
    with patch('builtins.input', mock_input):
        with patch('sys.stdout', mock_stdout):
            exec(open('l7/l7_z5.py').read())

    age = current_year - 1989
    expected_output = f"Siemomysł, masz {age} lat, jesteś pełnoletni."
    output = mock_stdout.getvalue().strip()
    assert output == expected_output, f"Oczekiwano: '{expected_output}', otrzymano: '{output}'"

@patch('builtins.input', side_effect=["Jadwiga", "2010"])
@patch('sys.stdout', new_callable=StringIO)
def test_niepelnoletni(mock_stdout, mock_input):
    # Wywołanie kodu z pliku
    with patch('builtins.input', mock_input):
        with patch('sys.stdout', mock_stdout):
            exec(open('l7/l7_z5.py').read())

    age = current_year - 2010
    expected_output = f"Jadwiga, masz {age} lat, nie jesteś pełnoletni."
    output = mock_stdout.getvalue().strip()
    assert output == expected_output, f"Oczekiwano: '{expected_output}', otrzymano: '{output}'"

@patch('builtins.input', side_effect=["Kazimierz", "2005"])
@patch('sys.stdout', new_callable=StringIO)
def test_granica_pelnoltnosci(mock_stdout, mock_input):
    # Wywołanie kodu z pliku
    with patch('builtins.input', mock_input):
        with patch('sys.stdout', mock_stdout):
            exec(open('l7/l7_z5.py').read())

    age = current_year - 2005
    expected_output = f"Kazimierz, masz {age} lat, jesteś pełnoletni."
    output = mock_stdout.getvalue().strip()
    assert output == expected_output, f"Oczekiwano: '{expected_output}', otrzymano: '{output}'"
