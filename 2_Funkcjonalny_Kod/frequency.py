import re
from collections import Counter

# Napisz funkcję letter_frequency, która przyjmuje jako argument string.
# Dla podanego stringa funkcja musi zliczyć ile razy wystąpiła każda litera z alfabetu łacińskiego.
# Zwróc wynik jako słownik wartości ile razy wystąpiła każda litera, gdzie klucz
# to występująca litera a wartścią jest liczba jej wystąpień.


def letter_frequency(text=None):
    if not text:
        return {}
    return dict(Counter("".join(re.findall("[a-zA-Z]+", text))))


print(letter_frequency("Mateusz ;;;';'- maąteusz"))

assert letter_frequency("Aasd---=-=-\\mjofw sad e") == {
    "A": 1,
    "a": 2,
    "s": 2,
    "d": 2,
    "m": 1,
    "j": 1,
    "o": 1,
    "f": 1,
    "w": 1,
    "e": 1,
}
assert letter_frequency("DaftCode") == {
    "D": 1,
    "a": 1,
    "f": 1,
    "t": 1,
    "C": 1,
    "o": 1,
    "d": 1,
    "e": 1,
}

napis = input("Podaj napis: ")


def letter_frequency1(napis):
    frequency = {}
    for letter in napis:
        keys = frequency.keys()
        if (
            letter == "ą"
            or letter == "ę"
            or letter == "ć"
            or letter == "ł"
            or letter == "ń"
            or letter == "ó"
            or letter == "ś"
            or letter == "ż"
            or letter == "ź"
        ):
            continue
        if letter in keys:
            frequency[letter] += 1
        else:
            frequency[letter] = 1
    return print(frequency)


print(letter_frequency1(napis))
