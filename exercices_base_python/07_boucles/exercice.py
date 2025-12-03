# 07 — Boucles

# TODO: implémenter une somme avec for et un petit jeu avec while.

def somme_1_a_n(n):
    # TODO


    for i in range(1, 9):
        secret = 8
        essai = None
    while essai != secret:
        essai = int(input("Devine: "))
    print("Bravo!")


if __name__ == "__main__":
    print("Somme 1..5 =", somme_1_a_n(5))

