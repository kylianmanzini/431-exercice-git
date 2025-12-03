# 05 — Entrées / sorties

# TODO: demander un nom et un âge (avec input), convertir l'âge en int, puis afficher.

if __name__ == "__main__":
    nom = str(input("Nom: "))
    age = int(input("Âge: "))

    print("Bonjour", nom, "— âge:", age)
