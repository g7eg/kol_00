import pytest
from unittest.mock import patch
from io import StringIO

@patch('builtins.input', side_effect=["Informatyka"])
@patch('sys.stdout', new_callable=StringIO)
def test_kierunek_istnieje(mock_stdout, mock_input):
    # Wywołanie kodu z pliku
    with patch('builtins.input', mock_input):
        with patch('sys.stdout', mock_stdout):
            exec(open('l9/l9_z5.py').read())

    output = mock_stdout.getvalue().strip()
    assert output == "Kierunek Informatyka znajduje się na Wydział Elektroniki.", \
        f"Oczekiwano: 'Kierunek Informatyka znajduje się na Wydział Elektroniki.', otrzymano: '{output}'"
    print("test_kierunek_istnieje przeszedł pomyślnie")

@patch('builtins.input', side_effect=["Ekonomia"])
@patch('sys.stdout', new_callable=StringIO)
def test_kierunek_nieistnieje(mock_stdout, mock_input):
    # Wywołanie kodu z pliku
    with patch('builtins.input', mock_input):
        with patch('sys.stdout', mock_stdout):
            exec(open('l9/l9_z5.py').read())

    output = mock_stdout.getvalue().strip()
    assert output == "Nie możesz studiować kierunku Ekonomia na Politechnice Wrocławskiej.", \
        f"Oczekiwano: 'Nie możesz studiować kierunku Ekonomia na Politechnice Wrocławskiej.', otrzymano: '{output}'"
    print("test_kierunek_nieistnieje przeszedł pomyślnie")

@patch('builtins.input', side_effect=["Architektura"])
@patch('sys.stdout', new_callable=StringIO)
def test_kierunek_istnieje_2(mock_stdout, mock_input):
    # Wywołanie kodu z pliku
    with patch('builtins.input', mock_input):
        with patch('sys.stdout', mock_stdout):
            exec(open('l9/l9_z5.py').read())

    output = mock_stdout.getvalue().strip()
    assert output == "Kierunek Architektura znajduje się na Wydział Architektury.", \
        f"Oczekiwano: 'Kierunek Architektura znajduje się na Wydział Architektury.', otrzymano: '{output}'"
    print("test_kierunek_istnieje_2 przeszedł pomyślnie")
