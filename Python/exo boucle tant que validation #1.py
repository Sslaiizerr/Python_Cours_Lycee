nbr_max = int(input())
etage = 0
cailloux_use = 0
nbr_cailloux_etage = 0

while cailloux_use + ((etage + 1) ** 2) <= nbr_max:
    etage += 1
    nbr_cailloux_etage = etage ** 2
    cailloux_use = cailloux_use + nbr_cailloux_etage
print(etage)
print(cailloux_use)
