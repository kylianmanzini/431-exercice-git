# 13 — Exceptions

Concepts clés:

- Les exceptions signalent des erreurs ou situations anormales durant l’exécution.
- Bloc `try`/`except` pour intercepter, `finally` pour exécuter du code de nettoyage.
- Lever une exception avec `raise` pour expliciter une erreur.

Exemples:

```python
def convertir_en_int(s):
    try:
        return int(s)
    except ValueError:
        print("Conversion invalide:", s)
        return None
    finally:
        pass  # code toujours exécuté

# Lever une exception personnalisée
def racine_carre(x):
    if x < 0:
        raise ValueError("x doit être >= 0")
    return x ** 0.5
```

Conseils:

- Intercepter uniquement les exceptions attendues (spécifiques), pas un `except:` générique.
- Fournir des messages d’erreur clairs et utiles.
