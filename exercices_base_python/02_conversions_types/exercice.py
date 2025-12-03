# 02 — Conversions de type

val_float = 3.7
val_str_num = "42"
val_str_alpha = "abc"

# TODO: convertir en int, float, str selon les consignes
res_int = int(val_float)  # Convertir 3.7 en int -> 3 (troncature)
res_float = float(val_str_num)  # Convertir "42" en float -> 42.0
res_str = str(val_float)  # Convertir 3.7 en str -> "3.7"

if __name__ == "__main__":
    print("Conversions:", res_int, res_float, res_str)

    # Démonstration des cas qui ne marchent pas
    print("\nCas non convertibles:")
    try:
        int(val_str_alpha)  # "abc" ne peut pas être converti en int
    except ValueError as e:
        print(f"int('{val_str_alpha}') lève ValueError: {e}")

    try:
        float(val_str_alpha)  # "abc" ne peut pas être converti en float
    except ValueError as e:
        print(f"float('{val_str_alpha}') lève ValueError: {e}")
