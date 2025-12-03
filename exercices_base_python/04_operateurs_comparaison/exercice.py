# 04 — Comparaisons et booléens

x = 10
y = 5

# TODO: compléter
egal = x == y  # 10 == 5 -> False
different = x != y  # 10 != 5 -> True
plus_grand = x > y  # 10 > 5 -> True
logique = (x > y) and (y > 0)  # (10 > 5) and (5 > 0) -> True and True -> True

if __name__ == "__main__":
    print("Comparaisons de base:")
    print("egal:", egal, different, plus_grand)
    print("Expression logique:", logique)

    # Autres exemples d'opérateurs de comparaison
    print("\nAutres opérateurs de comparaison:")
    print("x >= y:", x >= y)  # 10 >= 5 -> True
    print("x < y:", x < y)    # 10 < 5 -> False
    print("x <= y:", x <= y)  # 10 <= 5 -> False

    # Autres opérateurs logiques
    print("\nOpérateurs logiques:")
    print("not egal:", not egal)  # not False -> True
    print("(x > y) or (x < 0):", (x > y) or (x < 0))  # True or False -> True
