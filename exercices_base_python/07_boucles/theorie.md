# 07 — Boucles

Concepts clés:
- `for` pour itérer sur une séquence (ou `range`).
- `while` pour répéter tant qu’une condition est vraie.

Exemples:
```python
s = 0
for i in range(1, 6):
    s += i

secret = 8
essai = None
while essai != secret:
    essai = int(input("Devine: "))
```

Conseils:
- S’assurer qu’une boucle `while` peut terminer.
- Utiliser `break`/`continue` si nécessaire.
