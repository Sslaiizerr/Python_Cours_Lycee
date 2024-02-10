tab1 = []
tab2 = [8]
tab3 = [1, 2, 3, 4, 5]
tab4 = [45, 24, 18, 4]
tab5 = [27, 10, 12, 8, 11]

def echange_valeur_tableau(tab: list, indice1: int, indice2: int) -> list:
  temp = tab[indice1]
  tab[indice1] = tab[indice2]
  tab[indice2] = temp
  return tab

def tri_insertion(tableau) -> list:
    for indice in range(1, len(tableau)):
        ind0 = indice
        while (ind0 >= 1) and (tableau[ind0 - 1] > tableau[ind0]):
            echange_valeur_tableau(tableau, ind0 - 1, ind0)
            ind0 = ind0 - 1
    return tableau


assert tri_insertion(tab1) == [], "erreur 1"
assert tri_insertion(tab2) == [8], "erreur 2"
assert tri_insertion(tab3) == [1, 2, 3, 4, 5], "erreur 3"
assert tri_insertion(tab4) == [4, 18, 24, 45], "erreur 4"
assert tri_insertion(tab5) == [8, 10, 11, 12, 27], "erreur 5"