# Ecrire un programme Python qui partitionne ce dictionnaire en deux sous dictionnaires:
# etudiantAdmis dont les clés sont les étudiants admis et les valeurs des clés sont les moyennes obtenues(moyenne supérieurs ou égales à 10).
# etudiantNonAdmis dont les clés sont les étudiants non admis et les valeurs des clés sont les moyennes obtenues(moyenne inférieur à 10).

etudiants = {"etudiant_1": 13, "etudiant_2": 17, "etudiant_3": 9, "etudiant_4": 15,
             "etudiant_5": 8, "etudiant_6": 14, "etudiant_7": 16, "etudiant_8": 12,
             "etudiant_9": 13, "etudiant_10": 15, "etudiant_11": 14, "etudiant_112": 9,
             "etudiant_13": 10, "etudiant_14": 12, "etudiant_15": 13, "etudiant_16": 7,
             "etudiant_17": 12, "etudiant_18": 15, "etudiant_19": 9, "etudiant_20": 17, }


def separation(dictionnaire_principal: dict) -> dict:
    etudiantsAdmis = {}
    etudiantsNonAdmis = {}
    for key, value in dictionnaire_principal.items():
        if value >= 10:
            etudiantsAdmis[key] = value
        else:
            etudiantsNonAdmis[key] = value
    return etudiantsAdmis, etudiantsAdmis
