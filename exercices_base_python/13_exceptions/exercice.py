# 13 — Exceptions

# TODO: entourer de try/except

def convertir_en_int(s):
    # TODO: retourner un int ou None sur erreur
    try:
        return int(s)
    except ValueError:
        return None

if __name__ == "__main__":
    print(convertir_en_int("123"))
    print(convertir_en_int("abc"))
