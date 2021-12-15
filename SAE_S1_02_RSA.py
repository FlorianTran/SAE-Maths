### RAS ###
import math
import random

# ===== Q 1.1 ====== #


def list_prim(n):
    """
    Renvoie un tableau de tous les nombres premiers entre 0 et n
        1 entrée n
    renvoie une tableau de tous les nombres premiers
    """
    result = []
    if n <= 1:
        return result
    for num in range(2, n+1):
        if is_prim(num):
            result.append(num)
    return result


def is_prim(n):
    """
    Renvoie si nombre n est enier ou pas
        1 entrée n
    retourn vrai ou faux
    """
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# ===== Q 1.2 ====== #


def pgcd(a, b):
    """
    Pgcd
        prend en entrée 2 entiers:
            a et b
        renvoie 2 entiers b et r
        d le plus grand diviseur commun
        r le reste
    """
    r = a % b
    if r == 0:
        d = b
        return d
    return pgcd(b, r)


def extended_gcd(a, b):
    """
    Algorithme d'Euclide
        Prend en entrée 2 entiers:
            a et b
        renvoie 3 entiers d,u,v
        d est le pgcd des 2 entier a et b
        u et v sont les coéficient de Bezout
    """
    u0 = 1
    u1 = 0
    v0 = 0
    v1 = 1
    q = a//b
    r = a % b
    while r != 0:
        u2 = u0-q*u1
        v2 = v0-q*v1
        u0 = u1
        v0 = v1
        u1 = u2
        v1 = v2
        a = b
        b = r
        q = a//b
        r = a % b
    return b, u1, v1


# ===== Q 1.3 ====== #


def key_creation():
    """
    Key_creation
        créer une clé public, n une partie de clé publique et une clé privé
    """
    tabPrim = list_prim(1000)

    p = tabPrim[random.randrange(len(tabPrim))]
    q = tabPrim[random.randrange(len(tabPrim))]
    n = p * q
    phiN = (p-1)*(q-1)

    # tous premier x > phiN valide pgcd(x, phiN) = 1
    pub = tabPrim[random.randrange(len(tabPrim))]
    while pgcd(pub, phiN) != 1:
        pub = tabPrim[random.randrange(len(tabPrim))]
    _, priv, _ = extended_gcd(pub, phiN)
    return n, pub, priv

# ===== Q 1.4 ===== #


def convert_msg(msg):
    """
    Prend en entrée un message textuel
    Il est convertit grace à la table ascii, chaque charractère est convertit en
    un nombre à trois chiffre renvoie une lite de nombre, groupé 4 à 4 pour évité
    les attaques fréquentielles et pour ne pas avoir besoin d'un n trop grand
    """
    converted_msg = ""
    converted_msg_tab = []

    for character in msg:
        converted_msg += str(ord(character)).zfill(3)

    piv1, piv2 = 0, 4
    while len(converted_msg) % piv2 != 0:
        converted_msg = converted_msg + "0"
    while piv2 <= len(converted_msg):
        converted_msg_tab.append(converted_msg[piv1: piv2])
        piv1, piv2 = piv2, piv2 + 4
    return converted_msg_tab


def encryption_msg(n, pub, msg):
    """
    encryption_msg:
        prend en entrée 2 entier (n et pub qui sont la clef publique)
        et 1 liste d'entier (msg qui contient le message converti en ASCII)
    renvoie le message chiffré(crypted_msg)
    """
    crypted_msg = []
    for i in msg:
        crypted_msg.append(int(i)**pub % n)
    return crypted_msg

# ===== Q 1.5 ===== #


def decryption_msg(n, priv, msg):
    """
    decryption_msg:
        prend en entrée 2 entier ( n et priv qui sont la clé privée)
        et une liste d'entier (msg qui contient le message chiffré)
        renvoie le message déchiffré, en le passant d'un format ascii à textuel
        grace a une autre fonction
    """
    decrypted_msg_ascii = []
    decrypted_msg = []

    if priv < 0:
        priv = -priv
        for i in range(0, len(msg), 1):
            tmp = msg[i]**priv % n
            _, tmp2, _ = extended_gcd(tmp, n)
            decrypted_msg_ascii.append(tmp2)
    else:
        for i in msg:
            decrypted_msg_ascii.append(i**priv % n)

        for i in range(0, len(decrypted_msg_ascii), 1):
            tmp = str(decrypted_msg_ascii[i])
            tmp = tmp.zfill(4)
            decrypted_msg.append(tmp)
    return decrypted_msg


def reconvert_msg(decrypted_msg_ascii):
    """
    reconvert_msg
        prends en entrée un message déchiffré en ASCII
        convertit ce message en char
        renvoie le message en string
    """
    decrypted_msg_ascii = ''.join(decrypted_msg_ascii)
    decrypted_msg = ""
    piv1, piv2 = 0, 3

    while piv2 <= len(decrypted_msg_ascii):
        tmp = chr(int(decrypted_msg_ascii[piv1:piv2]))
        if tmp != "000":
            decrypted_msg = decrypted_msg + tmp
        piv1, piv2 = piv2, piv2 + 3

    return decrypted_msg


""" for i in range(0,1000,1):
    n,pub,priv=key_creation()
    while priv < 0 or n < 10000:
        n,pub,priv=key_creation() """
""" print(convert_msg("Bonjour les amis, est - ce"))
    print(encryption_msg(n, pub, convert_msg("Bonjour les amis, est - ce")))
    print(decryption_msg(n, priv, encryption_msg(n, pub, convert_msg("Bonjour les amis, est - ce")))) """
""" print(n,pub,priv)
    msg = reconvert_msg(decryption_msg(n, priv, encryption_msg(n, pub, convert_msg("Bonjour les amis, est - ce"))))
    print(msg) """
