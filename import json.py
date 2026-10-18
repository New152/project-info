import csv
import json

# ==========================================
# GESTION DES FICHIERS (PERSISTANCE)
# ==========================================

def charger_json(chemin):
    """Charge les données depuis un fichier JSON.
    Retourne un dictionnaire vide si le fichier n'existe pas encore.
    """
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}  # Au tout premier lancement

def sauvegarder_json(chemin, data):
    """Sauvegarde les données au format JSON."""
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def sauvegarder_csv(chemin, data):
    """Exporte les données au format CSV."""
    with open(chemin, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["nom", "prix", "quantite"])  # En-tête
        for nom, info in data.items():
            writer.writerow([nom, info["prix"], info["quantite"]])

# ==========================================
# SAISIE ROBUSTE
# ==========================================

def lire_nombre_entier(message):
    """Demande un entier jusqu'à ce que la saisie soit valide."""
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Ce n'est pas un nombre entier, réessayez.")

def lire_nombre_flottant(message):
    """Demande un nombre décimal jusqu'à ce que la saisie soit valide."""
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Ce n'est pas un nombre valide, réessayez.")

# ==========================================
# FONCTIONNALITÉS PRINCIPALES
# ==========================================

def afficher_produits(produits):
    """Affiche la liste complète des produits enregistrés."""
    if not produits:
        print("\nAucun produit enregistré pour l'instant.")
        return
    print("\n--- Liste des produits ---")
    for nom, info in sorted(produits.items()):
        print(f"- {nom} : {info['prix']} DT | Quantité : {info['quantite']}")

def ajouter_produit(produits):
    """Ajoute ou met à jour un produit."""
    nom = input("\nNom du produit : ").strip()
    if not nom:
        print("Le nom ne peut pas être vide.")
        return
    
    prix = lire_nombre_flottant("Prix (DT) : ")
    quantite = lire_nombre_entier("Quantité en stock : ")
    
    produits[nom] = {"prix": prix, "quantite": quantite}
    print(f"Produit '{nom}' enregistré avec succès.")

def chercher_produit(produits):
    """Cherche un produit par son nom."""
    nom = input("\nNom du produit à chercher : ").strip()
    if nom in produits:
        info = produits[nom]
        print(f"\nTrouvé : {nom} -> {info['prix']} DT | Stock : {info['quantite']}")
    else:
        print(f"\nLe produit '{nom}' est introuvable.")

def supprimer_produit(produits):
    """Supprime un produit de la collection."""
    nom = input("\nNom du produit à supprimer : ").strip()
    if nom in produits:
        del produits[nom]
        print(f"Produit '{nom}' supprimé avec succès.")
    else:
        print(f"Le produit '{nom}' n'existe pas.")

# ==========================================
# BOUCLE DU MENU INTERACTIF
# ==========================================

def main():
    fichier_json = "produits.json"
    fichier_csv = "produits.csv"
    
    # Chargement initial des données enregistrées
    produits = charger_json(fichier_json)

    while True:
        print("\n=== MENU PRODUITS ===")
        print("1) Afficher la collection")
        print("2) Ajouter / Modifier un produit")
        print("3) Rechercher un produit")
        print("4) Supprimer un produit")
        print("5) Exporter en CSV")
        print("6) Sauvegarder et Quitter")
        
        choix = input("> ").strip()
        
        if choix == "1":
            afficher_produits(produits)
        elif choix == "2":
            ajouter_produit(produits)
        elif choix == "3":
            chercher_produit(produits)
        elif choix == "4":
            supprimer_produit(produits)
        elif choix == "5":
            sauvegarder_csv(fichier_csv, produits)
            print(f"Données exportées avec succès dans '{fichier_csv}'.")
        elif choix == "6":
            sauvegarder_json(fichier_json, produits)
            print(f"Sauvegarde effectuée dans '{fichier_json}'. Au revoir !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()