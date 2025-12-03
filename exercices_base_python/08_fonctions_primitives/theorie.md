# 08 — Fonctions primitives (built-ins)

Concepts clés:

- Les fonctions natives de Python offrent des utilitaires essentiels: `abs`, `bool`, `dict`, `float`, `input`, `int`, `len`, `list`, `max`, `min`, `range`, `round`, `print`, `str`, `tuple`, `type`.

Exemples:

```python
valeurs = [3, -1, 7]
print(abs(-5))          # 5
print(len(valeurs))     # 3
print(max(valeurs))     # 7
print(round(3.14159, 2))# 3.14
print(type((1, 2)))     # <class 'tuple'>
```

Conseils:

- Connaître les signatures et retours pour éviter les erreurs.
- `input()` retourne une chaîne: convertir si nécessaire (`int`, `float`).
