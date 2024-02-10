from turtle import *

# Paramètre vitesse tortue
speed(0)

#### Fonctions pour clean code ####


def forward_right(f: int, r: int):
    """
        Trace un trait puis la tortue tourne vers la droite pour faire une nouvelle instruction

    Args:
        f (int): faire avancer la tortue du nombre de pixels voulus
        r (int): faire tourner la tortue vers la droite de l'angle voulu
    """
    forward(f)
    right(r)


def right_forward(r: int, f: int) -> None:
    """
        La tortue tourne vers la droite puis trace un trait

    Args:
        r (int): faire tourner la tortue vers la droite de l'angle voulu
        f (int): faire avancer la tortue du nombre de pixels voulus
    """
    right(r)
    forward(f)


def color_width(color_trait: str, w: int) -> None:
    """
        Change la couleur et l'épaisseur du trait de la tortue

    Args:
        color_trait (str): couleur du trait de la tortue
        w (int): épaisseur du trait de la tortue
    """
    color(color_trait)
    width(w)


def up_goto_down(x: float, y: float) -> None:
    """
        Place la tortue sur une position donnée en ayant levé le stylo

    Args:
        x (float): axe 'x' où va aller la tortue
        y (float): axe 'y' où va aller la tortue
    """
    up()
    goto(x, y)
    down()


def forward_width(f: int, w: int) -> None:
    """
        Avance la tortue puis modifie l'épaisseur du trait

    Args:
        f (int): faire avancer la tortue du nombre de pixels voulus
        w (int): épaisseur du trait de la tortue
    """
    forward(f)
    width(w)


def forward_color(f: int, color_trait: str) -> None:
    """
        Avance puis modifie la couleur de la tortue

    Args:
        f (int): faire avancer la tortue du nombre de pixels voulus
        color_trait (str): couleur du trait de la tortue
    """
    forward(f)
    color(color_trait)


def up_forward_down(f: int) -> None:
    """
        Lève le stylo, avance, baisse le stylo

    Args:
        f (int): faire avancer la tortue du nombre de pixels voulus
    """
    up()
    forward(f)
    down()


def color_fillcolor(color_trait: str, color_rempl: str) -> None:
    """
        Définit la couleur du trait de la tortue puis la couleur de remplissage

    Args:
        color_trait (str): couleur du trait de la tortue
        color_rempl (str): couleur de remplissage
    """
    color(color_trait)
    fillcolor(color_rempl)


#### /// Fonctions pour clean code \\\ ####


def contour_triangle(a: int, b: int, c: int, w: int, color_trait: str) -> None:
    """
        C'est une fonction qui se place aux coordonnées (b,c) puis qui trace un triangle équilatéral de longueur 'a' de couleur 'color'

    Args:
        a (int): longeur d'une côté du triangle
        b (int): abscisse où le tracé est commencé
        c (int): ordonnée où le tracé est commencé
        w (int): épaisseur du trait de la tortue
        color_rempl (str): couleur du trait de la tortue
    """
    up_goto_down(b, c)
    width(w)
    color(color_trait)
    for i in range(3):
        forward_right(a, -120)
    color("white")


def triangle_fleche(a: int, color_rempl: str, d: int) -> None:
    """
      Trace un triangle équilatéral rempli avec une couleur choisie

    Args:
        a (int): taille d'un coté du triangle
        color (str): permet de mettre une couleur de remplissage au choix pour ce triangle
        d (int): l'angle d'inclinaison du triangle pour s'adapter correctement au panneau
    """
    # 'color' est la couleur qui va etre utilisée pour remplir ce triangle
    fillcolor(color_rempl)
    # 'd' est le degrés de la fleche qui tourne
    right(d)
    begin_fill()
    for i in range(3):
        forward_right(a, -120)
    end_fill()


def milieu_triangle(a: int, h: int) -> None:
    """
        Permet à la tortue de se placer au milieu du triangle

    Args :
        a (int): représente la distance dont la tortue va avancer
        h (int): représente la hauteur qui sépare les triangles du tour et la figure a l'intérieur
    """
    up()
    forward_right(a, -90)
    up_forward_down(h)


