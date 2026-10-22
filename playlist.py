playlist = []  # Crée une liste vide pour stocker les chansons

def ajouter_chanson():  # Crée une fonction pour ajouter une chanson
    titre = input("Titre de la chanson : ").strip().title()  # Demande le titre, enlève les espaces inutiles et met les majuscules
    if titre == "":  # Vérifie si le titre est vide
        print("Le titre ne peut pas être vide.")  # Affiche un message si le titre est vide
    elif titre.lower() in [chanson.lower() for chanson in playlist]:  # Vérifie si le titre existe déjà, sans tenir compte des majuscules
        print("Cette chanson est déjà dans la playlist.")  # Indique que la chanson existe déjà
    else:  # Si le titre est valide et n'existe pas encore
        playlist.append(titre)  # Ajoute la chanson à la liste
        playlist.sort(key=str.lower)  # Trie les chansons par ordre alphabétique
        print("Chanson ajoutée :", titre)  # Confirme l'ajout
        print("Nombre de chansons :", len(playlist))  # Affiche le nombre total de chansons

def afficher_playlist():  # Crée une fonction pour afficher la playlist
    if len(playlist) == 0:  # Vérifie si la liste ne contient aucune chanson
        print("La playlist est vide.")  # Affiche un message si la liste est vide
    else:  # Si la playlist contient des chansons
        print("\n=== Ma playlist ===")  # Affiche le titre de la playlist
        for i, chanson in enumerate(playlist, start=1):  # Parcourt les chansons en leur donnant un numéro à partir de 1
            print(i, "-", chanson)  # Affiche le numéro et le titre de chaque chanson

def rechercher_chanson():  # Crée une fonction pour rechercher une chanson
    recherche = input("Chanson à rechercher : ").strip().lower()  # Demande un titre ou un morceau de titre et le met en minuscules
    if recherche == "":  # Vérifie si la recherche est vide
        print("La recherche ne peut pas être vide.")  
    else: 
        resultats = [chanson for chanson in playlist if recherche in chanson.lower()]  # Garde les chansons contenant le texte recherché
        if len(resultats) > 0:  
            for chanson in resultats: 
                print("Chanson trouvée :", chanson)  
        else: 
            print("Aucune chanson trouvée.")  

def supprimer_chanson():  
    titre = input("Titre à supprimer : ").strip().lower()  
    for chanson in playlist:
        if chanson.lower() == titre:  
            playlist.remove(chanson)  
            print("Chanson supprimée :", chanson)  
            print("Nombre de chansons :", len(playlist))  
            return  
    print("Cette chanson n'existe pas dans la playlist.")  

def menu():  
    while True:  
        print("\n=== Gestion de la playlist ===")  
        print("1. Ajouter une chanson")  
        print("2. Afficher la playlist") 
        print("3. Rechercher une chanson")  
        print("4. Supprimer une chanson")  
        print("5. Quitter") 
        try:  
            choix = int(input("Votre choix : ")) 
        except ValueError:  
            print("Veuillez entrer un nombre.")  
            continue  
        if choix == 1:  # Vérifie si l'utilisateur a choisi 1
            ajouter_chanson()  # Appelle la fonction d'ajout
        elif choix == 2:  # Vérifie si l'utilisateur a choisi 2
            afficher_playlist()  # Appelle la fonction d'affichage
        elif choix == 3:  
            rechercher_chanson()  
        elif choix == 4:  
            supprimer_chanson()  
        elif choix == 5:  
            print("Au revoir !")  
            break  
        else:  
            print("Choix invalide.")  
menu() 
