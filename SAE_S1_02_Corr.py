allvect_4 = [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0], [
    0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1]]


def application(vect_4):
    a, b, c, d = vect_4[0], vect_4[1], vect_4[2], vect_4[3]
    vect_7 = [(a+b+d) % 2, (a+c+d) % 2, a, (b+c+d) % 2, b, c, d]
    return vect_7


def tab_vect_7(allvect_4):
    all_vect_7 = []
    for vect_4 in allvect_4:
        all_vect_7.append(application(vect_4))
    return all_vect_7


allvect_7 = tab_vect_7(allvect_4)


def weight(vect_7):
    sum = 0
    for i in range(0, len(vect_7)):
        sum = sum + vect_7[i]
    return sum


def distance(vect1, vect2):
    vect3 = []
    for i in range(0, len(vect1)):
        vect3.append((vect1[i]+vect2[i]) % 2)
    return weight(vect3)


def preuve_Q4():
    for vect1 in allvect_7:
        for vect2 in allvect_7:
            if vect1 != vect2 and distance(vect1, vect2) < 3:
                return False
    return True