def virage_droit(a: int, color_trait: str) -> None:
    """
      Trace le virage à droite sans les flèches

    Args:
        a (int): épaisseur du trait de la tortue
        color_tortue (str): couleur du trait de la tortue
    """
    width(a)
    color(color_trait)
    circle(-170, 80)
    width(1)


def carre(x: int, color_trait: str, color_rempl: str) -> None:
    """
        Trace un carré

    Args:
        x (int): représente la valeur d'un coté du carré
        color_trait (str): couleur du trait de la tortue
        color_rempl (str): couleur de remplissage
    """
    color_fillcolor(color_trait, color_rempl)
    begin_fill()
    for i in range(4):
        forward_right(x, -90)
    end_fill()
    color("black")


def triangle_isocele(a: int, color_rempl: str, d: int, h: int) -> None:
    """
        Trace un triangle isocèle

    Args:
        a (int): taille du coté de la base du triangle
        color_rempl (str): couleur choisie pour remplir le triangle
        d (int): angle d'inclinaison du triangle
        h (int): représente la hauteur du triangle
    """
    # 'd' est l'angle d'inclinaison
    right(d)
    fillcolor(color_rempl)
    begin_fill()
    # récupère toutes les positions utiles
    pos_init = position()
    # abscisse
    pos_init_abs = xcor()
    # ordonnée
    pos_init_ord = ycor()
    forward(a)
    # aller au milieu du segment et a l'abscisse donnée qui se rajoute en plus de l'abscisse du point où est la tortue, pareil pour l'ordonnée
    goto(pos_init_abs + a / 2, pos_init_ord + h)
    # revenir au point initial (angle bas gauche)
    goto(pos_init)
    end_fill()


def fleche_principale_demi_cercle() -> None:
    """
        Permet d'enlever le demi cercle noir en bas de la flèche
    """
    begin_fill()
    right(90)
    circle(47, 180)
    end_fill()


def fleche_principale() -> None:
    """
        Trace la flèche principale du panneau 2
    """
    abs_init, ord_init = position()
    color_width("black", 90)
    # trace le trait droit de la flèche
    forward_right(250, 90)
    # change la taille du trait et la couleur du trait
    color_width("white", 1)
    # reculer un peu plus pour faire le triangle blanc plus grand afin de ne pas avoir de bords quand on trace le triangle noir pour faire la flèche
    backward(55)
    # trace le triangle au bout de la flèche blanc pour supprimer les bords ronds
    triangle_fleche(110, "white", 0)
    # se placer au bon endroit et remettre la couleur noire
    forward_color(10, "black")
    # trace le triangle noir au bout de la flèche
    triangle_fleche(90, "black", 0)
    up_goto_down(abs_init - 45, ord_init)
    # mettre le trait de la tortue en blanc
    color("white")
    triangle_isocele(90, "white", 0, 24)
    # pour enlever le petit cercle noir en bas
    fleche_principale_demi_cercle()


def rectangle_horizontal(L: int, l: int, color_trait: str,
                         color_rempl: str) -> None:
    """
        Trace un rectangle à l'orizontale
    Args:
        L (int): longueur du rectangle
        l (int): largeur du rectangle
        color_trait (str): couleur du trait de la tortue
        color_rempl (str): couleur de remplissage
    """
    color_fillcolor(color_trait, color_rempl)
    begin_fill()
    for i in range(2):
        forward_right(L, -90)
        forward_right(l, -90)
    end_fill()


def moitie_chaussee(a: int, c: int, b: int, d: int) -> None:
    """
        Fonction qui trace la moitié de la chaussée avec une épaisseur donnée, à des angles changeables en fonction de l'épaisseur et qui dépend d'un seul point

    Args:
        a (int): première longueur qui se répète
        c (int): angle répété
        b (int): seconde longueur répétée
        d (int): angle de rotation de la tortue pour faire une chaussée dans le bon sens
    """
    left(d)
    forward_right(b, -90)
    forward_right(a, c)
    forward_right(a, -c)
    forward_right(a, -90)
    forward_right(b, -90)
    forward_right(a, c)
    forward_right(a, -c)
    forward(a)


