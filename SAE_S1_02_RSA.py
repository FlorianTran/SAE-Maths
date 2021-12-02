### RAS ###
import math

# Q. 1.1

# Renvoie un tableau de tous les nombres premiers entre 0 et n


def list_prim(n):
    result = []
    if n <= 1:
        return result
    for num in range(2, n+1):
        if is_prim(num):
            result.append(num)
    return result

# Renvoie si nombre n est enier ou pas


def is_prim(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


""" def primmaisvrmrapide(n):
    out = list()
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if (sieve[p] and sieve[p] % 2 == 1):
            out.append(p)
            for i in range(p, n+1, p):
                sieve[i] = False
    return out """

# Q. 1.2
