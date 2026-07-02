import time
import random

def simuler_recherche_marges():
    print("=== Lancement du Robot-Gratteur-Marges ===")
    print("Connexion aux serveurs de prix en cours...")
    time.sleep(2)
    
    # Simulation de scraping sur des catégories de produits porteurs
    produits = ["Veste Technique", "Montre Chronographe", "Lunettes en Acétate", "Sneakers Édition Limitée"]
    
    prod = random.choice(produits)
    prix_grossiste = random.randint(15, 45)
    prix_marche = prix_grossiste + random.randint(40, 120)
    marge = prix_marche - prix_grossiste
    
    print(f"\n[ALERTE MARGE TROUVÉE]")
    print(f"Produit : {prod}")
    print(f"Prix Grossiste : {prix_grossiste} €")
    print(f"Prix de Revente : {prix_marche} €")
    print(f"Marge Brute : {marge} € disponible !")
    print("==========================================")

if __name__ == "__main__":
    simuler_recherche_marges()
