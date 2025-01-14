import sys
import os
import pytest

# Dodaj ścieżkę do katalogu głównego projektu
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from l11.l11_z4 import polacz_listy

# Testy jednostkowe

def test_polacz_listy_z_duplikatami():
    lista1 = [1, 2, 3, 4]
    lista2 = [3, 4, 5, 6]
    lista3 = [6, 7, 8]
    wynik = polacz_listy(lista1, lista2, lista3)
    assert wynik == [1, 2, 3, 4, 5, 6, 7, 8]

def test_polacz_listy_bez_duplikatow():
    lista1 = [1, 2, 3]
    lista2 = [4, 5, 6]
    wynik = polacz_listy(lista1, lista2)
    assert wynik == [1, 2, 3, 4, 5, 6]

def test_polacz_listy_pusta_lista():
    lista1 = []
    lista2 = [1, 2, 3]
    wynik = polacz_listy(lista1, lista2)
    assert wynik == [1, 2, 3]

def test_polacz_listy_jedna_lista():
    lista1 = [1, 2, 2, 3, 4]
    wynik = polacz_listy(lista1)
    assert wynik == [1, 2, 3, 4]

def test_polacz_listy_brak_argumentow():
    wynik = polacz_listy()
    assert wynik == []
