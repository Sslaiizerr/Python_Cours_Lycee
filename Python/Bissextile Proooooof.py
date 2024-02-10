def bissextile(a: int) -> bool:
    if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
        return (True)
    else:
        return (False)


def nb_jours_annee(a: int) -> int:
    if bissextile(a) == True:
        return (366)
    else:
        return (365)


def nb_jours_mois(a: int, m: int) -> int:
    if m == 2:
        if bissextile(a) == True:
            return (29)
        else:
            return (28)
    elif m <= 7:
        return (30 + m % 2)
    else:
        return (31 - m % 2)


def nb_jours(jn, mn, an, j, m, a) -> int:
    nb_j = nb_jours_mois(an, mn)-jn
    for k in range(mn + 1, 13):
        nb_j = nb_j + nb_jours_mois(an, k)
    for k in range(an + 1, a):
        nb_j = nb_j + nb_jours_annee(k)
    for k in range(m):
        nb_j = nb_j + nb_jours_mois(a, m)
    nb_j = nb_j + j
    return nb_j


# TEST
print(nb_jours(30, 7, 2006, 28, 11, 2022))
print(nb_jours(28, 11, 2022, 30, 7, 2006))
print("-------------------------------")
print(nb_jours(27, 11, 2022, 28, 11, 2022))
print(nb_jours(28, 11, 2022, 27, 11, 2022))
print("-------------------------------")
print(nb_jours(13, 1, 2022, 13, 1, 2022))
print("-------------------------------")
print(nb_jours(13, 1, 2022, 13, 2, 2022))
print("-------------------------------")
print(nb_jours(23, 4, 2021, 23, 4, 2022))
print(nb_jours(23, 4, 2022, 23, 4, 2021))
print("-------------------------------")
print(nb_jours(25, 11, 2021, 10, 12, 2021))
print(nb_jours(10, 12, 2021, 25, 11, 2021))
print("-------------------------------")
print(nb_jours(31, 12, 2022, 1, 1, 2023))
print(nb_jours(1, 1, 2023, 31, 12, 2022))
print("-------------------------------")
print(nb_jours(31, 12, 2020, 1, 1, 2021))
