# 09 — break, continue, pass

# TODO: illustrer break/continue/pass

def rechercher_premier_pair(nums):
    """Trouve le premier nombre pair dans une liste en utilisant continue et break"""
    for num in nums:
        if num % 2 != 0:  # Si impair, on passe au suivant (continue)
            continue
        # Si on arrive ici, c'est que le nombre est pair
        return num  # On sort de la fonction avec break implicite du return
    return None  # Si aucun nombre pair trouvé

def a_implementer_plus_tard():
    # TODO: laisser pass
    pass

def exemple_continue():
    """Exemple d'utilisation de continue"""
    print("Nombres pairs seulement:")
    for i in range(1, 11):
        if i % 2 != 0:  # Si impair, on saute
            continue
        print(i, end=" ")
    print()

def exemple_break():
    """Exemple d'utilisation de break"""
    print("Recherche du nombre 7:")
    for i in range(1, 15):
        print(f"Vérification de {i}...")
        if i == 7:
            print("Trouvé!")
            break  # Sort de la boucle
    print("Fin de la recherche")

if __name__ == "__main__":
    print("Premier nombre pair dans [1,3,5,8,9]:", rechercher_premier_pair([1,3,5,8,9]))
    print("Premier nombre pair dans [1,3,5,7,9]:", rechercher_premier_pair([1,3,5,7,9]))

    print("\nExemples supplémentaires:")
    exemple_continue()
    exemple_break()
