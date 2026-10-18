# Brique 2 — Le catalogue se souvient

## Thème
Un petit catalogue de produits en ligne de commande développé en Python. Chaque produit est enregistré dans un dictionnaire avec son prix et sa quantité en stock.

## Fonctionnalités
- **Gestion du catalogue** : Afficher les produits, en ajouter ou en modifier, et en chercher un par son nom.
- **Persistance des données** : 
  - Chargement automatique du catalogue au format JSON au démarrage (gestion du premier lancement si le fichier n'existe pas via `FileNotFoundError`).
  - Option pour recharger les données depuis un fichier CSV.
  - Enregistrement en JSON (`json.dump` / `json.load`) et export en CSV avec en-tête (`nom`, `prix`, `quantite`).
- **Robustesse** : Protection contre les saisies invalides (lettres au lieu de nombres, prix/quantités négatifs) grâce au motif `try / except ValueError`.

## Structure du projet
```text
brique2/
├── produit.py       # Le code source principal du programme
├── produits.json    # Fichier de sauvegarde JSON (généré automatiquement)
└── produits.csv     # Fichier d'export CSV (généré automatiquement)
