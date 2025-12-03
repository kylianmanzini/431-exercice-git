# 09 — break, continue, pass

# TODO: illustrer break/continue/pass
nums=[1,3,5,8,9]
def rechercher_premier_pair(nums):
    # TODO: utiliser continue et break

    for i in nums:
        if  i % 2 != 0: # si impair
            continue    #on passe au suivant
        #on arrive ici si i est pair
        return i # retourne le premier pair
        break # arrête la boucle mais inutile car return arrete la boucle déjà



def a_implementer_plus_tard(nums):
    # TODO: laisser pass
    pass



if __name__ == "__main__":
    print(rechercher_premier_pair(nums))