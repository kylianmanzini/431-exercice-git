# 13 — Exceptions

# TODO: entourer de try/except

def convertir_en_int(s):
    """Convertit une chaîne en int, retourne None si impossible"""
    try:
        return int(s)
    except ValueError:
        print(f"Erreur: '{s}' ne peut pas être converti en entier")
        return None

def diviser_par_zero():
    """Exemple d'exception ZeroDivisionError"""
    try:
        resultat = 10 / 0
        return resultat
    except ZeroDivisionError as e:
        print(f"Erreur de division: {e}")
        return None
    finally:
        print("Cette ligne s'exécute toujours (finally)")

def acceder_liste():
    """Exemple d'exception IndexError"""
    try:
        liste = [1, 2, 3]
        return liste[5]  # Index inexistant
    except IndexError as e:
        print(f"Erreur d'index: {e}")
        return None

if __name__ == "__main__":
    print("Conversion d'entiers:")
    print("convertir_en_int('123'):", convertir_en_int("123"))
    print("convertir_en_int('abc'):", convertir_en_int("abc"))

    print("\nAutres types d'exceptions:")
    diviser_par_zero()
    acceder_liste()
