import pytest
from unittest.mock import patch
from io import StringIO

@patch('builtins.input', side_effect=["45", "liczbowo"])
@patch('sys.stdout', new_callable=StringIO)
def test_ocena_liczbowa_niedostateczny(mock_stdout, mock_input):
    exec(open('l7/l7_z8.py').read())
    output = mock_stdout.getvalue().strip()
    assert output == "Otrzymałeś ocenę: 2.0", f"Oczekiwano: 'Otrzymałeś ocenę: 2.0', otrzymano: '{output}'"

@patch('builtins.input', side_effect=["75", "słownie"])
@patch('sys.stdout', new_callable=StringIO)
def test_ocena_slowna_dobry(mock_stdout, mock_input):
    exec(open('l7/l7_z8.py').read())
    output = mock_stdout.getvalue().strip()
    assert output == "Otrzymałeś ocenę: dobry", f"Oczekiwano: 'Otrzymałeś ocenę: dobry', otrzymano: '{output}'"

@patch('builtins.input', side_effect=["88", "oba"])
@patch('sys.stdout', new_callable=StringIO)
def test_ocena_oba_dobry_plus(mock_stdout, mock_input):
    exec(open('l7/l7_z8.py').read())
    output = mock_stdout.getvalue().strip()
    assert output == "Otrzymałeś ocenę: 4.5 (dobry plus)", f"Oczekiwano: 'Otrzymałeś ocenę: 4.5 (dobry plus)', otrzymano: '{output}'"

@patch('builtins.input', side_effect=["105", "liczbowo"])
@patch('sys.stdout', new_callable=StringIO)
def test_ocena_celujacy(mock_stdout, mock_input):
    exec(open('l7/l7_z8.py').read())
    output = mock_stdout.getvalue().strip()
    assert output == "Otrzymałeś ocenę: 5.5", f"Oczekiwano: 'Otrzymałeś ocenę: 5.5', otrzymano: '{output}'"

@patch('builtins.input', side_effect=["92", "nieznana"])
@patch('sys.stdout', new_callable=StringIO)
def test_nieznana_forma_oceny(mock_stdout, mock_input):
    exec(open('l7/l7_z8.py').read())
    output = mock_stdout.getvalue().strip()
    assert output == "Nieznana forma oceny.", f"Oczekiwano: 'Nieznana forma oceny.', otrzymano: '{output}'"
