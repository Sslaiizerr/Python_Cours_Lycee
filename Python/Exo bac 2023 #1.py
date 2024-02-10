def verifie(tab):
    n=len(tab)
    if n==1:
        return True
    for i in range(n-1):
        if tab[i]>tab[i+1]:
            return False
    return True


print(verifie([0, 5, 8, 8, 9]))
print(verifie([8, 12, 4]))
print(verifie([-1, 4]))
print(verifie([5]))
