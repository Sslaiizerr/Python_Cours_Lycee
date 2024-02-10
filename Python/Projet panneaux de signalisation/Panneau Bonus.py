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


def rectangle_horizontal(L: int, l: int, color_trait: str, color_rempl: str) -> None:
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
    goto(x, y)
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


panneau_bonus(-200, -200)

hideturtle()
exitonclick()
