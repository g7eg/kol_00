import sys
import os
import pytest

# Dodaj ścieżkę do pliku kolokwium.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # noqa

from kolokwium import poprawna_dlugosc, czy_cyfra


def test_poprawna_dlugosc_mniej_niz_8_znakow_cyfry():
    assert poprawna_dlugosc("123") == False  # Hasło ma mniej niż 8 znaków


def test_poprawna_dlugosc_mniej_niz_8_znakow_litery():
    assert poprawna_dlugosc("abc") == False  # Hasło ma mniej niż 8 znaków


def test_poprawna_dlugosc_mniej_niz_8_znakow_cyfry_i_litery():
    assert poprawna_dlugosc("123asd") == False  # Hasło ma mniej niż 8 znaków


def test_poprawna_dlugosc_wiecej_niz_8_znakow_cyfry():
    # Hasło ma więcej niż 8 znaków
    assert poprawna_dlugosc("1234567890") == True


def test_poprawna_dlugosc_wiecej_niz_8_znakow_litery():
    # Hasło ma więcej niż 8 znaków
    assert poprawna_dlugosc("asdrfgtswessdsd") == True


def test_poprawna_dlugosc_wiecej_niz_8_znakow_cyfry_i_litery():
    # Hasło ma więcej niż 8 znaków
    assert poprawna_dlugosc("asdrfgtswes12312412") == True


def test_poprawna_dlugosc_rowno_8_znakow_cyfry():
    assert poprawna_dlugosc("12345678") == True  # Hasło ma 8 znaków


def test_poprawna_dlugosc_rowno_8_znakow_litery():
    assert poprawna_dlugosc("abcdefgh") == True  # Hasło ma 8 znaków


def test_poprawna_dlugosc_rowno_8_znakow_cyfry_i_litery():
    assert poprawna_dlugosc("1234asdf") == True  # Hasło ma 8 znaków


def test_poprawna_dlugosc_zerowa_dlugosc():
    assert poprawna_dlugosc("") == False  # Hasło ma 8 znaków


def test_czy_cyfra_jedna_cyfra():
    assert czy_cyfra("abc1") == True  # Hasło zawiera cyfrę


def test_czy_cyfra_wiele_cyfra():
    assert czy_cyfra("abc11231231") == True  # Hasło zawiera cyfrę


def test_czy_cyfra_cyfra_na_poczatku():
    assert czy_cyfra("1abc") == True  # Hasło zawiera cyfrę


def test_czy_cyfra_na_koncu():
    assert czy_cyfra("abc1") == True  # Hasło zawiera cyfrę


def test_czy_cyfra_w_srodku():
    assert czy_cyfra("a4c") == True  # Hasło zawiera cyfrę


def test_czy_cyfra_brak_cyfry():
    assert czy_cyfra("abcasdasdagdasdas") == False  # Hasło zawiera cyfrę


def test_czy_cyfra_brak_cyfry_na_poczatku_male_litery():
    assert czy_cyfra("abcasdasdagdasdas") == False  # Hasło zawiera cyfrę


def test_czy_cyfra_brak_cyfry_na_koncu_male_litery():
    assert czy_cyfra("abcasdasdagdasdas") == False  # Hasło zawiera cyfrę


def test_czy_cyfra_brak_cyfry_na_poczatku_wielkie_litery():
    assert czy_cyfra("ABCDFGRKSKKDSKDKSK") == False  # Hasło zawiera cyfrę


def test_czy_cyfra_brak_cyfry_na_koncu_wielkie_litery():
    assert czy_cyfra("ABCDFGRKSKKDSKDKSK") == False  # Hasło zawiera cyfrę
