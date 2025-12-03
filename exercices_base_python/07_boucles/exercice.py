# 07 — Boucles

# TODO: implémenter une somme avec for et un petit jeu avec while.

def somme_1_a_n(n):
    """Calcule la somme des nombres de 1 à n en utilisant une boucle for"""
    somme = 0
    for i in range(1, n + 1):  # range(1, n+1) donne 1, 2, 3, ..., n
        somme += i
    return somme

def jeu_devinette():
    """Jeu où l'utilisateur doit deviner un nombre secret entre 1 et 10"""
    import random
    nombre_secret = random.randint(1, 10)
    essais = 0

    print("Devinez le nombre secret entre 1 et 10!")

    while True:  # Boucle infinie jusqu'à ce qu'on trouve
        essais += 1
        proposition_str = input("Votre proposition: ")
        proposition = int(proposition_str)

        if proposition == nombre_secret:
            print(f"Bravo! Vous avez trouvé en {essais} essais.")
            break
        elif proposition < nombre_secret:
            print("Trop petit!")
        else:
            print("Trop grand!")

if __name__ == "__main__":
    print("Somme 1..5 =", somme_1_a_n(5))
    print("Somme 1..10 =", somme_1_a_n(10))

    # Lancer le jeu (commenté pour éviter l'interaction automatique)
    # jeu_devinette()
