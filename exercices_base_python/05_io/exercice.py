# 05 — Entrées / sorties

# TODO: demander un nom et un âge (avec input), convertir l'âge en int, puis afficher.

if __name__ == "__main__":
    nom = input("Entrez votre nom: ")  # Demande le nom (retourne une chaîne)
    age_str = input("Entrez votre âge: ")  # Demande l'âge (retourne une chaîne)
    age = int(age_str)  # Convertit l'âge en entier

    print("Bonjour", nom, "— âge:", age)
