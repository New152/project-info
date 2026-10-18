# Brique 2 — Le catalogue se souvient

## Thème

Un petit catalogue de produits en ligne de commande. Chaque produit est enregistré dans un dictionnaire avec son prix et sa quantité en stock.

## Fonctionnalités

- Afficher les produits, les ajouter ou les modifier, et en chercher un par son nom.
- Charger le catalogue JSON au démarrage ; si le fichier n'existe pas encore, commencer avec un dictionnaire vide.
- Enregistrer et recharger les données au format JSON et CSV.
- Refuser les prix et quantités invalides grâce à `try / except ValueError`.
- Exporter le CSV avec un en-tête (`nom, prix, quantite`).

## Lancer le programme

Ouvrez `produit.py` dans VS Code et utilisez **Run Python File**. Le programme crée `produits.json` et `produits.csv` dans le dossier courant quand vous enregistrez ou exportez.

Au démarrage, les données JSON sont chargées automatiquement. L'option 4 recharge les données depuis le CSV ; les options 5 et 6 enregistrent respectivement en JSON et en CSV. L'option 7 enregistre en JSON puis quitte.

## Notions utilisées

Le code s'appuie sur les variables et types, les dictionnaires, les conditions, les boucles `for` et `while`, les fonctions, `input()` et `print()` de la Séance 1 ; et sur `with open()`, l'encodage UTF-8, `csv`, `json.dump()`, `json.load()` et `try / except` de la Séance 2.

## Travail Git de l'équipe

Suivez le cycle présenté dans le fascicule : synchroniser avant de commencer, travailler sur une branche `feature/...`, indexer les fichiers avec `git add`, enregistrer un commit clair avec `git commit -m "..."`, puis pousser la branche avec `git push -u origin ...`. Proposez ensuite une Pull Request pour la relecture et la fusion dans `main`.
