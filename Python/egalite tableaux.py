def egalite_tableaux(tableau1, tableau2) -> bool:
    egalite = True
    if len(tableau1) != len(tableau2):
        return False
    if len(tableau1) == 0:
        return True
    else:
        for i in range(len(tableau1)):
            if tableau1[i] != tableau2[i]:
                egalite = False
    return egalite