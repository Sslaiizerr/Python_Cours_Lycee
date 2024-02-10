from turtle import *

# Paramètre vitesse tortue
speed(0)

#### Fonctions pour clean code ####


def forward_right(f: int, r: int):
    """
        Trace un trait puis la tortue tourne vers la droite pour faire une nouvelle instruction

    Args:
        f (int): faire avancer la tortue du nombre de pixels voulu
        r (int): faire tourner la tortue vers la droite de l'angle voulu
    """
    forward(f)
    right(r)


def right_forward(r: int, f: int) -> None:
    """
        La tortue tourne vers la droite puis trace un trait

    Args:
        r (int): faire tourner la tortue vers la droite de l'angle voulu
        f (int): faire avancer la tortue du nombre de pixels voulu
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
        Fais un 'up()' suivi d'un 'goto()' et finit par un 'down()'

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
        f (int): faire avancer la tortue du nombre de pixels voulu
        w (int): épaisseur du trait de la tortue
    """
    forward(f)
    width(w)


def forward_color(f: int, color_trait: str) -> None:
    """
        Avance puis modifie la couleur de la tortue

    Args:
        f (int): faire avancer la tortue du nombre de pixels voulu
        color_trait (str): couleur du trait de la tortue
    """
    forward(f)
    color(color_trait)


def up_forward_down(f: int) -> None:
    """
        Fait un 'up()' puis avance et finit avec un 'down()'

    Args:
        f (int): faire avancer la tortue du nombre de pixels voulu
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
      Trace un triangle équilatéral

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
        Permet à la tortue de se placer au bon endroit dans le triangle pour tracer le virage à droite au milieu du triangle

    Args :
        a (int): représente le nombre de pas vers l'avant que la tortue va faire
        h (int): représente la hauteur qui sépare les triangles du tour et la figure a l'intérieur
    """
    up()
    forward_right(a, -90)
    up_forward_down(h)


def virage_droit(a: int, color_trait: str) -> None:
    """
      Trace le virage à droite sans les fleches

    Args:
        a (int): épaisseur du trait de la tortue
        color_tortue (str): permet de mettre une couleur au trait de la tortue
    """
    width(a)
    color(color_trait)
    circle(-170, 80)
    width(1)


def carre(x: int, color_trait: str, color_rempl: str) -> None:
    """
        Trace un carre

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
        color_rempl (str): couleur choisi pour remplir le triangle
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
        Permet d'enlever le demi cercle noir en bas de la fleche
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
    # tracer le trait droit de la fleche
    forward_right(250, 90)
    # changer la taille du trait et la couleur du trait
    color_width("white", 1)
    # reculer trop pour faire le triangle blanc plus grand afin de ne pas avoir de bords quand on trace le triangle noir pour faire la flèche
    backward(55)
    # tracer le triangle au bout de la fleche blanc pour supprimer les bords ronds
    triangle_fleche(110, "white", 0)
    # se placer au bon endroit et remettre la couleur noire
    forward_color(10, "black")
    # tracer le triangle au bout de la fleche noir
    triangle_fleche(90, "black", 0)
    up_goto_down(abs_init - 45, ord_init)
    # mettre le trait de la tortue en blanc
    color("white")
    triangle_isocele(90, "white", 0, 24)
    # pour enlever le petit cercle noir en bas
    fleche_principale_demi_cercle()


def rectangle_horizontal(L: int, l: int, color_trait: str,  color_rempl: str) -> None:
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
        Fonction qui trace la moitié de la chaussée avec une épaisseur donnée, a des angles changeables en fonction de l'épaisseur et qui dépend d'un seul point

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
        Trace la fleche principale et la barre horizontale qui forme le logo
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
        Permet de tracer la fleche dans le virage du panneau 1
    """
    # récuperer la position de la tortue avant qu'elle commence a tracer le trait d'épaisseur 'a'
    pos_init = position()
    # tracer le trait principal de la fleche
    virage_droit(35, "black")
    # placer la tortue au bon endroit
    right(90)
    forward_right(-15, -90)
    forward_right(4, 90)
    # tracer le triangle au bout pour faire la fleche
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
        x (int): axe 'x' où va être dessiné ce panneau
        y (int): axe 'y' où va être dessiné ce panneau
    """
    # contour rouge et noir du panneau
    contour_triangle_deux(x, y)
    up_goto_down(x, y)
    # placer la tortue au bon endroit sur le triangle pour qu'elle trace la fleche au milieu du triangle
    milieu_triangle(100, 100)
    up_forward_down(-100)
    fleche_virage()
    # tracer le triangle blanc en bas de la fleche
    triangle_fleche(40, "white", 160)
    # remettre la tortue en direction de la droite pour ne pas affecter les autres panneaux
    left(240)


def panneau_2(x: int, y: int) -> None:
    """
        Trace le panneau 2: intersectionn où vous êtes prioritaire

    Args:
        x (int): axe 'x' où va être dessiné ce panneau
        y (int): axe 'y' où va être dessiné ce panneau
    """
    # récupération des données de positionnement
    up_goto_down(x, y)
    abs_base, ord_base = position()
    milieu_triangle(200, -20)
    fleche_principale_et_barre_horizontale()
    backward(100)
    # tracer le rectangle
    rectangle_horizontal(200, 40, "black", "black")
    right(180)
    # se placer prêt a faire le contour dans le bon sens
    up_goto_down(abs_base, ord_base)
    contour_triangle_deux(x, y)


def panneau3(x: int, y: int) -> None:
    """
        Fonction qui trace le contour du triangle puis la chaussée intérieure

    Args:
        x (int): axe 'x' où va être dessiné ce panneau
        y (int): axe 'y' où va être dessiné ce panneau
    """
    contour_triangle_deux(x, y)
    up()
    forward_right(330, -90)
    forward_right(250, -90)
    down()
    color("black")
    chaussee_complete(-70, -55)


panneau_1(215, -270)
panneau_2(-620, -270)
panneau3(-203, -55)

hideturtle()
exitonclick()
