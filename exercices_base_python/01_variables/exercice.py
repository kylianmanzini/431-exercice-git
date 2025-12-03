# 01 — Variables
# TODO: compléter les affectations et manipulations demandées dans README.md

a_entier = 42  # un int
b_flottant = 3.14  # un float
c_chaine = "Bonjour Python"  # une str
liste = [1, 2, 3, 4, 5]  # une list
mon_tuple = ("pomme", "banane", "orange")  # un tuple
mon_dict = {"nom": "Alice", "age": 25}  # un dict

# Manipulations demandées dans le README
liste.append(6)  # Modifier la liste (ajouter un élément)
element_tuple = mon_tuple[1]  # Lire un élément du tuple (index 1 = "banane")
mon_dict["ville"] = "Paris"  # Ajouter une clé au dict

if __name__ == "__main__":
    print("Valeurs:", a_entier, b_flottant, c_chaine, liste, mon_tuple, mon_dict)
    print("Types:", type(a_entier), type(b_flottant), type(c_chaine), type(liste), type(mon_tuple), type(mon_dict))
    print("Manipulations:")
    print("Liste modifiée:", liste)
    print("Élément du tuple (index 1):", element_tuple)
    print("Dict avec nouvelle clé:", mon_dict)
