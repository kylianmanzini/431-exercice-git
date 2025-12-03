# 15 — Commentaires

Concepts clés:

- Les commentaires expliquent le pourquoi, pas l’évidence.
- Docstrings (chaînes en tête de fonctions/classes/modules) documentent l’API.

Exemples:

```python
def somme(a, b):
    """Retourne la somme de a et b.

    Paramètres:
        a (int|float): premier opérande
        b (int|float): second opérande
    """
    # Vérifier types si nécessaire (exemple pédagogique)
    return a + b
```

Conseils:

- Suivre PEP 8: commentaires concis, à jour, sans redondance.
- Préférer des noms de variables explicites pour limiter les commentaires.
