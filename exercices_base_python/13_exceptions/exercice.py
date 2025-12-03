# 13 — Exceptions

# TODO: entourer de try/except

def convertir_en_int(s):
    try:
        conversion_int = int(s)
    except ValueError:
        return None
    return conversion_int

if __name__ == "__main__":
    print(convertir_en_int("123"))
    print(convertir_en_int("abc"))
