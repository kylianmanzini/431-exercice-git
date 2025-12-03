# 08 — Fonctions primitives (built-ins)

# TODO: appeler plusieurs built-ins et afficher leurs résultats

data = [3, -1, 7]
res = {
    "abs_-1": abs(-1),  # Valeur absolue de -1 = 1
    "len_data": len(data),  # Longueur de la liste = 3
    "max_data": max(data),  # Maximum de la liste = 7
    "type_tuple": type((1, 2, 3)),  # Type d'un tuple = <class 'tuple'>
}

if __name__ == "__main__":
    print("Fonctions primitives de base:")
    print(res)

    print("\nAutres exemples de fonctions primitives:")
    print("min(data):", min(data))  # Minimum de la liste = -1
    print("round(3.7):", round(3.7))  # Arrondi = 4
    print("bool(0):", bool(0))  # False
    print("bool(5):", bool(5))  # True
    print("str(42):", str(42))  # Conversion en string
    print("int('42'):", int('42'))  # Conversion en int
    print("float('3.14'):", float('3.14'))  # Conversion en float
    print("list('abc'):", list('abc'))  # Conversion string en liste
    print("tuple([1,2,3]):", tuple([1,2,3]))  # Conversion liste en tuple
    print("dict([('a',1), ('b',2)]):", dict([('a',1), ('b',2)]))  # Conversion en dict
