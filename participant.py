participants = []  # Crée une liste vide pour stocker les participants

def ajouter_participant():  # Fonction qui permet d'ajouter un participant
    nom = input("Nom du participant : ").strip().title()  # Demande le nom, retire les espaces et met les majuscules
    if nom == "":  # Vérifie si le nom est vide
        print("Le nom ne peut pas être vide.")  # Affiche un message d'erreur
    elif nom.lower() in [p.lower() for p in participants]:  # Vérifie si le nom existe déjà, sans tenir compte des majuscules
        print("Ce participant existe déjà.")  # Informe que le participant est déjà inscrit
    else:  # Si le nom est valide et n'existe pas encore
        participants.append(nom)  # Ajoute le nom à la liste
        print("Participant ajouté :", nom)  # Confirme l'ajout

def afficher_participants():  # Fonction qui affiche tous les participants
    if len(participants) == 0:  # Vérifie si la liste est vide
        print("Aucun participant pour le moment.")  # Affiche un message si personne n'est inscrit
    else:  # Si la liste contient des participants
        print("Liste des participants :")  # Affiche le titre de la liste
        for participant in participants:  # Parcourt chaque participant de la liste
            print("-", participant)  # Affiche le nom du participant

def rechercher_participant():  # Fonction qui recherche un participant
    recherche = input("Nom à rechercher : ").strip().lower()  # Demande un nom et le met en minuscules
    if recherche == "":  # Vérifie si la recherche est vide
        print("La recherche ne peut pas être vide.")  # Affiche un message d'erreur
    else:  # Si la recherche n'est pas vide
        trouves = [p for p in participants if recherche in p.lower()]  # Garde les noms contenant le texte recherché
        if len(trouves) > 0:  # Vérifie si au moins un résultat existe
            for participant in trouves:  # Parcourt les résultats trouvés
                print("Participant trouvé :", participant)  # Affiche chaque résultat
        else:  # Si aucun résultat n'a été trouvé
            print("Aucun participant trouvé.")  # Informe l'utilisateur

def supprimer_participant():  # Fonction qui supprime un participant
    nom = input("Nom à supprimer : ").strip().lower()  # Demande le nom et le met en minuscules
    for participant in participants:  # Parcourt la liste des participants
        if participant.lower() == nom:  # Vérifie si le nom correspond, sans tenir compte de la casse
            participants.remove(participant)  # Supprime le participant de la liste
            print("Participant supprimé :", participant)  # Confirme la suppression
            return  # Arrête la fonction après la suppression
    print("Ce participant n'existe pas.")  # S'affiche si aucun nom ne correspond

def menu():  # Fonction principale qui affiche le menu
    while True:  # Répète le menu jusqu'à ce que l'utilisateur quitte
        print("\n=== Gestion des participants ===")  # Affiche le titre du menu
        print("1. Ajouter un participant")  # Affiche le choix 1
        print("2. Afficher les participants")  # Affiche le choix 2
        print("3. Rechercher un participant")  # Affiche le choix 3
        print("4. Supprimer un participant")  # Affiche le choix 4
        print("5. Quitter")  # Affiche le choix 5

        try:  # Essaie de récupérer un choix valide
            choix = int(input("Votre choix : "))  # Demande le choix et le convertit en entier
        except ValueError:  # Se déclenche si l'utilisateur ne saisit pas un nombre entier
            print("Veuillez entrer un nombre.")  # Affiche un message d'erreur
            continue  # Recommence la boucle et réaffiche le menu

        if choix == 1:  # Si l'utilisateur choisit 1
            ajouter_participant()  # Appelle la fonction d'ajout
        elif choix == 2:  # Si l'utilisateur choisit 2
            afficher_participants()  # Appelle la fonction d'affichage
        elif choix == 3:  # Si l'utilisateur choisit 3
            rechercher_participant()  # Appelle la fonction de recherche
        elif choix == 4:  # Si l'utilisateur choisit 4
            supprimer_participant()  # Appelle la fonction de suppression
        elif choix == 5:  # Si l'utilisateur choisit 5
            print("Au revoir !")  # Affiche un message de départ
            break  # Arrête la boucle while
        else:  # Si le choix n'est pas compris entre 1 et 5
            print("Choix invalide.")  # Informe l'utilisateur que son choix est incorrect

menu()  # Lance le programme en appelant la fonction menu