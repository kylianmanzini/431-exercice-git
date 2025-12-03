# 10 — Fonctions personnalisées

Concepts clés:

- Déclaration avec `def`, paramètres et valeur de retour (`return`).
- Appel de fonction avec arguments positionnels/nommés.

Exemples:

```python
def aire_rectangle(l, h):
    return l * h

def saluer(nom):
    return f"Bonjour {nom}!"

print(aire_rectangle(3, 4))
print(saluer("Alice"))
```

Conseils:

- Documenter brièvement la fonction (docstring) et types attendus.
- Éviter les effets de bord non nécessaires.