def chaussee_complete(a: int, c: int):
    """
        Fonction qui trace la chaussée entière avec une épaisseur et un angle changeables

    Args:
      a (int): longueur d'un côté
      c (int): angle d'inclinaison
    """
    begin_fill()
    moitie_chaussee(a, -30, c, 180)
    end_fill()
    up()
    left(-90)
    forward_right(75, 180)
    down()
    begin_fill()
    moitie_chaussee(a, 30, c, 0)
    end_fill()


def contour_triangle_deux(x: int, y: int) -> None:
    """
        Permet de tracer les deux contours pour les panneaux triangulaires

    Args:
        x (int): abscisse où on commence à tracer le triangle
        y (int): ordonnée où on commence à tracer le triangle
    """
    contour_triangle(500, x - 50, y - 50, 10, "red")
    contour_triangle(532, x - 66, y - 59, 5, "black")


def fleche_principale_et_barre_horizontale() -> None:
    """
        Trace la flèche principale et la barre horizontale qui forme le logo
    """
    abs_init, ord_init = position()
    fleche_principale()
    # se placer pour faire le rectangle horizontal
    up()
    color_width("black", 40)
    goto(abs_init, ord_init)
    forward_right(290 / 2, -90)
    down()
    width(1)


def fleche_principale_positionnement() -> None:
    """
        Permet de positionner correctement la tortue pour tracer la suite du panneau au bon endroit
    """
    forward_right(23, -90)
    forward_right(15, 90)
    color("white")
    down()


def fleche_virage() -> None:
    """
        Permet de tracer la flèche dans le virage du panneau 1
    """
    # récupere la position de la tortue avant qu'elle commence a tracer le trait d'épaisseur 'a'
    pos_init = position()
    # tracer le trait principal de la flèche
    virage_droit(35, "black")
    # placer la tortue au bon endroit
    right(90)
    forward_right(-15, -90)
    forward_right(4, 90)
    # tracer le triangle au bout pour faire la flèche
    triangle_fleche(32, "black", -5)
    right(5)
    # placer la tortue au bon endroit
    up()
    goto(pos_init)
    fleche_principale_positionnement()


def panneau_1(x: int, y: int) -> None:
    """
        Dessine le panneau 1: virage à droite

    Args:
        x (int): abscisse 'x' où va être dessiné ce panneau
        y (int): ordonnée 'y' où va être dessiné ce panneau
    """
    # contour rouge et noir du panneau
    contour_triangle_deux(x, y)
    up_goto_down(x, y)
    # placer la tortue au bon endroit sur le triangle pour qu'elle trace la flèche au milieu du triangle
    milieu_triangle(100, 100)
    up_forward_down(-100)
    fleche_virage()
    # tracer le triangle blanc en bas de la flèche
    triangle_fleche(40, "white", 160)
    # remettre la tortue en direction de la droite pour ne pas affecter les autres panneaux
    left(240)


def panneau_2(x: int, y: int) -> None:
    """
        Trace le panneau 2: intersectionn où vous êtes prioritaire

    Args:
        x (int): abscisse 'x' où va être dessiné ce panneau
        y (int): ordonnée 'y' où va être dessiné ce panneau
    """
    # récupération des données de positionnement
    up_goto_down(x, y)
    abs_base, ord_base = position()
    milieu_triangle(200, -20)
    fleche_principale_et_barre_horizontale()
    backward(100)
    # trace le rectangle
    rectangle_horizontal(200, 40, "black", "black")
    right(180)
    # se placer prêt à faire le contour dans le bon sens
    up_goto_down(abs_base, ord_base)
    contour_triangle_deux(x, y)


