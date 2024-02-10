f = input(
    "Choisir une forme à dessiner en perspective cavalière (cube, pavé droit) : ")

if f == "cube":
    # cube
    x = float(input("Choisir une valeur pour 'x' étant le coté du cube : "))
    c = x ** 2
    d = x / 2

    from turtle import*
    import turtle

    down()

    # base carré
    for i in range(4):
        forward(x)
        left(90)

    # premiere arrete qui part vers la droite
    left(45)
    forward(d)
    left(180)
    forward(d)
    right(225)
    forward(x)

    # deuxieme arrete qui part vers la droite
    left(45)
    forward(d)
    left(180)
    forward(d)
    right(135)
    forward(x)

    # troisieme arrete qui part vers la droite
    right(45)
    forward(d)
    left(180)
    forward(d)
    right(45)
    forward(x)

    # quatrieme arrete qui part vers la droite
    right(135)
    forward(d)
    left(180)
    forward(d)
    left(45)
    forward(x)
    left(90)

    # deuxieme base carré
    left(45)
    forward(d)
    right(45)
    for i in range(4):
        forward(x)
        left(90)

if f == "pavé droit":
    # pavé droit
    l = float(input("Choisir une valeur pour la largeur du pavé droit : "))
    L = float(input("Choisir une valeur pour la longeur du pavé droit : "))
    largon = l / 2

    from turtle import*
    import turtle

    down()

    # base rectangle
    for i in range(2):
        forward(L)
        left(90)
        forward(l)
        left(90)

    # premiere arrete qui part vers la droite
    left(45)
    forward(largon)
    left(180)
    forward(largon)
    right(225)
    forward(L)

    # deuxieme arrete qui part vers la droite
    left(45)
    forward(largon)
    left(180)
    forward(largon)
    right(135)
    forward(l)

    # troisieme arrete qui part vers la droite
    right(45)
    forward(largon)
    left(180)
    forward(largon)
    right(45)
    forward(L)

    # quatrieme arrete qui part vers la droite
    right(135)
    forward(largon)
    left(180)
    forward(largon)
    left(45)
    forward(l)
    left(90)

    # deuxieme base rectangle
    left(45)
    forward(largon)
    right(45)
    for i in range(2):
        forward(L)
        left(90)
        forward(l)
        left(90)

else:
    print("Ce logiciel n'est pas capable de représenter votre forme ou cette forme n'existe pas.")
