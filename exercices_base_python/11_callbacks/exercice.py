# 11 — Callbacks

# TODO: implémenter appliquer(nums, f)

def appliquer(nums, f):
    """Applique la fonction f à chaque élément de nums et retourne la liste des résultats"""
    resultats = []
    for num in nums:
        resultats.append(f(num))
    return resultats

def carre(x):
    """Fonction classique pour calculer le carré"""
    return x ** 2

def est_pair(x):
    """Fonction qui retourne True si x est pair"""
    return x % 2 == 0

if __name__ == "__main__":
    print("Multiplier par 2:", appliquer([1,2,3], lambda x: x * 2))
    print("Calculer carrés:", appliquer([1,2,3,4], carre))
    print("Vérifier pairs:", appliquer([1,2,3,4,5], est_pair))

    # Exemple avec une fonction définie ailleurs
    import math
    print("Racine carrée:", [round(x, 2) for x in appliquer([1,4,9,16], math.sqrt)])
