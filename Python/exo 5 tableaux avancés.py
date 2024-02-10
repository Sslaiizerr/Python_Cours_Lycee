from random import *

def affichage(tableau: list):
    for ligne in tableau:
        for elt in ligne:
            print(elt, "", end="")

def tab2dim_random() -> list:
    tab = [[randint(1, 9999) for i in range(30)] for i in range(30)]
    print(affichage(tab))
    return tab

tab2dim_random()