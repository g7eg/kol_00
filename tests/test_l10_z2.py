import sys
import os
import pytest

# Dodaj ścieżkę do katalogu głównego projektu
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from l10.l10_z2 import czy_liczba_doskonala

def test_liczba_doskonala():
    assert czy_liczba_doskonala(6) == True
    assert czy_liczba_doskonala(28) == True
    assert czy_liczba_doskonala(496) == True

def test_liczba_nie_doskonala():
    assert czy_liczba_doskonala(12) == False
    assert czy_liczba_doskonala(18) == False
    assert czy_liczba_doskonala(100) == False

def test_male_liczby():
    assert czy_liczba_doskonala(1) == False
    assert czy_liczba_doskonala(2) == False
    assert czy_liczba_doskonala(3) == False