def panneau3(x: int, y: int) -> None:
    """
        Fonction qui trace le contour du triangle puis la chaussée intérieure

    Args:
        x (int): abscisse 'x' où va être dessiné ce panneau
        y (int): ordonnée 'y' où va être dessiné ce panneau
    """
    contour_triangle_deux(x, y)
    # se placer
    up()
    forward_right(330, -90)
    forward_right(250, -90)
    down()
    color("black")
    # trace la chaussée
    chaussee_complete(-70, -55)
    left(90)


def contour_cercle(r: int, a: int, w: int, color_trait: str, color_rempl: str,
                   bool: bool) -> None:
    """
      Trace le cercle qui délimite le contour du panneau

    Args:
        r (int): rayon du cercle que la tortue va tracer
        a (int): angle que va faire la tortue avant de s'arrêter
        w (int): épaisseur du trait de la tortue
        color_trait (str): Permet de mettre une couleur au trait de la tortue
        color_rempl (str): Permet de mettre une couleur au remplissage de la tortue
        bool(bool): remplir l'intérieur du cercle ?
    """
    width(w)
    if bool == True:  # fait un cercle rempli
        color_fillcolor(color_trait, color_rempl)
        begin_fill()
        circle(r, a)
        end_fill()
        # réinitialise la taille du trait pour ne pas impacter la suite du programme
        width(1)
    elif bool == False:  # fait un cercle non rempli
        color(color_trait)
        circle(r, a)
        width(1)


def rectangle_horizontal(L: int, l: int, color_trait: str,
                         color_rempl: str) -> None:
    """
        Trace un rectangle à l'horizontale

    Args:
        L (int): longueur du rectangle
        l (int): largeur du rectangle
        color_trait (str): couleur du trait de la tortue
        color_rempl (str): couleur de replissage
    """
    color_fillcolor(color_trait, color_rempl)
    begin_fill()
    for i in range(2):
        forward_right(L, -90)
        forward_right(l, -90)
    end_fill()


def fond_panneau_rond(
    x: int,
    y: int,
    color_trait: str,
    color_rempl: str,
) -> None:
    """
        Trace le fond des panneaux ronds (remplissage + contour)

    Args:
        x (int): axe des abscisses où on trace le panneau
        y (int): axe des ordonnées où on trace le panneau
        color_trait (str): couleur du trait de la tortue
        color_rempl (str): couleur de remplissage
    """
    up_goto_down(x, y)
    # contour cercle noir
    contour_cercle(210, 360, 5, "black", "white", True)
    up_goto_down(x, y + 20)
    # contour + remplissage cercle bleu
    contour_cercle(190, 360, 30, color_trait, color_rempl, True)


def placer_milieu_cercle():
    """
        Place la tortue au milieu du rond
    """
    up()
    left(90)
    # comme si je faisais avancer puis reculer pour se mettre au bon endroit ppur commencer mon rectangle
    forward_right(210 - 55, -90)
    forward_right(290 / 2, 180)
    down()


def panneau_4(x: int, y: int) -> None:
    """
        Trace le panneau 4: Circulation interdite à tous les véhicules dans les deux sens

    Args:
        x (int): abscisse de la tortue pour commencer le panneau
        y (int): ordonée de la tortue pour commencer le panneau
    """
    fond_panneau_rond(x, y, "red", "white")


def panneau_5(x: int, y: int) -> None:
    """
        Trace le panneau 5: Sens interdit

    Args:
        x (int): abscisse de la tortue pour commencer le panneau
        y (int): ordonée de la tortue pour commencer le panneau
    """
    fond_panneau_rond(x, y, "red", "red")
    # aller au milieu du rond
    placer_milieu_cercle()
    rectangle_horizontal(300, 65, "white", "white")


def panneau_6(x: int, y: int) -> None:
    """
        Trace le panneau 6 : Fin d'interdiction

    args:
        x (int): abscisse de la tortue pour commencer le panneau
        y (int): ordonée de la tortue pour commencer le panneau
    """
    fond_panneau_rond(x, y, "black", "white")
    up()
    forward_right(-80, -90)
    forward_right(25, 35)
    down()
    rectangle_horizontal(360, 50, "black", "black")
    right(55)


