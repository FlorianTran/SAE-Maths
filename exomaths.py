# 7.1a
def quotient(a, b):
    div = 0
    res = a
    while a > b:
        a = a-b
        div = div+1
    res = a
    return res, div


def qotrem(a, b):
    q = 0
    r = a
    while r >= b:
        q = q+1
        r = r-b
    return q, r

# 7.1b


def euclide(a, b):
    if a > b:
        q = 0
        r = a
        while r >= b:
            q = q+1
            r = r-b
        if r == 0:
            return b
        else:
            a = b
            b = r
    else:
        print("erreur,a doit être plus grand que b")
    return b


def pgcd_it(a, b):
    r = qotrem(a, b)[1]
    while r != 0:
        a = b
        b = r
        r = qotrem(a, b)[1]
    return b


def pgcd_r(a, b):
    r = qotrem(a, b)[1]
    if r == 0:
        return b
    return pgcd_r(b, r)


def bezout(a, b):
    u0 = 1
    u1 = 0
    v0 = 0
    v1 = 1
    q, r = qotrem(a, b)
    while r != 0:
        u2 = u0-q*u1
        v2 = v0-q*v1
        u0 = u1
        v0 = v1
        u1 = u2
        v1 = v2
        a = b
        b = r
        q, r = qotrem(a, b)
    return b, u1, v1
# 7.1c
# 9


def conversion(c, n):
    l = []
    res, div = quotient(c, n)
    l.append(res)
    while div > 0:
        res, div = quotient(div, n)
        l.append(res)
    return list(reversed(l))


def conversion_inverse(l, n):
    somme = 0
    i = 0
    s = len(l)-1
    while i < len(l):
        somme = somme+l[i]*n**s
        i = i+1
        s = s-1
    return somme


def revr_base_10(nombre, base):
    acc = 0
    for chiffre in nombre:
        acc = acc*base+chiffre
    return acc

# 10


def exp_mod(a, k, n):
    bin_k = conversion(k, 2)
    tab_puissance = [a]
    for i in range(len(bin_k)):
        tmp = tab_puissance[-1]
        tmp = tmp*tmp
        tmp = qotrem(tmp, n)[1]
        tab_puissance.append(tmp)
        tab_puissance = list(reversed(tab_puissance))
    return tab_puissance
