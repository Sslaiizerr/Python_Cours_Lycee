from random import *

def tableau_nb_hasard(n:int) -> list:
    """Prend en paramètre un entier naturel et qui renvoie un tableau rempli au hasard de n nombres entiers compris entre O et 100."""
    tab_1 = [randint(0, 100) for nbr in range(n)]
    return tab_1
    
def echange_valeur_tableau(tab: list, indice1: int, indice2: int) -> list:
  temp = tab[indice1]
  tab[indice1] = tab[indice2]
  tab[indice2] = temp
  return tab

def tri_insertion(tab: list) -> list:
  taille = len(tab)
  if taille == 0 or taille == 1:
    return tab
  for indice in range(taille):
    while tab[indice - 1] > tab[indice] and indice != 0:
      echange_valeur_tableau(tab, indice - 1, indice)
      indice -= 1
  return tab

tab_1111 = tableau_nb_hasard(50)
print(tri_insertion(tab_1111))

