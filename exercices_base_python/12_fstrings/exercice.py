# 12 — f-strings

nom = "Alice"
age = 20
annee_courante = 2025

# TODO: construire une chaîne formatée avec f-string
message = f"{nom} a {age} ans (né(e) en {annee_courante-age})"

if __name__ == "__main__":
    print(message)
