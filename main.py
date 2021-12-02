### RAS ###
import  math

# Q. 1.1

# Renvoie un tableau de tous les nombres premiers entre 0 et n


def list_prim(n):
    result = []
    if n <= 1:
        return result
    for num in range(2, n+1):
        if is_prime(num):
            result.append(num)
    return result

# Renvoie si nombre n est enier ou pas


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Q. 1.2
print("test")