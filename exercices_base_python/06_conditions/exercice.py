# 06 — Conditions

# TODO: lire une note (float) et afficher la mention avec if/elif/else.

if __name__ == "__main__":
    note_str = input("Entrez votre note (entre 0 et 6): ")
    note = float(note_str)  # Convertir en float

    # Évaluation de la mention
    if note < 4:
        mention = "insuffisant"
    elif note <= 5.5:
        mention = "moyen"
    else:  # note >= 5.5
        mention = "bien"

    print(f"Note: {note} - Mention: {mention}")
