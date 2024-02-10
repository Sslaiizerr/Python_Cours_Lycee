tab = [500, 200, 100, 50, 20, 10, 5, 2, 1]

prix = int(input("Quel est le prix de l'article ? "))
don = 0
result = []
for i in range(len(tab)):
    if don + tab[i] <= prix:
        don += tab[i]
        result.append(tab[i])
print(result)