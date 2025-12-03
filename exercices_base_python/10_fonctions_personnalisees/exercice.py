# 10 — Fonctions personnalisées

# TODO: définir aire_rectangle(l, h) et saluer(nom)

def aire_rectangle(l, h):
    """Calcule l'aire d'un rectangle de longueur l et hauteur h"""
    return l * h

def saluer(nom):
    """Retourne un message de salutation pour le nom donné"""
    return f"Bonjour {nom}, comment allez-vous ?"

def aire_cercle(rayon):
    """Calcule l'aire d'un cercle (paramètre avec valeur par défaut)"""
    import math
    return math.pi * rayon ** 2

def multiplier(a, b=2):
    """Multiplie deux nombres (b a une valeur par défaut)"""
    return a * b

def additionner(*args):
    """Additionne un nombre variable d'arguments"""
    return sum(args)

if __name__ == "__main__":
    print("Aire rectangle 3x4:", aire_rectangle(3, 4))
    print("Aire rectangle 5x2:", aire_rectangle(5, 2))
    print()
    print(saluer("Alice"))
    print(saluer("Bob"))
    print()

    print("Exemples supplémentaires:")
    print("Aire cercle rayon 3:", round(aire_cercle(3), 2))
    print("Multiplier 5*2:", multiplier(5))
    print("Multiplier 5*3:", multiplier(5, 3))
    print("Additionner 1+2+3+4:", additionner(1, 2, 3, 4))
