# 16 — Portée des variables

x = 10  # variable globale

# TODO: écrire une fonction qui lit x, puis une autre qui modifie x avec global

def lire_globale():
    return x

def modifier_globale():
    global x
    x = 33
    return x

if __name__ == "__main__":
    print(lire_globale())
    modifier_globale()
    print(x)
