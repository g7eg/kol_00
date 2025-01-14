import pytest
from unittest.mock import patch
from io import StringIO

@patch('builtins.input', side_effect=["3", "4", "5"])
@patch('sys.stdout', new_callable=StringIO)
def test_mozna_utworzyc_trojkat(mock_stdout, mock_input):
    exec(open('l7/l7_z7.py').read())
    output = mock_stdout.getvalue().strip()
    assert output == "Można stworzyć trójkąt.", f"Oczekiwano: 'Można stworzyć trójkąt.', otrzymano: '{output}'"

@patch('builtins.input', side_effect=["1", "1", "3"])
@patch('sys.stdout', new_callable=StringIO)
def test_nie_mozna_utworzyc_trojkata(mock_stdout, mock_input):
    exec(open('l7/l7_z7.py').read())
    output = mock_stdout.getvalue().strip()
    assert output == "Nie można stworzyć trójkąta.", f"Oczekiwano: 'Nie można stworzyć trójkąta.', otrzymano: '{output}'"

@patch('builtins.input', side_effect=["2", "2", "2"])
@patch('sys.stdout', new_callable=StringIO)
def test_mozna_utworzyc_trojkat_rownoboczny(mock_stdout, mock_input):
    exec(open('l7/l7_z7.py').read())
    output = mock_stdout.getvalue().strip()
    assert output == "Można stworzyć trójkąt.", f"Oczekiwano: 'Można stworzyć trójkąt.', otrzymano: '{output}'"
