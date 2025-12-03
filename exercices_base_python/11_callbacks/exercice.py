# 11 — Callbacks

# TODO: implémenter appliquer(nums, f)

def appliquer(nums, f):
    # TODO
    for num in nums:
        f(num)
    return num

if __name__ == "__main__":
    print(appliquer([1,2,3], lambda x: x * 2))
