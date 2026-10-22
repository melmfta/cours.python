playlist = []
def ajouter_chanson(playlist):
    titre = input("Entrez le titre de la chanson : ").strip()

    if titre == "":
        print("Erreur : le titre ne peut pas être vide.")
        print()
#verifier si la chanson existe
#any == True, si comparaison vrai
    elif any(chanson.lower() == titre.lower() for chanson in playlist):
        print("Cette chanson existe déjà.")
        print()
    else:
        playlist.append(titre.title())
        playlist.sort()
        print("Chanson ajoutée.")
        print()

def afficher_playlist(playlist):
    if len(playlist) == 0:
        print("La playlist est vide.")
        print()
    else:
        playlist.sort()
        print("\nPlaylist")
#parcourir la liste et numéroter les Chansons
        for numero, chanson in enumerate(playlist, start=1):
            print(f"{numero}. {chanson}")

def rechercher_chanson(playlist):
    titre = input("Entrez le titre ou une partie du titre : ").strip()

    if titre == "":
        print("Erreur : le titre ne peut pas être vide.")
        print()
    elif any(titre.lower() == t.lower() for t in playlist) :
            print(f"{titre.title()} est dans la playlist.")
            print()
    else:
        print(f"{titre.title()} n'est pas dans la playlist.")
        print()

def supprimer_chanson(playlist):
    titre = input("Entrez le titre de la chanson à supprimer : ").strip()

    if titre == "":
        print("Erreur : le titre ne peut pas être vide.")
        print()
    else:
        for chanson in playlist:
            if chanson.lower() == titre.lower():
                playlist.remove(chanson)
                print(f"{chanson} a été supprimée.")
                print()
                break
        else:
            print("Cette chanson n'existe pas dans la playlist.")
            print()

def afficher_menu() :
    while True :
        print("\n === PLAYLIST ===\n")
        print("1. Ajouter une chanson")
        print("2. Afficher la playlist")
        print("3. Rechercher une chanson")
        print("4. Supprimer une chanson")
        print("5. Quitter")
        print()

        try:
            choix = int(input("Votre choix : ").strip())
            print()
            if choix == 1:
                ajouter_chanson(playlist)
            elif choix == 2:
                afficher_playlist(playlist)
            elif choix == 3:
                rechercher_chanson(playlist)
            elif choix == 4:
                supprimer_chanson(playlist)
            elif choix == 5:
                print("Au revoir !")
                print()
                break
            else:
                print("Choix invalide ! Veuillez choisir entre 1, 2, 3, 4 ou 5.")
        except ValueError:
            print("Erreur : veuillez entrer un nombre entier.")
            print()
afficher_menu()