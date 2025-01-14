import sys
import os
import pytest

# Dodaj ścieżkę do pliku kolokwium.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # noqa

from kolokwium import czy_mala_litera, czy_wielka_litera


def test_czy_wielka_litera():
    assert czy_wielka_litera("abcA123") == True  # Hasło zawiera wielką literę
    # Hasło nie zawiera wielkiej litery
    assert czy_wielka_litera("abcdefg") == False
    assert czy_wielka_litera("1234A") == True  # Hasło zawiera wielką literę
    # Hasło nie zawiera wielkiej litery
    assert czy_wielka_litera("1234") == False


def test_czy_mala_litera():
    assert czy_mala_litera("ABC123") == False  # Hasło nie zawiera małą literę
    # Hasło nie zawiera małej litery
    assert czy_mala_litera("ABCDEFG") == False
    assert czy_mala_litera("1aB2") == True  # Hasło zawiera małą literę
    assert czy_mala_litera("1234") == False  # Hasło nie zawiera małej litery
