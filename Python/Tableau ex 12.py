from random import *


def est_dans(element: int, tple: tuple) -> tuple:
    for elt in range(len(tple)):
        if element == elt:
            return True
    else:
        return False


print(est_dans(4, (1, 2, 3, 4, 5, 6)))
print(est_dans(9, (1, 2, 3, 4, 5, 6)))
