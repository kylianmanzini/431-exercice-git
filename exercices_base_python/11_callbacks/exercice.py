# 11 — Callbacks

# TODO: implémenter appliquer(nums, f)

def appliquer(nums, f):
    new_list = []
    for i in nums:
        new_list.append(f(i))
    return new_list

if __name__ == "__main__":
    print(appliquer([1,2,3], lambda x: x * 2))
