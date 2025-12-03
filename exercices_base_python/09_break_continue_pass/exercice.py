# 09 — break, continue, pass

# TODO: illustrer break/continue/pass

def rechercher_premier_pair(nums):
    # TODO: utiliser continue et break
    for num in nums:
        if num % 2 != 0:
            continue
        else:
            return num
            break # pas nécessaire ici mais pour l'illustration
    return None

def a_implementer_plus_tard():
    pass

if __name__ == "__main__":
    print(rechercher_premier_pair([1,2,5,8,9]))
