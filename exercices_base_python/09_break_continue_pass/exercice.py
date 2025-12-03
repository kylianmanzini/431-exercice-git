# 09 — break, continue, pass

# TODO: illustrer break/continue/pass

def rechercher_premier_pair(nums):
    # TODO: utiliser continue et break
    for num in nums:
        if num % 2 != 0:
            continue
        else:
            break
    return num

def a_implementer_plus_tard():
    # TODO: laisser pass
    pass

if __name__ == "__main__":
    print(rechercher_premier_pair([1,3,5,8,9]))
