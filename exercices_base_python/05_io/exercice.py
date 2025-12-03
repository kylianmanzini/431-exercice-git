# 05 — Entrées / sorties

# TODO: demander un nom et un âge (avec input), convertir l'âge en int, puis afficher.

if __name__ == "__main__":
    try: 
        nom = str(input("Votre nom svp : "))
        age = int(input("Votre age svp : "))
    except ValueError:
        print("Erreur : Vous avez mis une mauvaise valeur. ")
        quit()
    # TODO
    print("Bonjour", nom, "— âge:", age)
