# 11 — Callbacks

# TODO: implémenter appliquer(nums, f)

def appliquer(nums, f):
    return [f(x) for x in nums]

def multiplier_par_2(x):
    return x*2

if __name__ == "__main__":
    print(appliquer([1,2,3], lambda x: x * 2))

