# choix opération
print("Quelle opération voulez vous faire? (addition, soustraction, multiplication ou division)")
choix = str(input("Saisir une opération : "))

# addition
if choix == "addition":
    a = float(input("Saisir une première valeur : "))
    b = float(input("Saisir une deuxièmeaddi valeur : "))
    r = a + b
    print(a, "+", b, "=", r)

# soustraction
elif choix == "soustraction":
    a = float(input("Saisir une première valeur : "))
    b = float(input("Saisir une deuxième valeur : "))
    r = a - b
    print(a, "-", b, "=", r)

# multiplication
elif choix == "multiplication":
    a = float(input("Saisir une première valeur : "))
    b = float(input("Saisir une deuxième valeur : "))
    r = a * b
    print(a, "*", b, "=", r)

# division
elif choix == "division":
    a = float(input("Saisir une première valeur : "))
    b = float(input("Saisir une deuxième valeur : "))
    r = a / b
    print(a, "/", b, "=", r)

# opération impossible
else:
    print("Cette opération est impossible avec cette calculatrice. Vous ne pouvez faire que des additions, des soustractions, des multiplications ou des divisions.")
