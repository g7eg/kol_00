import pytest
from unittest.mock import patch
from io import StringIO

@patch('builtins.input', side_effect=["50", "30", "42"])
@patch('sys.stdout', new_callable=StringIO)
def test_odgadniecie_w_trzech_probach(mock_stdout, mock_input):
    exec(open('l8/l8_z5.py').read())
    output = mock_stdout.getvalue().strip().split("\n")
    expected_output = [
        "Szukana wartość jest mniejsza",
        "Szukana wartość jest większa",
        "Brawo! Odgadłeś liczbę w 3 próbach."
    ]
    assert output == expected_output, f"Oczekiwano: {expected_output}, otrzymano: {output}"

@patch('builtins.input', side_effect=["10", "60", "55", "42"])
@patch('sys.stdout', new_callable=StringIO)
def test_odgadniecie_w_czterech_probach(mock_stdout, mock_input):
    exec(open('l8/l8_z5.py').read())
    output = mock_stdout.getvalue().strip().split("\n")
    expected_output = [
        "Szukana wartość jest większa",
        "Szukana wartość jest mniejsza",
        "Szukana wartość jest mniejsza",
        "Brawo! Odgadłeś liczbę w 4 próbach."
    ]
    assert output == expected_output, f"Oczekiwano: {expected_output}, otrzymano: {output}"

@patch('builtins.input', side_effect=["42"])
@patch('sys.stdout', new_callable=StringIO)
def test_odgadniecie_za_pierwszym_razem(mock_stdout, mock_input):
    exec(open('l8/l8_z5.py').read())
    output = mock_stdout.getvalue().strip()
    expected_output = "Brawo! Odgadłeś liczbę w 1 próbach."
    assert output == expected_output, f"Oczekiwano: '{expected_output}', otrzymano: '{output}'"
