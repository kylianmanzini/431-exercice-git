# 15 — Commentaires

# TODO: ajouter des commentaires pertinents dans les fonctions ci-dessous

def somme(a, b):
    """
    
    Fonction qui calcule la somme de 2 nombres
    
    :param a: premier nombre
    :param b: deuxième nombre
    """
    
    # Vérifier si les paramètres sont bien des nombres (entiers, flottants, complexes)
    if isinstance(a, (int, float, complex)) and isinstance(a, (int, float, complex)):
        # Faire la somme et retourner le résultat
        return a + b


if __name__ == "__main__":
    print(somme(2, 3))
