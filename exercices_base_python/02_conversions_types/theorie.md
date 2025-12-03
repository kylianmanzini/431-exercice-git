# 02 — Conversions de type

Concepts clés:
- Conversion (casting) entre types: `int()`, `float()`, `str()`, etc.
- Conversion valide vs invalide: `int("42")` OK, `int("abc")` lève `ValueError`.
- Conversion de collections: `list(tuple)`, `tuple(list)`, `dict(list_de_pairs)`.

Exemples:
```python
int(3.7)      # 3
float("2.0") # 2.0
str(42)       # "42"
list((1,2))   # [1, 2]
```

Conseils:
- Convertir les entrées `input()` (toujours des chaînes) avant calcul.
- Entourer les conversions risquées avec `try/except`.
