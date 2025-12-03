# 13 — Exceptions

# TODO: entourer de try/except

def convertir_en_int(abc):
    try:
        return int(abc)
    except ValueError:
        print("Conversion invalide:", abc)
        return None
    finally:
        pass  # code toujours exécuté


if __name__ == "__main__":
    print(convertir_en_int("123"))
    print(convertir_en_int("abc"))
