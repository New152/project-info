import csv
import json

FICHIER_JSON = "produits.json"
FICHIER_CSV = "produits.csv"

def charger_json(chemin):
    try:
        f = open(chemin, "r", encoding="utf-8")
        produits = json.load(f)
        f.close()
        return produits
    except FileNotFoundError:
        print("Le fichier JSON n'existe pas encore, on commence avec un dico vide.")
        return {}

def charger_csv(chemin):
    produits = {}
    try:
        f = open(chemin, "r", newline="", encoding="utf-8")
        lecteur = csv.DictReader(f)
        for ligne in lecteur:
            produits[ligne["nom"]] = {
                "prix": float(ligne["prix"]),
                "quantite": int(ligne["quantite"])
            }
        f.close()
    except FileNotFoundError:
        print("Le fichier CSV n'existe pas.")
    except ValueError:
        print("Erreur dans les données du CSV.")
        return {}
    return produits

def sauvegarder_json(chemin, produits):
    f = open(chemin, "w", encoding="utf-8")
    json.dump(produits, f, ensure_ascii=False, indent=2)
    f.close()
    print("Sauvegarde JSON réussie !")

def sauvegarder_csv(chemin, produits):
    f = open(chemin, "w", newline="", encoding="utf-8")
    writer = csv.writer(f)
    writer.writerow(["nom", "prix", "quantite"])
    for nom in produits:
        writer.writerow([nom, produits[nom]["prix"], produits[nom]["quantite"]])
    f.close()
    print("Export CSV réussi !")

def afficher_produits(produits):
    if len(produits) == 0:
        print("Le catalogue est vide !")
    else:
        print("\n--- LISTE DES PRODUITS ---")
        for nom in produits:
            prix = produits[nom]["prix"]
            qte = produits[nom]["quantite"]
            print(nom, ":", prix, "DT -", qte, "en stock")

def ajouter_produit(produits):
    nom = input("Nom du produit : ")
    
    while True:
        try:
            prix = float(input("Prix : "))
            if prix >= 0:
                break
            print("Le prix doit être positif.")
        except ValueError:
            print("Erreur : veuillez saisir un nombre valide.")
            
    while True:
        try:
            quantite = int(input("Quantité : "))
            if quantite >= 0:
                break
            print("La quantité doit être positive.")
        except ValueError:
            print("Erreur : veuillez saisir un nombre entier valide.")
            
    produits[nom] = {"prix": prix, "quantite": quantite}
    print("Produit ajouté avec succès !")

def chercher_produit(produits):
    nom = input("Quel produit cherchez-vous ? ")
    if nom in produits:
        infos = produits[nom]
        print(nom, ":", infos["prix"], "DT -", infos["quantite"], "en stock")
    else:
        print("Produit introuvable.")

def main():
    produits = charger_json(FICHIER_JSON)

    while True:
        print("\n=== MENU ===")
        print("1. Afficher les produits")
        print("2. Ajouter ou modifier un produit")
        print("3. Chercher un produit")
        print("4. Charger depuis le CSV")
        print("5. Enregistrer en JSON")
        print("6. Exporter en CSV")
        print("7. Quitter")
        
        choix = input("Votre choix : ")

        if choix == "1":
            afficher_produits(produits)
        elif choix == "2":
            ajouter_produit(produits)
        elif choix == "3":
            chercher_produit(produits)
        elif choix == "4":
            produits = charger_csv(FICHIER_CSV)
            print("Chargement CSV terminé.")
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
