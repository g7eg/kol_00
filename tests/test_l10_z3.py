import sys
import os
import pytest

# Dodaj ścieżkę do katalogu głównego projektu
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from l10.l10_z3 import czy_liczba_pierwsza, generuj_nieparzyste_liczby_pierwsze

def test_czy_liczba_pierwsza():
    assert czy_liczba_pierwsza(2) == True
    assert czy_liczba_pierwsza(3) == True
    assert czy_liczba_pierwsza(4) == False
    assert czy_liczba_pierwsza(29) == True
    assert czy_liczba_pierwsza(100) == False

def test_generuj_nieparzyste_liczby_pierwsze():
    assert set(generuj_nieparzyste_liczby_pierwsze()) == {3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
