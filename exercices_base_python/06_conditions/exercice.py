# 06 — Conditions

# TODO: lire une note (float) et afficher la mention avec if/elif/else.

if __name__ == "__main__":
    note = float(input("Entrez la note (1-6) : "))
    # TODO
    if note < 4:
        print("Insuffisant")
    elif 4 <= note < 5.5:
        print("Moyen")
    elif note >= 5.5:
        print("Bien")