import numpy as np
import SAE_S1_02_RSA as rsa
import SAE_S1_02_Corr as corr


def convert_binary(crypted_msg):
    """
    convert un tableau d'entier en un tableau de tableau de vecteur
    """
    list_vect = []
    i = 0
    for num in crypted_msg:
        tmp_vect = []
        for chiffre in str(num):
            tmp_val = str(format(int(chiffre), "b")).zfill(4)
            a, b, c, d = int(tmp_val[0]), int(
                tmp_val[1]), int(tmp_val[2]), int(tmp_val[3])
            vect = [(a+b+d) % 2, (a+c+d) % 2, a, (b+c+d) % 2, b, c, d]
            tmp_vect.append(vect)
        list_vect.append(tmp_vect)
        i = i+1
    return list_vect

    # en gros on met chiffre par chiffre en binaire = chiffre = 4 bits apres avec M on le met en vecteur


def noise(vect_msg):
    """
    prend un vecteur vect_msg et renvoie ce vecteur potentiellement bruite
    """
    # on fait une copie du vecteur initial
    vect = vect_msg.copy()
    # une chance sur quatre de ne pas bruiter le vecteur
    test = np.random.randint(0, 4)
    if test > 0:
        index = np.random.randint(0, np.size(vect))
        vect[index] = (vect[index] + 1) % 2
    return vect


def sim_noise(tab_vect):
    tab_vect_noise = []
    for num in tab_vect:
        tmp = []
        for v in num:
            tmp.append(noise(v))
        tab_vect_noise.append(tmp)
    return tab_vect_noise


def denoise(vect_msg):
    pass  # regarde la distance ou


def reconvert_binary(vect_msg):
    msg = []
    for num in vect_msg:
        total = ""
        for v in num:
            a, b, c, d = v[2], v[4], v[5], v[6]
            val = 8*a+4*b+2*c+d
            total = total + str(val)
        msg.append(int(total))
    return msg
