# Exercice d'utilisation de Git et GitHub

## Etape 1: Cloner le dépôt
Cloner le dépôt GitHub sur votre machine locale en utilisant la commande git clone suivie de l'URL du dépôt.

## Etape 2: Créer une nouvelle branche
Créer une nouvelle branche pour votre travail avec la commande git checkout -b nom_de_votre_branche.

*Votre branche doit suivre la convention de nommage: nom_prenom*

Utilisez la commande `git push` pour pousser la branche sur le dépôt distant après l'avoir créée localement.

### Etape 3: Faire des modifications et pusher vos commits

Le but est de faire un exercice de python, puis de commiter vos modifications sur votre branche.
Vous pouvez donc modifier les fichiers dans le dossier `exercices_base_python` et séparer vos modifications en plusieurs commits logiques par dossier d'exercice.

*Attention à faire des commits clairs et concis, avec des messages explicites.*

Utilisez les commandes `git add`, `git commit` et `git push` pour enregistrer vos modifications.

Attention à ne commiter que les fichiers que vous avez modifiés.

Tips :
- `git status` pour vérifier les fichiers modifiés avant de commiter. 
- `git add <fichier>` pour ajouter un fichier spécifique. `git add .` pour ajouter tous les fichiers modifiés.
- `git commit -m "Message de commit"` pour enregistrer les modifications avec un message descriptif.

Lorsque vous avez terminé vos modifications et vos commits, pousser votre branche sur le dépôt distant avec la commande `git push`.

# Exercices: Validation des bases Python

Ce module regroupe des exercices progressifs pour valider les notions de base en Python. Chaque dossier contient:
- `README.md`: théorie synthétique, objectifs et consignes.
- `exercice.py`: squelette à compléter avec TODOs et un petit lanceur.

## Plan des exercices
1. Variables
2. Conversions de type
3. Opérateurs arithmétiques
4. Opérateurs de comparaison et booléens
5. Entrées / sorties (`input`, `print`)
6. Conditions (`if`, `elif`, `else`)
7. Boucles (`while`, `for`)
8. Fonctions primitives (built-ins)
9. `break`, `continue`, `pass`
10. Fonctions personnalisées (`def`, `return`, paramètres)
11. Callbacks (fonctions passées en argument)
12. f-strings (formatage)
13. Exceptions (`try` / `except` / `finally`)
14. Modules personnalisés (`import`)
15. Commentaires et portée des variables

## Démarrage rapide
Exécuter un exercice:
```bash
python exercices_base_python/01_variables/exercice.py
```

Valider tous les exercices manuellement: parcourez chaque dossier, lisez `README.md`, lisez `theorie.md` et complétez `exercice.py` et exécutez.

Bon apprentissage !
