# 11 — Callbacks

# TODO: implémenter appliquer(nums, f)

def appliquer(nums, f):
    for num in nums:
        print(f(num))
    return None

if __name__ == "__main__":
    print(appliquer([1,2,3], lambda x: x * 2))
