import sys
import os
import pytest
import random

# Dodaj ścieżkę do katalogu głównego projektu
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from l11.l11_z1 import lista_elementow

# Testy jednostkowe

def test_losowy_element_z_listy():
    losowy_element = random.choice(lista_elementow)
    # Sprawdzenie, czy wylosowany element należy do listy
    assert losowy_element in lista_elementow

def test_losowe_elementy_z_listy():
    losowe_elementy = random.choices(lista_elementow, k=3)
    # Sprawdzenie, czy lista ma długość 3
    assert len(losowe_elementy) == 3
    # Sprawdzenie, czy wszystkie elementy wylosowane znajdują się w oryginalnej liście
    for element in losowe_elementy:
        assert element in lista_elementow
