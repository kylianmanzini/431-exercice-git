# 04 — Comparaisons et booléens

x = 10
y = 5

# TODO: compléter
egal = x == y
different = x != y
plus_grand = x > y
logique = (x>y) and (y>5)  # and signiqfie que les deux conditions doivent être vraies pour obtenir True
logique2 = (x<y) or (y!=4) # or signifie que une des deux conditions doit être vraie pour obtenir True

if __name__ == "__main__":
    print(egal, different, plus_grand, logique, logique2)
