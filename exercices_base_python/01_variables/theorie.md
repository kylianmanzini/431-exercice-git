# 01 — Variables

Concepts clés:
- Une variable associe un nom à une valeur en mémoire.
- Python est typé dynamiquement: le type est attaché à la valeur, pas au nom.
- Types de base utiles ici:
  - `int` (entier), `float` (réel), `str` (chaîne)
  - `list` (liste mutable), `tuple` (séquence immuable)
  - `dict` (dictionnaire: clé → valeur)

Bonnes pratiques:
- Noms explicites: `age`, `prix_unitaire`, `notes_eleves`.
- Choisir la structure adaptée: `tuple` pour données fixes, `list` pour collections modifiables.
- Accéder aux éléments: `liste[0]`, `mon_tuple[1]`, `mon_dict["cle"]`.

Exemples rapides:
```python
x = 3          # int
y = 2.5        # float
nom = "Alice"  # str
nums = [1, 2, 3]       # list
coord = (10, 20)       # tuple
info = {"nom": "Alice", "age": 20}  # dict
```
