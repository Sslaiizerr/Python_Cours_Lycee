from random import *

prix = randint(0, 100)

score = 100

tentatives = 0

print(
  "Devinez le juste prix ! Le prix est un nombre compris entre 0 et 100 inclus."
)

while True:
  nombre = int(input())
  tentatives += 1
  if nombre < prix:
    print("Le just prix est plus haut")
  if nombre > prix:
    print("Le juste prix est plus bas")
  if nombre == prix:
    print(
      "Félicitations, vous avez trouvé le juste prix {} en {} essais, votre score est {} !"
      .format(prix, tentatives, int(score / tentatives)))
    break

print("Partie terminée")
