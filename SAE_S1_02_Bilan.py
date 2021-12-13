import SAE_S1_02_RSA as RSA
import numpy as np



def convert_binary():
    pass
    
# en gros on met chiffre par chiffre en binaire = chiffre = 4 bits apres avec M on le met en vecteur


def noise(vect_msg):
    """
    prend un vecteur vect_msg et renvoie ce vecteur potentiellement bruite
    """
    ### on fait une copie du vecteur initial
    vect = vect_msg.copy()
    ### une chance sur quatre de ne pas bruiter le vecteur
    test = np.random.randint(0,4)
    if test>0:
        index = np.random.randint(0,np.size(vect))
    vect[index] = (vect[index] +1)%2
    return vect

def denoise(vect_msg):
    pass #regarde la distance ou ya un