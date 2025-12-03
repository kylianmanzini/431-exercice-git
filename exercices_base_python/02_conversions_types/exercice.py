# 02 — Conversions de type

val_float = 3.7
val_str_num = "42"
val_str_alpha = "abc"

res_int = int(val_float)        # convertit le float en int → 3
res_float = float(val_str_num)  # convertit la chaîne "42" en float → 42.0
res_str = str(val_float)        # convertit le float en str → "3.7"

if __name__ == "__main__":
    print("Conversions:", res_int, res_float, res_str)
