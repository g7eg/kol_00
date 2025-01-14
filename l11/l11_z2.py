# ## Lista 11 Zad. 2
# 2pkt
# Napisać funkcję 'wczytaj_plik(nazwa_pliku)', która obsługuje otwieranie pliku do wczytywania danych.
# Jako argument przyjmuje nazwę pliku. Zapytać użytkownika o nazwę pliku, który chce otworzyć do wczytania.
# Jeśli plik nie istnieje wypisać mu odpowiedni komunikat.
# Jeśli plik istnieje wczytaj całą jego zawartość i zwróć jako wynik funkcji a następnie wyświetl ją na ekrania.
# Skorzystać z wiedzy dotyczącej obsługi wyjątków.

# Podpowiedź:
# Podając nazwę pliku przeszukiwany domyślnie jest główny katalog, został tam utworzony 'przykladowy_plik.txt'.
# Jeżeli chcesz otworzyć plik znajdujący się w innym katalogu musisz podać do niego ścieżkę.

# Podpowiedź:
# Pamiętaj o wykorzystaniu deklaracji:
# ```python
# if __name__ == "__main__":
#     # Pobranie nazwy pliku
#     # Wywołanie funkcji z przekazaniem parametru
# ```

# > [!TIP]
# > Przykład:
# Podaj nazwę pliku do wczytania: przykladowy_plik.txt
# Zawartość pliku wczytana pomyślnie.
# Zawartość pliku:
# Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym.
# Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki.
# Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym.
# Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum,
# a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych,
# jak Aldus PageMaker
