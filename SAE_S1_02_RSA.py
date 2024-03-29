### RAS ###
import math
import random

# ===== Q 1.1 ====== #


def list_prim(n):
    """
    prend en entrée un entier n
    renvoie un tableau de tous les nombres premiers entre 0 et n
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
    prend en entrée
    renvoie si nombre n est un nombre entier ou pas
    """
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# ===== Q 1.2 ====== #


def pgcd(a, b):
    """
    prend en entrée 2 entiers:a et b
    renvoie 2 entiers b et r: b le plus grand diviseur commun et r le reste
    """
    r = a % b
    if r == 0:
        d = b
        return d
    return pgcd(b, r)


def extended_gcd(a, b):
    """
    prend en entrée 2 entiers:a et b
    renvoie 3 entiers d,u,v:
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
créer une clé public, n une partie de clé publique et une clé privé, la fonction les renvoie. (On ne veux pas de n < 10000 car nous pour
crypter n doit etre supérieur à la valeur du message or nous avons des message de 4 chiffres et donc msg < 10000) nous avons aussi fait
le choix de ne pas prendre des priv avec une valeur négative car elle posait trop problème malgré le fait que l'on puisse prendre son inverse
avec extended_gcp etc.s
"""
    tabPrim = list_prim(1000)
    p = tabPrim[random.randrange(len(tabPrim))]
    q = tabPrim[random.randrange(len(tabPrim))]
    while p == q:
        p = tabPrim[random.randrange(len(tabPrim))]
        q = tabPrim[random.randrange(len(tabPrim))]

    n = p * q
    phiN = (p-1)*(q-1)

    # tous premier x > phiN valide pgcd(x, phiN) = 1
    pub = tabPrim[random.randrange(len(tabPrim))]

    while pgcd(pub, phiN) != 1:
        pub = tabPrim[random.randrange(len(tabPrim))]
    _, priv, _ = extended_gcd(pub, phiN)

    while priv < 0 or n < 10000:
        n, pub, priv = key_creation()

    return n, pub, priv


# ===== Q 1.4 ===== #


def convert_msg(msg):
    """
    prend en entrée un message textuel,
    il est convertit grace à la table ASCII, chaque charractère est convertit en
    un nombre à trois chiffre renvoie une tableau de nombre, groupé 4 à 4 pour évité
    les attaques fréquentielles et pour ne pas avoir besoin d'un n trop grand (n >= 10000)
    renvoie le message converti
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
    prend en entrée 2 entier (n et pub qui sont la clef publique)
    et 1 tableau d'entier (msg qui contient le message converti en ASCII)
    renvoie le message chiffré(crypted_msg)
    """
    crypted_msg = []
    for i in msg:
        crypted_msg.append(int(i)**pub % n)
    return crypted_msg

# ===== Q 1.5 ===== #


def decryption_msg(n, priv, msg):
    """
    prend en entrée 2 entier ( n et priv qui sont la clé privée)
    et un tableau d'entier (msg qui contient le message chiffré)
    renvoie le message déchiffré, en le passant d'un format ascii à textuel
    grace a une autre fonction
    """
    decrypted_msg_ascii = []
    decrypted_msg = []

    # nous avons abandonné l'idée de prendre des clé privé négatif car cela créer certain problème de temps en temps
    """ if priv < 0:
        priv = -priv
        for i in range(0, len(msg), 1):
            tmp = msg[i]**priv % n
            _, tmp2, _ = extended_gcd(tmp, n)
            decrypted_msg_ascii.append(tmp2) """

    for i in msg:
        decrypted_msg_ascii.append(i**priv % n)

    for i in range(0, len(decrypted_msg_ascii), 1):
        tmp = str(decrypted_msg_ascii[i])
        tmp = tmp.zfill(4)
        decrypted_msg.append(tmp)
    return decrypted_msg


def reconvert_msg(decrypted_msg_ascii):
    """
    prend en entrée un message déchiffré en ASCII
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
