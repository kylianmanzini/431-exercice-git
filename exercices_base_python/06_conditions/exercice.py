# 06 — Conditions

# TODO: lire une note (float) et afficher la mention avec if/elif/else.

if __name__ == "__main__":
    note = 5.5
    if note == 6:
        print("Excellent")
    elif note >= 5:
        print("Bien")
    elif note >= 4:
        print("Assez bien")
    else:
        print("Insuffisant")
