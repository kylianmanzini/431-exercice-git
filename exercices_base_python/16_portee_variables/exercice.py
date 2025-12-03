# 16 — Portée des variables

x = 10  # variable globale

def lire_globale():
    """Lit la variable globale x (lecture seule)"""
    return x  # Accès en lecture à la variable globale

def modifier_globale():
    """Modifie la variable globale x en utilisant le mot-clé global"""
    global x  # Déclare que nous allons modifier la variable globale
    x = 20    # Modification de la variable globale

def fonction_locale():
    """Démontre une variable locale"""
    x = 30  # Variable locale, différente de la globale
    print(f"Variable locale x = {x}")
    return x

def fonction_imbriquee():
    """Démontre l'usage de nonlocal dans des fonctions imbriquées"""
    y = 100  # Variable locale à fonction_imbriquee

    def sous_fonction():
        nonlocal y  # Accès à la variable de la fonction parente
        y = 200     # Modification de la variable parente
        print(f"Dans sous_fonction: y = {y}")

    sous_fonction()
    return y

if __name__ == "__main__":
    print("=== Portée des variables ===")
    print(f"Variable globale initiale: x = {x}")

    print(f"\nLecture de la globale: lire_globale() = {lire_globale()}")

    print(f"\nAvant modification: x = {x}")
    modifier_globale()
    print(f"Après modification globale: x = {x}")

    print("
Fonction avec variable locale:")
    fonction_locale()
    print(f"Variable globale inchangée: x = {x}")

    print("
Fonction imbriquée avec nonlocal:")
    resultat = fonction_imbriquee()
    print(f"Résultat final: y = {resultat}")
