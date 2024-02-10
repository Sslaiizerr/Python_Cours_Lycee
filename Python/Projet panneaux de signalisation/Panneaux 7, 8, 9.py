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
        Change la couleur ey lépaisseur du trait de la tortue
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
        Fait un 'up()', avance et finit avec un 'down()'
    Args:
        f (int): faire avancer la tortue du nombre de pixels voulu
    """
    up()
    forward(f)
    down()


def color_fillcolor(color_trait: str, color_rempl: str) -> None:
    color(color_trait)
    fillcolor(color_rempl)

#### /// Fonctions pour clean code \\\ ####


def contour_cercle(r: int, a: int, w: int, color_trait: str, color_rempl: str, bool: bool) -> None:
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


def fond_panneau_rond(x: int, y: int,  color_trait: str, color_rempl: str,) -> None:
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


def placer_milieu_cercle() -> None:
    """
        Place la tortue au milieu du rond
    """
    up()
    left(90)
    # comme si je faisais avancer puis reculer pour se mettre au bon endroit ppur commencer mon rectangle
    forward_right(210-55, -90)
    forward_right(290 / 2, 180)
    down()


def placer_gauche_cercle() -> None:
    """
        Place la tortue un peu à gauche et en bas du cercle
    """
    up()
    left(90)
    forward_right(50, -90)
    forward_right(50, 180)
    down()


def fleche(x: int) -> None:
    """
        Trace une fleche tournée vers la droite

    Args :
        x (int): représente le multiplicateur pour agrandir la taille de la fleche (ex: pour x = 2, la taille de la fleche sera 2 fois plus grande que la taille de la fleche de base)
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
        Permet d'aller au milieu a droite du rectangle

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
        Permet de faire du clean code en évitant toutes les répétitions d'instructions des fonctions fleches
    """
    left(90)
    rectangle_horizontal(150, 55, "white", "white")
    # aller au milieu en haut du rectangle
    milieu_droit_rectangle(150, 55)
    width(55)


def fleche_longue_droite() -> None:
    """
        Trace une fleche longue vers la droite
    """
    debut_fct_fleche_courte_et_longue()
    circle(-70, 90)
    forward_width(80, 1)
    forward_right(11, 90)
    forward_right(22.5, -90)


def fleche_courte_droite() -> None:
    """
        Trace une fleche courte vers la droite
    """
    debut_fct_fleche_courte_et_longue()
    circle(-70, 90)
    forward_width(50, 1)
    forward_right(11, 90)
    forward_right(19, -90)


def fleche_courte_gauche() -> None:
    """
        Trace une fleche courte vers la gauche
    """
    debut_fct_fleche_courte_et_longue()
    circle(70, 90)
    forward_width(50, 1)
    forward_right(11, -90)
    forward_right(-19, 90)


def panneau_7(x: int, y: int) -> None:
    """
        Trace le panneau 7: 

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
        Trace le panneau 8: 

    Args:
        x (int): abscisse de la tortue pour commencer le panneau
        y (int): ordonnée de la tortue pour commencer le panneau
    """
    # départ programme
    fond_panneau_rond(x, y, "blue", "blue")
    # aller à gauche du rond
    placer_gauche_cercle()
    # rectangle du milieu à la veticale
    fleche_longue_droite()
    fleche(8)


def panneau_9(x: int, y: int) -> None:
    """
        Trace le panneau 9: 
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


panneau_7(-450, -200)
panneau_8(0, -200)
panneau_9(450, -200)

hideturtle()
exitonclick()
