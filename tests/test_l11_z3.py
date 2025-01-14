import sys
import os
import pytest

# Dodaj ścieżkę do katalogu głównego projektu
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from l11.l11_z3 import zlicz_wystapienia_slowo_kot

# Testy jednostkowe

def test_zlicz_wystapienia_slowo_kot_istniejacy_plik_wielkie_i_male_litery(tmp_path):
    # Tworzenie tymczasowego pliku
    nazwa_pliku = tmp_path / "tekst.txt"
    zawartosc_pliku = "Kot jest bardzo fajnym zwierzęciem. kot to też zwierzę domowe. Kot lubi mleko."

    with open(nazwa_pliku, 'w') as f:
        f.write(zawartosc_pliku)

    # Sprawdzenie liczby wystąpień słowa "kot"
    wynik = zlicz_wystapienia_slowo_kot(str(nazwa_pliku))
    assert wynik == 3

    # Usunięcie pliku testowego po zakończeniu testu
    if nazwa_pliku.exists():
        os.remove(nazwa_pliku)

def test_zlicz_wystapienia_slowo_kot_nieistniejacy_plik():
    # Test dla pliku, który nie istnieje
    wynik = zlicz_wystapienia_slowo_kot("nieistniejacy_plik.txt")
    assert wynik is None

def test_zlicz_wystapienia_slowo_kot_brak_wystapien(tmp_path):
    # Tworzenie tymczasowego pliku bez słowa "kot"
    nazwa_pliku = tmp_path / "tekst.txt"
    zawartosc_pliku = "Pies jest wiernym przyjacielem człowieka."

    with open(nazwa_pliku, 'w') as f:
        f.write(zawartosc_pliku)

    # Sprawdzenie liczby wystąpień słowa "kot"
    wynik = zlicz_wystapienia_slowo_kot(str(nazwa_pliku))
    assert wynik == 0

    # Usunięcie pliku testowego po zakończeniu testu
    if nazwa_pliku.exists():
        os.remove(nazwa_pliku)
