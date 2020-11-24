# Napisz funkcję fold.
# Funkcja ma na celu mnożenie kolejnych par elementów zadanych list i
# zwrócenie listy iloczynów kolejnych par.
# Jeżeli listy wejściowe są nierówne, na ostatnich pozycjach listy wyjściowej
# powinny znaleźć się 0. Tyle 0, ile jest różnicy między listami.

def fold(a=None, b=None):
    if not a:
        a = []
    if not b:
        b = []

    res = [_a * _b for _a, _b in zip(a, b)]
    diff = abs(len(a) - len(b))
    res.extend([0] * diff)
    return res


def fold1(array1, array2):
    list = []
    if type(array1) == type(None) and type(array2) == type(None):
        return list
    if type(array1) == type(array2) and len(array1) == len(array2):
        for num1, num2 in zip(array1, array2):
            list.append(num1 * num2)
        return list
    if type(array1) == type(list):
        for x in range(len(array1)):
            array1[x] = 0
        return array1
    else:
        if type(array2) == type(list):
            for x in range(len(array2) + 1):
                array2[x] = 0
            return array2


def fold2(list_a, list_b):
    if len(list_a) == list_b.len():
        for i in list_b.len():
            result[i] = list_a[i] * list_b[i]
        return result
    elif list_a.len() > list_b.len():
        n = list_a.len() - list_b.len()
        for i in list_b.len():
            result[i] = list_a[i] * list_b[i]
            result.append([0] * n)
            return result
    else:
        n = list_b.len() - list_a.len()
        for i in list_b.len():
            result[i] = list_a[i] * list_b[i]
            result.append([0] * n)
            return result


assert fold(None, None) == []
assert fold([1, 2, 3], [1, 2, 3]) == [1, 4, 9]
assert fold([1, 2], [1, 2, 3]) == [1, 4, 0]
assert fold(None, [1, 2, 3]) == [0, 0, 0]
assert fold([1, 2, 3], None) == [0, 0, 0]


print(fold1([1, 2], [1, 2, 3]))
print(fold2([1, 2], [1, 2, 3]))
