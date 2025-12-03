# 06 — Conditions

# TODO: lire une note (float) et afficher la mention avec if/elif/else.

if __name__ == "__main__":
    note = None
    # TODO

note=float(input("Quelle est la note:"))

if   note <4:
        print("Insuffisant")
elif note <5.5:
        print("Moyen")
else:
        print("Bien")

