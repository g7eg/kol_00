# Walidacja haseł

# Napisz program, który sprawdzi, czy hasło wprowadzone przez użytkownika spełnia określone kryteria.

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

# Podaj hasło: abc
# Hasło nie spełnia następujących wymagań:
# - Brakuje wielkiej litery.
# - Brakuje cyfry.
# - Hasło jest za krótkie (min. 8 znaków).

def poprawna_dlugosc(h):
    """Sprawdza, czy hasło ma co najmniej 8 znaków."""

    # pass  # Zamiast słowa pass wpisz kod funkcji

    return len(h) >= 8


def czy_cyfra(h):
    """Sprawdza, czy hasło zawiera co najmniej jedną cyfrę."""

    # pass  # Zamiast słowa pass wpisz kod funkcji

    return any(c.isdigit() for c in h)


def czy_wielka_litera(h):
    """Sprawdza, czy hasło zawiera co najmniej jedną wielką literę."""

    # pass  # Zamiast słowa pass wpisz kod funkcji

    return any(c.isupper() for c in h)


def czy_mala_litera(h):
    """Sprawdza, czy hasło zawiera co najmniej jedną małą literę."""

    # pass  # Zamiast słowa pass wpisz kod funkcji

    return any(c.islower() for c in h)


def sprawdz_haslo(h):
    """Waliduje hasło na podstawie wszystkich kryteriów i zwraca raport w postaci LISTĘ błędów. 
    W przypadku braku błędów zwraca True.

    Lista możliwych błędów:

    Hasło jest za krótkie (min. 8 znaków).
    Brakuje cyfry.
    Brakuje wielkiej litery.
    Brakuje małej litery.

    """

    # pass  # Zamiast słowa pass wpisz kod funkcji

    raport = []

    if not poprawna_dlugosc(h):
        raport.append("Hasło jest za krótkie (min. 8 znaków).")

    if not czy_cyfra(h):
        raport.append("Brakuje cyfry.")

    if not czy_wielka_litera(h):
        raport.append("Brakuje wielkiej litery.")

    if not czy_mala_litera(h):
        raport.append("Brakuje małej litery.")

    return raport if raport else True


if __name__ == '__main__':
    # Tu już nic nie musisz dopisywać
    haslo = input("Podaj hasło do walidacji: ")
    wynik = sprawdz_haslo(haslo)
    print(wynik)