def placer_gauche_cercle() -> None:
    """
        Place la tortue un peu à gauche par rapport au milieu et en bas du cercle
    """
    up()
    left(90)
    forward_right(50, -90)
    forward_right(50, 180)
    down()


def fleche(x: int) -> None:
    """
        Trace une flèche tournée vers la droite

    Args :
        x (int): représente le multiplicateur pour agrandir la taille de la flèche (ex: pour x = 2, la taille de la flèche sera 2 fois plus grande que la taille initiale de la flèche)
    """
    begin_fill()
    right(140)
    forward_right(x * 10, -140)
    forward_right(x * 5, -40)
    forward_right(x * 14.3, -100)
    forward_right(x * 14.3, -40)
    forward_right(x * 5, -140)
    forward_right(x * 10, -140)
    # remettre la tortue dans la meme direction que celle de départ
    right(100)
    end_fill()


def milieu_droit_rectangle(L: int, l: int) -> None:
    """
        Permet d'aller au milieu à droite du rectangle

    Args:
        L (int): entrer la longueur du rectangle d'où on veut aller au milieu
        l (int): entrer la largeur du rectangle d'où on veut aller au milieu
    """
    up()
    forward(L)
    left(90)
    forward(l / 2)
    right(90)
    down()


def debut_fct_fleche_courte_et_longue() -> None:
    """
        Début d'instructions des fonctions flèches
        Permet de faire du clean code en évitant toutes les répétitions d'instructions des fonctions flèches
    """
    left(90)
    rectangle_horizontal(150, 55, "white", "white")
    # aller au milieu en haut du rectangle
    milieu_droit_rectangle(150, 55)
    width(55)


def fleche_longue_droite() -> None:
    """
        Trace une flèche longue vers la droite
    """
    debut_fct_fleche_courte_et_longue()
    circle(-70, 90)
    forward_width(80, 1)
    forward_right(11, 90)
    forward_right(22.5, -90)


def fleche_courte_droite() -> None:
    """
        Trace une flèche courte vers la droite
    """
    debut_fct_fleche_courte_et_longue()
    circle(-70, 90)
    forward_width(50, 1)
    forward_right(11, 90)
    forward_right(19, -90)


def fleche_courte_gauche() -> None:
    """
        Trace une flèche courte vers la gauche
    """
    debut_fct_fleche_courte_et_longue()
    circle(70, 90)
    forward_width(50, 1)
    forward_right(11, -90)
    forward_right(-19, 90)


def panneau_7(x: int, y: int) -> None:
    """
        Trace le panneau 7: Obligation de tourner à droite avant le panneau

    Args:
        x (int): abscisse de la tortue pour commencer le panneau
        y (int): ordonée de la tortue pour commencer le panneau
    """
    color("black")
    fond_panneau_rond(x, y, "blue", "blue")
    # aller au milieu du rond
    placer_milieu_cercle()
    rectangle_horizontal(220, 55, "white", "white")
    # aller au bout du rectangle (angle bas droit)
    forward(220)
    fleche(10)


def panneau_8(x: int, y: int) -> None:
    """
        Trace le panneau 8: Direction obligatoire à la prochaine intersection

    Args:
        x (int): abscisse de la tortue pour commencer le panneau
        y (int): ordonnée de la tortue pour commencer le panneau
    """
    fond_panneau_rond(x, y, "blue", "blue")
    # aller à gauche du rond
    placer_gauche_cercle()
    # rectangle du milieu à la veticale
    fleche_longue_droite()
    fleche(8)


def panneau_9(x: int, y: int) -> None:
    """
        Trace le panneau 9: Direction obligatoire à la prochaine intersection
    Args:
        x (int): abscisse de la tortue pour commencer le panneau
        y (int): ordonnée de la tortue pour commencer le panneau
    """
    fond_panneau_rond(x, y, "blue", "blue")
    # aller au milieu du rond
    right_forward(-90, 30)
    right_forward(90, 27)
    abs_init, ord_init = position()
    # rectangle du milieu à la veticale
    fleche_courte_droite()
    fleche(6.5)
    up_goto_down(abs_init, ord_init)
    fleche_courte_gauche()
    fleche(6.5)
    left(180)


