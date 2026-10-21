def uniao(a, b):
    r = []
    for i in range(0, len(a)):
        r.append(a[i])

    for j in range(0, len(b)):
        existe = False
        for i in range(0, len(a)):
            if a[i] == b[j]:
                existe = True
        if existe == False:
            r.append(b[j])

    return r


def intersecao(a, b):
    r = []

    for i in range(0, len(a)):
        for j in range(0, len(b)):
            if a[i] == b[j] and a[i] not in r:
                r.append(a[i])

    return r

def complemento(a, u):
    r = []
    for i in range(0, len(u)):
        existe = False

        for j in range(0, len(a)):
            if u[i] == a[j]:
                existe = True

        if existe == False:
            r.append(u[i])

    return r

u = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [1, 2, 3, 5, 8]
b = [2, 4, 5, 7]
c = [1, 4, 6, 8, 10]

print("1 =", uniao(a, b))
print("2 =", intersecao(a, b))
print("3 =", intersecao(a, c))
print("4 =", complemento(a, u))