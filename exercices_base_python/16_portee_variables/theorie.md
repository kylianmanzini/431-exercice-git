# 16 — Portée des variables

Concepts clés:

- Portée locale: noms définis dans une fonction, visibles seulement à l’intérieur.
- Portée globale: noms au niveau module, visibles partout dans le module.
- `global` pour modifier une variable globale, `nonlocal` pour modifier une variable d’une closure.

Exemples:

```python
x = 10  # globale

def lire_globale():
    return x

def modifier_globale():
    global x
    x = 42

def outer():
    y = 5
    def inner():
        nonlocal y
        y = 6
    inner()
    return y
```

Conseils:

- Limiter l’usage de `global`; préférer passer des paramètres/retours.
- Utiliser `nonlocal` pour closures quand approprié.