def fond_panneau_bonus() -> None:
    """
        Permet de créer le fond carré du panneau bonus
    """
    carre(500, "blue", "blue")
    up()
    forward_right(-10, -90)
    forward_right(-10, 90)
    down()
    width(6)
    # "vide" pour ne pas avoir a mettre de couleur de remplissage
    carre(520, "Black", "")
    width(0)


def placer_milieu_bas_panneau() -> None:
    """
        Permet de se placer au milieu en bas du panneau
    """
    up()
    # '+ 40' -> la moitié de la largeur du rectangle d'apres
    forward_right(255 + 40, -90)
    forward_right(30, 90)
    down()


def aller_haut_gauche_rectangle() -> None:
    """
        Permet de se placer dans l'angle en haut à gauche du rectangle
    """
    up()
    forward_right(300, -90)
    forward_right(80, 180)
    down()


def rectangle_blanc_haut() -> None:
    """
        Trace le rectangle horizontal en haut du panneau
    """
    # '40' -> la largeur du rectangle vertical divisé par 2
    backward(160 - 40)
    rectangle_horizontal(320, 150, "white", "white")


def petit_rectangle_rouge() -> None:
    """
        Trace le petit rectangle rouge en haut du panneau à l'intérieur de l'autre rectangle
    """
    # se placer
    up()
    forward_right(10, -90)
    forward_right(10, 90)
    down()
    # tracer le rectangle
    rectangle_horizontal(300, 130, "red", "red")


def rectangle_horizontal(L: int, l: int, color_trait: str,
                         color_rempl: str) -> None:
    """
        Trace un rectangle à l'horizontale

    Args:
        L (int): longueur du rectangle
        l (int): largeur du rectangle
        color_trait (str): couleur du trait de la tortue
        color_rempl (str): couleur de replissage
    """
    color_fillcolor(color_trait, color_rempl)
    begin_fill()
    for i in range(2):
        forward_right(L, -90)
        forward_right(l, -90)
    end_fill()


def panneau_bonus(x, y) -> None:
    """
        Trace le panneau bonus : Impasse ou rue sans issue
    """
    up_goto_down(x, y)
    # création du fond du panneau
    fond_panneau_bonus()
    placer_milieu_bas_panneau()
    # se mettre à la perpendiculaire
    left(90)
    rectangle_horizontal(300, 80, "white", "white")
    aller_haut_gauche_rectangle()
    # prochain rectangle horizontal
    rectangle_blanc_haut()
    # plus petit rectangle rouge au milieu
    petit_rectangle_rouge()


def affichage(a: int) -> None:
    '''
      Trace les panneaux 1,2,3 si le nombre entré est 1.
      Les panneaux 4,5,6 si le nombre entré est 2.
      Les panneaux 7,8,9 si le nombre entré est 3.
      Le panneaux bonus si le nombre entré est 4.
      Efface si le nombre entré est 5.

  Args:
      a(int): nombre entré par l'utilisateur
  '''
    # mettre un chiffre supérieur à 5 pour arrêter la boucle
    while a < 6:
        # entrer le chiffre 1 pour afficher la première catégorie
        if a == 1:
            panneau_1(215, -270)
            panneau_2(-620, -270)
            panneau3(-203, -55)
        # entrer le chiffre 2 pour afficher la deuxième catégorie
        elif a == 2:
            panneau_4(-468, -200)
            panneau_5(0, -200)
            panneau_6(450, -200)
        # entrer le chiffre 3 pour afficher la troisième catégorie
        elif a == 3:
            panneau_7(-450, -200)
            panneau_8(0, -200)
            panneau_9(450, -200)
        # entrer le chiffre 4 pour afficher le panneau bonus
        elif a == 4:
            panneau_bonus(-200, -200)
        elif a == 5:
            clear()

        a = int(input())


a = int(input())
affichage(a)

hideturtle()
exitonclick()
