import csv

fichier = open("Bon_de_commande.csv", "r")

table = list.csvreader(fichier,  delimiter=",")

print(table)

fichier.close()