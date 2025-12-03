# 14 — Modules personnalisés

# Import du module personnalisé outils
from outils import carre, cube, est_positif, PI

if __name__ == "__main__":
    print("Utilisation du module outils:")
    print(f"carre(5) = {carre(5)}")
    print(f"cube(3) = {cube(3)}")
    print(f"est_positif(-2) = {est_positif(-2)}")
    print(f"est_positif(5) = {est_positif(5)}")
    print(f"PI = {PI}")

    # Import du module entier
    import outils
    print(f"\nVia import outils: outils.GRAVITE = {outils.GRAVITE}")
