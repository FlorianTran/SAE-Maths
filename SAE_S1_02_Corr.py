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
