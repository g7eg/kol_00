import sys
import os
import pytest
from io import StringIO
from contextlib import redirect_stdout

# Dodaj ścieżkę do katalogu głównego projektu
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from l11.l11_z5 import zlicz_unikalne_slowa

# Funkcja pomocnicza do tworzenia plików testowych
def stworz_testowy_plik(nazwa_pliku, zawartosc):
    with open(nazwa_pliku, 'w', encoding='utf-8') as plik:
        plik.write(zawartosc)

# Funkcja pomocnicza do odczytania zawartości pliku
def odczytaj_plik(nazwa_pliku):
    with open(nazwa_pliku, 'r', encoding='utf-8') as plik:
        return plik.read()

# Testy jednostkowe

def test_zlicz_unikalne_slowa():
    # Przygotowanie danych testowych
    nazwa_pliku_wejsciowego = 'test_input.txt'
    nazwa_pliku_wyjsciowego = 'test_output.txt'
    zawartosc = "Kot kot pies pies pies"
    
    stworz_testowy_plik(nazwa_pliku_wejsciowego, zawartosc)
    
    # Wywołanie funkcji
    zlicz_unikalne_slowa(nazwa_pliku_wejsciowego, nazwa_pliku_wyjsciowego)
    
    # Sprawdzenie wyników
    wynik = odczytaj_plik(nazwa_pliku_wyjsciowego)
    oczekiwany_wynik = "kot: 2\npies: 3\n"
    
    assert wynik == oczekiwany_wynik
    
    # Usunięcie plików testowych
    os.remove(nazwa_pliku_wejsciowego)
    os.remove(nazwa_pliku_wyjsciowego)

def test_plik_nie_istnieje():
    nazwa_pliku_wejsciowego = 'nie_istnieje.txt'
    nazwa_pliku_wyjsciowego = 'wyniki_tmp.txt'
    
    # Przechwycenie wyjścia funkcji
    f = StringIO()
    with redirect_stdout(f):
        zlicz_unikalne_slowa(nazwa_pliku_wejsciowego, nazwa_pliku_wyjsciowego)
    output = f.getvalue().strip()

    # Sprawdzenie, czy wyświetlono odpowiedni komunikat
    assert output == f"Plik {nazwa_pliku_wejsciowego} nie istnieje."
    
    # Usunięcie pliku wynikowego, jeśli został utworzony
    if os.path.exists(nazwa_pliku_wyjsciowego):
        os.remove(nazwa_pliku_wyjsciowego)
