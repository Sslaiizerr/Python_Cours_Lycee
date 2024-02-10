pop = int(input("Saisir la population : "))
nbr_malade = 1
nbr_jour = 1

while nbr_malade <= pop:
    nbr_malade = nbr_malade * 2
    nbr_jour += 1
print("Au jour {0} la population entière sera contaminée.".format(nbr_jour))
