a = int(input("Saisir la longeur du rectangle : "))
b = int(input("Saisir la largeur du rectangle : "))

c = a * b
if c == a*a:
    print("Ceci est un rectangle particulier vu que sa longeur et sa largeur sont identiques. Sont aire est égale à ", c, " m²")
else:
    print("Ce rectangle a une aire de ", c, " m²")
