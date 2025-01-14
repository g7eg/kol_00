import sys
import os
import pytest

# Dodaj ścieżkę do katalogu głównego projektu
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from l10.l10_z4 import oblicz_silnie

def test_oblicz_silnie_dla_liczb_dodatnich():
    assert oblicz_silnie(5) == 120
    assert oblicz_silnie(0) == 1
    assert oblicz_silnie(1) == 1

def test_oblicz_silnie_dla_liczby_ujemnej():
    assert oblicz_silnie(-5) is None
