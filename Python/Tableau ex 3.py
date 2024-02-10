releve_notes = [12, 10, 17, 16, 8, 12, 16, 12]
# moi


def somme(tab) -> int:
    somme = 0
    for indice in range(len(tab)):
        somme += tab[indice]
    return somme


def moyenne(tab):
    moyenne = somme(tab) / len(tab)
    return moyenne


# prof

def somme(tab):
    som = 0
    for i in range(len(tab)):
        som = som+tab[i]
    return som


def moyenne(tab):
    som = somme(tab)
    taille = len(tab)
    moy = som/taille
    return moy


print(moyenne(releve_notes))
