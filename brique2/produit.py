import csv
import json

FICHIER_JSON = "produits.json"
FICHIER_CSV = "produits.csv"


def charger_json(chemin):
    """Désérialise le catalogue JSON, ou démarre avec un dictionnaire vide."""
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Aucune sauvegarde JSON : le catalogue commence vide.")
        return {}
    except ValueError:
        print("Le fichier JSON est invalide : le catalogue commence vide.")
        return {}


def charger_csv(chemin):
    """Lit le catalogue CSV et reconstruit son dictionnaire de produits."""
    produits = {}
    try:
        with open(chemin, "r", newline="", encoding="utf-8") as f:
            for ligne in csv.DictReader(f):
                produits[ligne["nom"]] = {
                    "prix": float(ligne["prix"]),
                    "quantite": int(ligne["quantite"]),
                }
    except FileNotFoundError:
        print("Le fichier CSV n'existe pas encore.")
    except ValueError:
        print("Le fichier CSV contient un prix ou une quantité invalide.")
        return {}
    return produits


def sauvegarder_json(chemin, produits):
    """Sérialise le catalogue dans un fichier JSON."""
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(produits, f, ensure_ascii=False, indent=2)
    print("Catalogue enregistré en JSON.")


def sauvegarder_csv(chemin, produits):
    """Exporte le catalogue sous forme de tableau CSV."""
    with open(chemin, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["nom", "prix", "quantite"])
        for nom, informations in produits.items():
            writer.writerow([nom, informations["prix"], informations["quantite"]])
    print("Catalogue exporté en CSV.")


def lire_prix(message):
    """Redemande le prix tant qu'il n'est pas un nombre positif ou nul."""
    while True:
        try:
            prix = float(input(message))
            if prix >= 0:
                return prix
            print("Le prix ne peut pas être négatif.")
        except ValueError:
            print("Saisissez un nombre décimal valide.")


def lire_quantite(message):
    """Redemande la quantité tant qu'elle n'est pas un entier positif ou nul."""
    while True:
        try:
            quantite = int(input(message))
            if quantite >= 0:
                return quantite
            print("La quantité ne peut pas être négative.")
        except ValueError:
            print("Saisissez un nombre entier valide.")


def afficher_produits(produits):
    """Affiche tous les produits du catalogue."""
    if not produits:
        print("Le catalogue est vide.")
        return
    print("\n--- Catalogue ---")
    for nom, informations in produits.items():
        print(f"{nom} : {informations['prix']} DT — {informations['quantite']} en stock")


def ajouter_produit(produits):
    """Ajoute un produit ou met à jour celui qui porte le même nom."""
    nom = input("Nom du produit : ").strip()
    if not nom:
        print("Le nom ne peut pas être vide.")
        return
    prix = lire_prix("Prix (DT) : ")
    quantite = lire_quantite("Quantité en stock : ")
    produits[nom] = {"prix": prix, "quantite": quantite}
    print(f"Produit '{nom}' enregistré.")


def chercher_produit(produits):
    """Recherche un produit par son nom."""
    nom = input("Nom du produit à chercher : ").strip()
    informations = produits.get(nom)
    if informations is None:
        print("Produit introuvable.")
    else:
        print(f"{nom} : {informations['prix']} DT — {informations['quantite']} en stock")


def main():
    produits = charger_json(FICHIER_JSON)

    while True:
        print("\n=== CATALOGUE DE PRODUITS ===")
        print("1) Afficher les produits")
        print("2) Ajouter ou modifier un produit")
        print("3) Chercher un produit")
        print("4) Recharger depuis le CSV")
        print("5) Enregistrer en JSON")
        print("6) Exporter en CSV")
        print("7) Enregistrer et quitter")
        choix = input("> ").strip()

        if choix == "1":
            afficher_produits(produits)
        elif choix == "2":
            ajouter_produit(produits)
        elif choix == "3":
            chercher_produit(produits)
        elif choix == "4":
            produits = charger_csv(FICHIER_CSV)
            print("Catalogue rechargé depuis le CSV.")
        elif choix == "5":
            sauvegarder_json(FICHIER_JSON, produits)
        elif choix == "6":
            sauvegarder_csv(FICHIER_CSV, produits)
        elif choix == "7":
            sauvegarder_json(FICHIER_JSON, produits)
            print("Au revoir !")
            break
        else:
            print("Choix invalide, réessayez.")


main()
