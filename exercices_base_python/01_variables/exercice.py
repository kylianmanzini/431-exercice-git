# 01 — Variables
# TODO: compléter les affectations et manipulations demandées dans README.md
# Le mot clé TODO est un marqueur de tâche dans les commentaires, il est affiché par l'interpréteur et met en évidence.


a_entier = 5  # TODO: un int
b_flottant = 5.5  # TODO: un float
c_chaine = "elephant"  # TODO: une str

# une list (les crochets [] sont utilisés pour les listes)

liste =  ["numero1", "numero2", "numero3"]# TODO: une list

# un tuple (les parenthèses () sont utilisées pour les tuples)

mon_tuple = ("valeur1, valeur2")  # TODO: un tuple

# un dict (les accolades {} avec des paires clé:valeur)

mon_dict = {"object": "velo",
            "couleur": "rouge",
            "prix": 120,
            "en_stock":True}  # TODO: un dict

if __name__ == "__main__": #if __name__ (c'est a dire : si ce nom du fichier) == (est égal a) "__main__" (le nom programme principal)
    print(f"Valeurs: {a_entier}, {b_flottant}, {c_chaine}, {liste}, {mon_tuple}, {mon_dict}")
    print("Types:", type(a_entier), type(b_flottant), type(c_chaine), type(liste), type(mon_tuple), type(mon_dict))


