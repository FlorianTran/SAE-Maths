import numpy as np
import SAE_S1_02_RSA as rsa
import SAE_S1_02_Corr as corr


def convert_binary(crypted_msg):
    """
    prend en entrée un tableau d'entiers 
    renvoie un tableau de tableau de vect binaire de taille 7 qui corresponde chaqun à un chiffre des entiers d'entrée
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
    prend un vecteur vect_msg
    renvoie ce vecteur potentiellement bruite (un seul bit du vecteur peut être altéré)
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
    """
    prend un tableau de tableau de vecteur (résultat de convert_binary)
    renvoie ce même tableau avec des vecteurs potentiellement bruité grace à la fonction noise
    """
    tab_vect_noise = []
    for num in tab_vect:
        tmp = []
        for v in num:
            tmp.append(noise(v))
        tab_vect_noise.append(tmp)
    return tab_vect_noise


def denoise(vect):
    """
    prend un vecteur binaire de taille7
    renvoie ce même vecteur si il n'est pas bruité sinon renvoie le vecteur corrigé
    """
    for vect_origin in corr.allvect_7:
        if corr.distance(vect, vect_origin) == 1:
            return vect_origin
    return vect


def denoise_msg(tab_vect_noise):
    """
    prend un tableau de tableau de vecteur (taille 7)
    renvoie ce même tableau avec tous les vecteurs corrigés, sans bruit
    """
    for i in range(0, len(tab_vect_noise)):
        for j in range(0, len(tab_vect_noise[i])):
            tab_vect_noise[i][j] = denoise(tab_vect_noise[i][j])
    return tab_vect_noise


def reconvert_binary(vect_msg):
    """
    prend un tableau de tableau de vecteur et reconvertit chaque vecteur en chiffre 
    puis recréer les nombre du message crypté
    renvoie un tableau d'entier
    """
    msg = []
    for num in vect_msg:
        total = ""
        for vect in num:
            a, b, c, d = vect[2], vect[4], vect[5], vect[6]
            val = 8*a+4*b+2*c+d
            total = total + str(val)
        msg.append(int(total))
    return msg


""" exemple d'un message"""

exemple = "test"
print(exemple)

"""On créer d'abord la clef publique et la clef privée. """
n, pub, priv = rsa.key_creation()

""" On convertit le message grace à la table ASCII et on l'encrypte. """
msg_crypt = rsa.encryption_msg(n, pub, rsa.convert_msg(exemple))

""" On simule un envoie, avec du bruit, pour cela on on passe d'un le message crypter en binaire. """
msg_noise = sim_noise(convert_binary(msg_crypt))

""" Ici on va venir enlever le bruit. """
msg_crypt_denoise = denoise_msg(msg_noise)

""" Pour finir on va reconvertir le msg qui est en binaire pour ensuite pouvoir le 
decrypter et enfin le reconvertir en pleine lettre (avec la table ASCII) """
msg_final = rsa.reconvert_msg(rsa.decryption_msg(
    n, priv, reconvert_binary(msg_crypt_denoise)))

print(msg_final)


def test(x):
    exemple = "test"
    cont = 0
    while x > 0:
        n, pub, priv = rsa.key_creation()
        msg_final = rsa.reconvert_msg(rsa.decryption_msg(n, priv, reconvert_binary(denoise_msg(
            sim_noise(convert_binary(rsa.encryption_msg(n, pub, rsa.convert_msg(exemple))))))))
        if exemple != msg_final:
            print(x, n, pub, priv, msg_final)
            cont = cont + 1
        x = x-1
    return cont
