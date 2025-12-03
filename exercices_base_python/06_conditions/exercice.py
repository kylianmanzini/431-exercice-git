# 06 — Conditions

# TODO: lire une note (float) et afficher la mention avec if/elif/else.

if __name__ == "__main__":
    note = 6
    if (1 <= note) and (note < 4):
        print("Insuffisant")
    elif (4 <= note) and (note < 5.5):
        print("Moyen")
    elif (5.5 <= note) and (note <= 6):
        print("Bien")
    else:
        print("Votre note n'est pas entre 1 et 6")
