# 09 — break, continue, pass

Concepts clés:

- `break` interrompt la boucle immédiatement.
- `continue` saute à l’itération suivante.
- `pass` sert de placeholder (ne fait rien).

Exemples:

```python
for n in [1, 3, 5, 8, 9]:
    if n % 2 != 0:
        continue      # saute les impairs
    print(n)          # affiche 8
    break             # s'arrête après le premier pair
```

Conseils:

- Utiliser `pass` pour esquisser une fonction, à compléter plus tard.
- `break`/`continue` améliorent la lisibilité si utilisés avec parcimonie.
