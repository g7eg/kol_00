import sys
import os
import pytest

# Dodaj ścieżkę do pliku kolokwium.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # noqa

from kolokwium import sprawdz_haslo


def test_sprawdz_haslo():
    assert sprawdz_haslo(
        "abc12345") == ['Brakuje wielkiej litery.']
    assert sprawdz_haslo("Abc12345") == True
