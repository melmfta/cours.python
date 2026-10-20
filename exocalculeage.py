print("======EXO: le calculateur d'âge ======")
while True :
    try :
        annee_naissance = int(input("Quelle est votre année de naissance ? "))
        if 1900 <= annee_naissance <= 2026 :
            break
        else :
            print("Erreur : veuillez saisir une année entre 1900 et 2026.")
    
    except ValueError :
        print("Erreur : Veuillez saisir un nombre entier pour l'année de naissance.")
    
age = 2026 - annee_naissance
print(f"Vous avez {age} ans.")