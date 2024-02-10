releve_notes = [15, 13, 18]


def echange(i: int, j: int) -> list:
    note_intermédiaire = releve_notes[i]
    releve_notes[i] = releve_notes[j]
    releve_notes[j] = note_intermédiaire
    print(releve_notes)


print(echange(0, 1))
