print("====== MA BIBLIOTHEQUE ======")
livres = ("Le Petit Prince", "Matilda", "L’Odyssée", "Le Hobbit")

def afficher_livres():
    for livre in livres:
        print(livre)

def rechercher_livre():
    recherche = input("Quel livre recherchez-vous ? ")
    recherche = recherche.strip().lower()

    trouve = False
    for livre in livres:
        if livre.lower() == recherche:
            trouve = True
            print("Livre trouvé :", livre)

    if not trouve:
        print("Livre introuvable.")

while True:
    print("1. Rechercher un livre")
    print("2. Afficher tous les livres")
    print("3. Quitter")
    choix = input("Votre choix : ")
    try:
        choix = int(choix)
    except ValueError:
        print("Veuillez entrer un nombre.")
        continue
    if choix == 1:
        rechercher_livre()
    elif choix == 2:
        afficher_livres()
    elif choix == 3:
        print("Au revoir !")
        break
    else:
        print("Choix invalide. Choisissez 1, 2 ou 3.")


