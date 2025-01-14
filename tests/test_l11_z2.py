import sys
import os
import pytest

# Dodaj ścieżkę do katalogu głównego projektu
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from l11.l11_z2 import wczytaj_plik

# Testy jednostkowe

def test_wczytaj_plik_istniejacy(tmp_path):
    # Utworzenie tymczasowego pliku
    nazwa_pliku = tmp_path / "testowy_plik.txt"
    zawartosc_pliku = "To jest testowa zawartość pliku."
    
    with open(nazwa_pliku, 'w') as f:
        f.write(zawartosc_pliku)
    
    # Sprawdzenie poprawności wczytywania istniejącego pliku
    wynik = wczytaj_plik(str(nazwa_pliku))
    assert wynik == zawartosc_pliku

    # Usunięcie pliku testowego po zakończeniu testu
    if nazwa_pliku.exists():
        os.remove(nazwa_pliku)

def test_wczytaj_plik_nieistniejacy():
    # Test dla pliku, który nie istnieje
    wynik = wczytaj_plik("nieistniejacy_plik.txt")
    assert wynik is None
