# 14 — Modules personnalisés

Concepts clés:

- Un module est un fichier Python importable (ex: `outils.py`).
- L’import (`import`, `from ... import ...`) permet de réutiliser du code.

Exemples:

```python
# outils.py
def carre(x):
    return x * x

# exercice.py
from outils import carre
print(carre(5))  # 25
```

Conseils:

- Placer fonctions réutilisables dans des modules dédiés.
- Éviter les imports circulaires; organiser par domaines.
