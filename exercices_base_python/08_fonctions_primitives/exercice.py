# 08 — Fonctions primitives (built-ins)

# TODO: appeler plusieurs built-ins et afficher leurs résultats

data = [3, -1, 7]
res = {
    "abs_-1": abs(-1),
    "len_data": len(data),
    "max_data": max(data),
    "type_tuple": type(data),
    "range_data": range(-1,8) ,
    "round": round(3.145259) ,
    "str_data": str(data),
    "bool_data": bool(data)
}
print(data)


if __name__ == "__main__":
    print(res)
