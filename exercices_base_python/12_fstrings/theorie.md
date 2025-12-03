# 12 — f-strings

Concepts clés:

- Les f-strings permettent d’insérer des expressions dans des chaînes: `f"{expr}"`.
- Plus lisible et performant que `format` dans la plupart des cas.

Exemples:

```python
nom = "Alice"
age = 20
annee = 2025 - age
message = f"{nom} a {age} ans (né(e) en {annee})"
print(message)
```

Conseils:

- Utiliser la syntaxe `{var:format}` pour formater (`{x:.2f}` pour 2 décimales).
- Attention aux guillemets et aux accolades littérales (`{{` et `}}`).
