# 07 — Boucles

# TODO: implémenter une somme avec for et un petit jeu avec while.

def somme_1_a_n(n):
    somme = 0
    for i in range(1, n + 1):
        somme += i
    return somme

if __name__ == "__main__":
    print("Somme 1..5 =", somme_1_a_n(5))
    boucle = True
    while boucle:
        entree = input("Entrez 'q' pour quitter, et autre chose pour jouer : \n")
        if entree == 'q':
            print("Jeu terminé.")
            boucle = False
        else:
            print(f"Vous avez entré : {entree}. Rejouez ! (Oui le jeu est nul.)")