def enleve_les_espaces_en_trop(phrase: str)-> str:
    intermédiaire = phrase.split()
    for elt in intermédiaire:
        if elt == ",":
            phrase += elt
            
        elif elt == ".":
            phrase += elt
            
        elif elt == "!":
            phrase += elt
            
        elif elt == "?":
            phrase += elt
            
        elif elt == ":":
            phrase += elt
            
        elif elt == ";":
            phrase += elt
            
        else:
            phrase += " " + elt
    return phrase

print(enleve_les_espaces_en_trop("L’interjection	« Hélas ! » témoigne de son jugement rétrospectif	marqué par le regret. La	phrase négative	et exclamative qui	suit explicite la raison du remords : le jour du départ	d’Amiens. Le narrateur insiste ainsi sur le concours de	circonstances qui a conduit à sa rencontre avec Manon. Avant le	récit même de l’événement, le narrateur procède ainsi à une	dramatisation qui vise à susciter l’intérêt de ses auditeurs et	à souligner l’importance de cet épisode. L’emploi du	conditionnel passé (« j’aurais porté »), traduisant	l’irréel du passé, souligne le caractère irréversible des	conséquences associées à la perte de « l’innocence ».	Un tel jugement rétrospectif du « je » narrateur met en	évidence les changements profonds qui ont affecté le personnage	depuis cette date. Mais ce n’est qu’avec la connaissance des	événements qui ne sont pas encore advenus que le narrateur peut	juger du caractère funeste du choix du jour de son départ. Des	Grieux narrateur montre ainsi qu’il n’était pas en son pouvoir	d’échapper à cette rencontre qu’il présente comme une œuvre	du destin."))