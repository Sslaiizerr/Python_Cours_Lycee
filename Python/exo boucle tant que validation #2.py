nbr_valeurs = int(input())
temp_mini = int(input())
temp_max = int(input())
valeur_saisie = int(input())
compteur = 1

while valeur_saisie >= temp_mini and valeur_saisie <= temp_max and compteur < nbr_valeurs:
    print("Rien à signaler")
    valeur_saisie = valeur_saisie = int(input())
    compteur += 1
if valeur_saisie < temp_mini or valeur_saisie > temp_max:
    print("Alerte !!")
else:
    print("Rien à signaler")
