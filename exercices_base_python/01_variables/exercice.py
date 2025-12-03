# 01 — Variables
# TODO: compléter les affectations et manipulations demandées dans README.md

a_entier = int(30)
b_flottant = float(3.5)
c_chaine = "Alice"
liste = [1,3,"pomme",9]
mon_tuple = (3, "pomme",7,3.4)
mon_dict = {"clé":"3"}

liste[2]="kiwi" #remplace pomme par kiwi
print(liste)

print(mon_tuple[1]) #affiche pomme

mon_dict["pomme de terre"]= "raclette" # rajoute la clé-valeur: pomme de terre:raclette
print(mon_dict)


if __name__ == "__main__":

    print("Valeurs:", a_entier, b_flottant, c_chaine, liste, mon_tuple, mon_dict)
    print("Types:", type(a_entier), type(b_flottant), type(c_chaine), type(liste), type(mon_tuple), type(mon_dict))
