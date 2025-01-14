import pytest
from unittest.mock import patch
from io import StringIO

@patch('builtins.input', side_effect=["5", "1", "2", "3", "4", "5", "5"])
@patch('sys.stdout', new_callable=StringIO)
def test_pary_liczb(mock_stdout, mock_input):
    # Wywołanie kodu z pliku
    with patch('builtins.input', mock_input):
        with patch('sys.stdout', mock_stdout):
            exec(open('l9/l9_z4.py').read())

    output = mock_stdout.getvalue().strip().split('\n')
    assert output[0] == "Lista: [1, 2, 3, 4, 5]", f"Oczekiwano: 'Lista: [1, 2, 3, 4, 5]', otrzymano: '{output[0]}'"
    assert output[1] == "1 + 4 = 5", f"Oczekiwano: '1 + 4 = 5', otrzymano: '{output[1]}'"
    assert output[2] == "2 + 3 = 5", f"Oczekiwano: '2 + 3 = 5', otrzymano: '{output[2]}'"
    print("test_pary_liczb przeszedł pomyślnie")

@patch('builtins.input', side_effect=["3", "1", "2", "3", "7"])
@patch('sys.stdout', new_callable=StringIO)
def test_brak_par(mock_stdout, mock_input):
    # Wywołanie kodu z pliku
    with patch('builtins.input', mock_input):
        with patch('sys.stdout', mock_stdout):
            exec(open('l9/l9_z4.py').read())

    output = mock_stdout.getvalue().strip()
    assert output == "Lista: [1, 2, 3]\nBrak par liczb, których suma jest równa szukanej sumie.", \
        f"Oczekiwano: 'Lista: [1, 2, 3]\nBrak par liczb, których suma jest równa szukanej sumie.', otrzymano: '{output}'"
    print("test_brak_par przeszedł pomyślnie")

@patch('builtins.input', side_effect=["3", "a", "2", "3", "5"])
@patch('sys.stdout', new_callable=StringIO)
def test_niepoprawna_wartosc(mock_stdout, mock_input):
    # Wywołanie kodu z pliku
    with patch('builtins.input', mock_input):
        with patch('sys.stdout', mock_stdout):
            exec(open('l9/l9_z4.py').read())

    output = mock_stdout.getvalue().strip()
    assert output == "Błędna wartość, wprowadź liczbę całkowitą.", f"Oczekiwano: 'Błędna wartość, wprowadź liczbę całkowitą.', otrzymano: '{output}'"
    print("test_niepoprawna_wartosc przeszedł pomyślnie")
