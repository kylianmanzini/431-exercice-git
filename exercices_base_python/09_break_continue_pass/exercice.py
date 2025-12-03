# 09 — break, continue, pass

# TODO: illustrer break/continue/pass

def rechercher_premier_pair(nums):
    for i in nums:
        if i is int: # Partie inutile, sert juste à utiliser continue
            continue
        if (i%2 == 0):
            break #Mieux de juste faire return i
    return i

def a_implementer_plus_tard():
    pass

if __name__ == "__main__":
    print(rechercher_premier_pair([1,3,5,8,9]))
