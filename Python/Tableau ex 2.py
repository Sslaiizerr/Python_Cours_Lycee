releve_notes = [12, 10, 17, 16, 8, 12, 16, 12]

# moi


def occurences(note1):
    releve = 0
    for indice in range(len(releve_notes)):
        if releve_notes[indice] == note1:
            releve += 1
    return releve


print(occurences(12))

# la prof


def occurences_prof(v, t):
    occ = 0
    for i in range(len(t)):
        if t[i] == v:
            occ = occ+1
    return occ
