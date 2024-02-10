from math import *


def dico_carre(nbre: int) -> dict:
    dictionnaire_carre = {i ** 2 for i in range(1, nbre + 1)}
    return dictionnaire_carre


print(dico_carre(7))
