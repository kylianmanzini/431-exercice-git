# 10 — Fonctions personnalisées

# TODO: définir aire_rectangle(l, h) et saluer(nom)

def aire_rectangle(l, h):
    return l*h

def saluer(nom):
    return str(f"Bonjour {nom} !")

if __name__ == "__main__":
    print(aire_rectangle(3, 4))
    print(saluer("Alice"))
