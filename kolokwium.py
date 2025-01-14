# Walidacja haseł

# Zaprogramuj funkcje które sprawdzą czy przekazany do nich ciąg znaków spełnia określone kryterium.
# Następnie zaimplementuj funkcję sprawdz_haslo, która zwróci True jeśli wszystkie kryteria są spełnione, w przeciwnym razie zwróci listę błędów.

# Kryteria:

# - Minimum 8 znaków,
# - Co najmniej jedna wielka litera,
# - Co najmniej jedna mała litera,
# - Co najmniej jedna cyfra.

# Program musi składać się z następujących funkcje:

# 1. `poprawna_dlugosc(h)` – zwraca `True`, jeśli hasło ma co najmniej 8 znaków.
# 2. `czy_cyfra(h)` – zwraca `True`, jeśli hasło zawiera cyfrę.
# 3. `czy_wielka_litera(h)` – zwraca `True`, jeśli hasło zawiera wielką literę.
# 4. `czy_mala_litera(h)` – zwraca `True`, jeśli hasło zawiera małą literę.
# 5. `sprawdz_haslo(h)` – zwraca `True`, jeśli wszystkie powyższe warunki są spełnione, w przeciwnym razie listę błędów.

# Na ocenę 3.0:
# Poprawna implementacja funkcji `poprawna_dlugosc` oraz `czy_cyfra`.

# Na ocenę 4.0:
# Poprawna implementacja funkcji `poprawna_dlugosc`, `czy_cyfra`,  `czy_wielka_litera` oraz `czy_mala_litera`.

# Na ocenę 5.0:
# Poprawna implementacja wszystkich funkcji.

# Przykład pełnego raportu:

# Podaj hasło do walidacji: abc
# ['Hasło jest za krótkie (min. 8 znaków).', 'Brakuje cyfry.', 'Brakuje wielkiej litery.']

# Kolejny przykład pełnego raportu:

# Podaj hasło do walidacji: Abc
# ['Hasło jest za krótkie (min. 8 znaków).', 'Brakuje cyfry.']

# Następny przykład pełnego raportu:

# Podaj hasło: Abc12345
# True


def poprawna_dlugosc(h):
    """Sprawdza, czy hasło ma co najmniej 8 znaków."""

    pass  # Zamiast słowa pass wpisz kod funkcji


def czy_cyfra(h):
    """Sprawdza, czy hasło zawiera co najmniej jedną cyfrę."""

    pass  # Zamiast słowa pass wpisz kod funkcji


def czy_wielka_litera(h):
    """Sprawdza, czy hasło zawiera co najmniej jedną wielką literę."""

    pass  # Zamiast słowa pass wpisz kod funkcji


def czy_mala_litera(h):
    """Sprawdza, czy hasło zawiera co najmniej jedną małą literę."""

    pass  # Zamiast słowa pass wpisz kod funkcji


def sprawdz_haslo(h):
    """Waliduje hasło na podstawie wszystkich kryteriów i zwraca raport w postaci LISTĘ błędów. 
    W przypadku braku błędów zwraca True.

    Lista możliwych błędów:

    Hasło jest za krótkie (min. 8 znaków).
    Brakuje cyfry.
    Brakuje wielkiej litery.
    Brakuje małej litery.

    """

    pass  # Zamiast słowa pass wpisz kod funkcji


if __name__ == '__main__':
    # Tu już nic nie musisz dopisywać
    haslo = input("Podaj hasło do walidacji: ")
    wynik = sprawdz_haslo(haslo)
    # Printowaie wyniku
    print(wynik)
