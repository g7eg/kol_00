import sys
import os
import pytest
from io import StringIO
from contextlib import redirect_stdout

# Dodaj ścieżkę do katalogu głównego projektu
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from l11.l11_z7 import Ksiazka, Biblioteka

def test_dodaj_ksiazke():
    biblioteka = Biblioteka()
    biblioteka.dodaj_ksiazke("Testowa Książka", "Testowy Autor", 2023)
    assert len(biblioteka.ksiazki) == 1
    assert biblioteka.ksiazki[0].tytul == "Testowa Książka"
    assert biblioteka.ksiazki[0].autor == "Testowy Autor"

def test_usun_ksiazke_o_tytule():
    biblioteka = Biblioteka()
    biblioteka.dodaj_ksiazke("Testowa Książka", "Testowy Autor", 2023)
    biblioteka.usun_ksiazke_o_tytule("Testowa Książka")
    assert len(biblioteka.ksiazki) == 0

def test_wypisz_zawartosc_biblioteki():
    biblioteka = Biblioteka()
    biblioteka.dodaj_ksiazke("Książka 1", "Autor 1", 2022)
    
    expected_output = ("Zawartość biblioteki:\n"
                       "'Książka 1' - Autor 1 (2022)\n")

    f = StringIO()
    with redirect_stdout(f):
        biblioteka.wypisz_zawartosc_biblioteki()
    output = f.getvalue()
    
    assert output == expected_output

def test_znajdz_ksiazke_autora():
    biblioteka = Biblioteka()
    biblioteka.dodaj_ksiazke("Książka A", "Autor X", 2021)
    biblioteka.dodaj_ksiazke("Książka B", "Autor X", 2020)
    
    expected_output = ("Książki autora 'Autor X':\n"
                       "'Książka A' - Autor X (2021)\n"
                       "'Książka B' - Autor X (2020)\n")

    f = StringIO()
    with redirect_stdout(f):
        biblioteka.znajdz_ksiazke_autora("Autor X")
    output = f.getvalue()
    
    assert output == expected_output

def test_znajdz_ksiazke_autora_brak():
    biblioteka = Biblioteka()
    
    expected_output = "Nie znaleziono książek autora 'Nieznany Autor'.\n"

    f = StringIO()
    with redirect_stdout(f):
        biblioteka.znajdz_ksiazke_autora("Nieznany Autor")
    output = f.getvalue()
    
    assert output == expected_output
