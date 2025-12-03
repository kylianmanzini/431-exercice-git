# 11 — Callbacks

Concepts clés:

- Un callback est une fonction passée en argument à une autre fonction.
- Permet d’appliquer dynamiquement un traitement.

Exemples:

```python
def appliquer(nums, f):
    return [f(x) for x in nums]

print(appliquer([1,2,3], lambda x: x * 2))  # [2, 4, 6]
```

Conseils:

- Les lambdas sont utiles pour des fonctions courtes.
- Privilégier des noms clairs pour les callbacks.
