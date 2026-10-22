print("======EXO : COMPTER LES VOYELLES D'UNE PHRASE=======================")


def compter_voyelles(texte):
    voyelles = "aeiouyàâêîôûäëïöüéè"
    compteur = 0
    for caractere in texte.lower():
        if caractere in voyelles:
            compteur += 1
    return compteur


def demander_choix():
    while True:
        print("\n 1. Analyser une phrase")
        print("2. Quitter")

        try:
            choix = int(input("Votre choix : "))
            if choix == 1 or choix == 2:
                return choix
            else:
                print("Erreur : choix invalide.")
        except ValueError:
            print("Erreur : merci de choisir 1 ou 2.")


def lancer_programme():
    while True:
        choix = demander_choix()

        if choix == 1:
            phrase = input("Veuillez saisir une phrase : ")

            if phrase.strip() == "":
                print("Erreur : la phrase ne peut pas être vide.")
            else:
                nombre = compter_voyelles(phrase)
                print(f"Le nombre de voyelles dans la phrase est : {nombre}")
        elif choix == 2:
            print("Au revoir !")
            break

