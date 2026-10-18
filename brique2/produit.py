import csv
import json
import os

FICHIER_JSON = "produits.json"
FICHIER_CSV = "produits.csv"


def charger_json(chemin):
    if os.path.exists(chemin):
        f = open(chemin, "r", encoding="utf-8")
        produits = json.load(f)
        f.close()
        return produits
    else:
        print("Aucune sauvegarde JSON : le catalogue commence vide.")
        return {}


def charger_csv(chemin):
    produits = {}
    if os.path.exists(chemin):
        f = open(chemin, "r", newline="", encoding="utf-8")
        lecteur = csv.DictReader(f)
        for ligne in lecteur:
            produits[ligne["nom"]] = {
                "prix": float(ligne["prix"]),
                "quantite": int(ligne["quantite"])
            }
        f.close()
    else:
        print("Le fichier CSV n'existe pas encore.")
    return produits


def sauvegarder_json(chemin, produits):
    f = open(chemin, "w", encoding="utf-8")
    json.dump(produits, f, ensure_ascii=False, indent=2)
    f.close()
    print("Catalogue enregistré en JSON.")


def sauvegarder_csv(chemin, produits):
    f = open(chemin, "w", newline="", encoding="utf-8")
    writer = csv.writer(f)
    writer.writerow(["nom", "prix", "quantite"])
    for nom in produits:
        writer.writerow([nom, produits[nom]["prix"], produits[nom]["quantite"]])
    f.close()
    print("Catalogue exporté en CSV.")


def afficher_produits(produits):
    if len(produits) == 0:
        print("Le catalogue est vide.")
    else:
        print("\n--- Catalogue ---")
        for nom in produits:
            print(nom, ":", produits[nom]["prix"], "DT —", produits[nom]["quantite"], "en stock")


def ajouter_produit(produits):
    nom = input("Nom du produit : ")
    prix = float(input("Prix (DT) : "))
    quantite = int(input("Quantité en stock : "))
    produits[nom] = {"prix": prix, "quantite": quantite}
    print(f"Produit '{nom}' enregistré.")


def chercher_produit(produits):
    nom = input("Nom du produit à chercher : ")
    if nom in produits:
        print(nom, ":", produits[nom]["prix"], "DT —", produits[nom]["quantite"], "en stock")
    else:
        print("Produit introuvable.")


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
        choix = input("> ")

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
