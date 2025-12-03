# 15 — Commentaires et portée des variables
"""
Ce module démontre l'utilisation de commentaires selon PEP 8
et l'importance de la portée des variables en Python.
"""

# Constantes globales (convention : majuscules)
TAUX_TVA = 0.20  # Taux de TVA standard en France
DEVISE = "EUR"   # Devise utilisée

def somme(a, b):
    """
    Calcule la somme de deux nombres.

    Args:
        a (int|float): Premier nombre à additionner
        b (int|float): Deuxième nombre à additionner

    Returns:
        int|float: La somme des deux nombres

    Example:
        >>> somme(2, 3)
        5
        >>> somme(1.5, 2.5)
        4.0
    """
    # Calcul simple de la somme
    resultat = a + b
    return resultat

def calculer_prix_ttc(prix_ht):
    """
    Calcule le prix TTC à partir du prix HT en appliquant la TVA.

    Args:
        prix_ht (float): Prix hors taxe

    Returns:
        float: Prix toutes taxes comprises
    """
    # Utilisation de la constante globale TAUX_TVA
    prix_ttc = prix_ht * (1 + TAUX_TVA)
    return round(prix_ttc, 2)  # Arrondi à 2 décimales

def afficher_informations():
    """
    Affiche des informations sur le programme.
    Démonstration de l'accès aux variables globales.
    """
    print(f"Devise utilisée: {DEVISE}")
    print(f"Taux de TVA: {TAUX_TVA * 100}%")

if __name__ == "__main__":
    # Test des fonctions avec commentaires
    print("=== Tests des fonctions ===")
    print(f"somme(2, 3) = {somme(2, 3)}")
    print(f"somme(1.5, 2.5) = {somme(1.5, 2.5)}")

    print("
=== Calcul de prix TTC ===")
    prix_ht = 100.0
    prix_ttc = calculer_prix_ttc(prix_ht)
    print(f"Prix HT: {prix_ht}€")
    print(f"Prix TTC: {prix_ttc}€")

    print("
=== Informations du programme ===")
    afficher_informations()
