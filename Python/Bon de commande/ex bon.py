import csv

table = [{"réf.": 18635, "désignation": "lot crayon HB", "prix": 2.30, "qté": 1},
         {"réf.": 15223, "désignation": "stylo rouge", "prix": 1.50, "qté": 3},
         {"réf.": 20112, "désignation": "cahier petits carreaux", "prix": 3.50, "qté": 2}]

fichier = open("Bon de commande dict.csv", "w")

writer = csv.DictWriter(fichier, ["réf.", "désignation", "prix", "qté"])

writer.writeheader()
writer.writerows(table)

fichier.close()