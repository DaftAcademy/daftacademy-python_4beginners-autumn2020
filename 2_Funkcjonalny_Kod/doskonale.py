# Napisz funkcję doskonale, ktora zwraca listę wszystich liczb doskonałych
# mniejszych bądź równych zadanemu n
# Wewnątrz, stwórz funkcję suma_dzielnikow, która zwraca sumę
# dzielników właściwych zadanej liczby
def suma_dzielnikow(k):
    return sum(
        [
            i
            for i
            in range(1, k // 2 + 1)
            if k % i == 0
        ]
    )


def doskonale(n):
    return [
        k
        for k
        in range(1, n + 1)
        if k == suma_dzielnikow(k)
    ]


def doskonale_v1(n):
    if n< 1:
        return False

    perfect_sum = 0
    for i in range(1,n):
        if n%i==0:
            perfect_sum += i

    return perfect_sum == n

def doskonale1(n):
    for i in range(0, n+1):
      if doskonale_v1(i):
        l = []
        l.append(i)
        print(l)


assert doskonale(3) == []
assert doskonale(30) == [6, 28]
assert doskonale(300) == [6, 28]
assert doskonale(3000) == [6, 28, 496]


print(doskonale1(300))