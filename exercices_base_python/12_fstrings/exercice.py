# 12 — f-strings

nom = "Alice"
age = 20
annee_courante = 2025

# TODO: construire une chaîne formatée avec f-string
message = f"{nom} a {age} ans (né en {annee_courante - age})"

if __name__ == "__main__":
    print(message)

    # Autres exemples d'utilisation des f-strings
    prix = 19.99
    quantite = 3
    total = prix * quantite

    print(f"\nPrix unitaire: {prix:.2f}€")  # Formatage des décimales
    print(f"Quantité: {quantite}")
    print(f"Total: {total:.2f}€")  # Calcul directement dans la f-string

    # Formatage avec alignement
    print(f"\n{'Produit':<15} {'Prix':>8} {'Qté':>4}")
    print(f"{'Ordinateur':<15} {prix:>8.2f}€ {quantite:>4}")

    # Expressions dans les f-strings
    temperature = 23.5
    print(f"\nLa température est {'chaude' if temperature > 20 else 'froide'} ({temperature}°C)")
