### RAS ###
import math
import random

# ===== Q 1.1 ====== #


def list_prim(n):
    """
    Renvoie un tableau de tous les nombres premiers entre 0 et n
        1 entrée n
    retourne une tableau de tous les nombres premiers
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


def extended_gcd(a, b):
    """
    Algorithme d'Euclide
        Prend en entrée 2 entiers:
            a et b
        retourne 3 entiers d,u,v
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


def pgcd(a, b):
    """
    Pgcd
        prend en entrée 2 entiers:
            a et b
        retourne 2 entiers b et r
        b le plus grand diviseur commun
        r le reste
    """
    r = a % b
    if r == 0:
        return b
    return pgcd(b, r)


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
    Il est convertit grace à la table ascii, chaque charractère est convertit en un nombre à trois chiffre
    renvoie une lite de nombre, groupé 4 à 4 pour évité les attaques fréquentielles et pour ne pas avoir besoin d'un n trop grand
    """
    converted_msg = ""
    converted_msg_tab = []
    t = 4

    for character in msg:
        tmp = str(ord(character))
        tmp = tmp.zfill(3)
        converted_msg += tmp

    for i in range(t, len(converted_msg), t):
        converted_msg_tab.append(converted_msg[(i-t): i])
    if len(converted_msg) % t != 0:
        converted_msg_tab.append(
            converted_msg[((len(converted_msg)//t)*t): len(converted_msg)])

    return converted_msg_tab


def encryption_msg(n, pub, msg):
    pass


# ===== Q 1.5 ===== #


def decryption_msg(n, priv, msg):
    pass
