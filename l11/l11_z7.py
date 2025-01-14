# ## Lista 11 Zad. 7
# ### 3pkt + 2pkt
# ta część za 3 punkty:
# Doklasy książka z poprzedniego zadania dopisać klasę biblioteka która będzie składać się z obiektów klasy książka. Do przechowywania książek w klasie biblioteka użyć zwykłej listy.
# Klasa biblioteka powinna posiadać następujące metody (taka funkcja należąca do klasy):
# - dodaj_ksiazke() - dodaje książkę do biblioteki
# - usun_ksiazke_o_tytule() - usuwa książkę o wskazanym tytule z biblioteki
# - wypisz_zawartosc_biblioteki() - wypisuje wszystkie książki w bibliotece
# - znajdz_ksiazke_autora() - wypisuje wszystkie książki wskazanego autora

# dalsza treść na kolejne 2 pkt:
# Wykonać menu (utwórz runkcję menu()) które pozwoli wykorzystać powyższe klasy i daje użytkownikowi możliwość tworzenia książek i korzystania z biblioteki. Pamiętać, że program powinien działać do czasu aż użytkownik nie wybierze z menu opcji do zamknięcia programu. Do tego celu można wykorzystać pętlę while.


# Podpowiedź:
# Bezpośrednie tworzenie obiektu klasy Biblioteka w programie może powodować problemy z testami jednostkowymi. Aby tego uniknąć utwórz obiekt klasy biblioteka w funkcji menu().
# ```python
# if __name__ == "__main__":
#     menu()
# ```

# > [!TIP]
# > Przykład:
# --- MENU ---
# 1. Dodaj książkę
# 2. Usuń książkę o tytule
# 3. Wypisz zawartość biblioteki
# 4. Znajdź książki autora
# 5. Wyjście
# Wybierz opcję (1-5): 1
# Podaj tytuł książki: Władca Pierścieni
# Podaj autora książki: J.R.R. Tolkien
# Podaj rok wydania książki: 1954
# Książka 'Władca Pierścieni' dodana do biblioteki.

# --- MENU ---
# 1. Dodaj książkę
# 2. Usuń książkę o tytule
# 3. Wypisz zawartość biblioteki
# 4. Znajdź książki autora
# 5. Wyjście
# Wybierz opcję (1-5): 3
# Zawartość biblioteki:
# 'Władca Pierścieni' - J.R.R. Tolkien (1954)

# --- MENU ---
# 1. Dodaj książkę
# 2. Usuń książkę o tytule
# 3. Wypisz zawartość biblioteki
# 4. Znajdź książki autora
# 5. Wyjście
# Wybierz opcję (1-5): 2
# Podaj tytuł książki do usunięcia: Władca Pierścieni
# Książka 'Władca Pierścieni' została usunięta z biblioteki.

# --- MENU ---
# 1. Dodaj książkę
# 2. Usuń książkę o tytule
# 3. Wypisz zawartość biblioteki
# 4. Znajdź książki autora
# 5. Wyjście
# Wybierz opcję (1-5): 3
# Biblioteka jest pusta.

# --- MENU ---
# 1. Dodaj książkę
# 2. Usuń książkę o tytule
# 3. Wypisz zawartość biblioteki
# 4. Znajdź książki autora
# 5. Wyjście
# Wybierz opcję (1-5):
# [...]
