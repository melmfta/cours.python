nom_etudiant = "Timothée"
note_1 = 11.5
note_2 = 8.0
note_3 = 13.0

print("Etudiant : ", nom_etudiant)
print("Notes : ", note_1, note_2, note_3)

#calculs :
nombre_de_notes = 3
somme_des_notes = note_1 + note_2 + note_3
moyenne = somme_des_notes / nombre_de_notes

#comparaison : le résulat est un boolean
est_admis = moyenne >= 10

#affichage des résultats :
print("Etudiant : ", nom_etudiant)
print("Somme des notes : ", somme_des_notes)
print("Moyenne : ", moyenne)
print("Admis : ", est_admis)

#vérification du typage :
print("Type de 'nom_etudiant' ; ", type (nom_etudiant))
print("Type de 'somme_des_notes' : ", type(somme_des_notes))
print("Type de 'moyenne' : ", type(moyenne))
print("Type de 'est_admis' : ", type(est_admis))


print("=====CARNET DE NOTES=====")
nom_etudiant = input("Nom de l'étudiant : ")
note_1 = float(input("Note 1 (sur 20) : ").replace(",", "."))
note_2 = float(input("Note 2 (sur 20) : ").replace(",", "."))
note_3 = float(input("Note 3 (sur 20) : ").replace(",", "."))

nombre_de_notes = 3
moyenne = (note_1 + note_2 + note_3) / nombre_de_notes

print(f"Etudiant : ", nom_etudiant)
print(f"Notes : {note_1:.2f}, {note_2:.2f}, {note_3:.2f}")
print(f"Moyenne : {moyenne:.2f}")

#validité des notes : une note est valide si elle est compris entre 0 et 20
notes_valides = (0 <= note_1 <= 20) and (0 <= note_2 <= 20) and (0 <= note_3 <= 20)

if not notes_valides :
    print("Erreur : une ou plusieurs notes be sont pas valides doivent être compreise entre 0 et 20")
else :
    moyenne = (note_1 + note_2 + note_3) / 3
    # affficher la mention
    if moyenne >= 16 :
        mention = "Très bien"
    elif moyenne >= 14 :
        mention = "Bien"
    elif moyenne >= 12 :
        mention = "Assez bien"
    elif moyenne >= 10 :
        mention = "Passable"
    else :
        mention = "Insuffisante"
        
    print(f"Etudiant : {nom_etudiant}")
    print(f"Notes : {note_1:2f}, {note_2:.2f}, {note_3:.2f}")
    print(f"Moyenne : {moyenne:.2f}")
    
    if est_admis :
        print("Décision : Admis")
    else  :
        print("Décision : Refusé")
        
print("----BOUCLES----")
nom_etudiant = input("Nom de l'étudiant : ")
# accumulateurs :
somme_des_notes = 0.0
nombre_de_notes = 0

choix = ""
while choix != "0" :
    print()
    print("1 : ajouter une note")
    print("3 : afficher le bulletin")
    print("0 : quitter")
    choix = input("Votre choix : ")
    
    if choix == "1" :
        note = float(input("Saisir une note (sur 20) : ").replace(",", "."))
        somme_des_notes += note
        nombre_de_notes += 1
        print(f"Note {note:.2f} enregistrée")
    elif choix == "3":
        if nombre_de_notes == 0 :
            print("Aucune note enregistrée.")
        else :
            moyenne = somme_des_notes / nombre_de_notes
            print(f"Bulletin de {nom_etudiant} : ")
            print(f"Nombre de notes {nombre_de_notes} : ")
            print(f"Moyenne {moyenne:.2f}/20")
    elif choix == "0" :
        print("Au revoir !")
    else :
        print("Choix invalide : tapez 1, 3 ou 0.")
    
  


note_min = 20.0
note_max = 0.0
compteur = 0
while compteur < 3:
    note = float(input("Saisis une note : "))
    while note < 0 or note > 20:
        print("Note invalide !")
        note = float(input("Recommence : "))
    if note < note_min:
        note_min = note
    elif note > note_max:
        note_max = note
    else:
        print("Note comprise entre le minimum et le maximum.")
    compteur += 1
print("Note minimale :", note_min)
print("Note maximale :", note_max)

note_minimale = 20.0
note_maximale = 0.0
quantite = int(input("Combien de notes ? "))
for numero in range(1, quantite + 1):
    note = float(input("Saisis une note : "))
    while note < 0 or note > 20:
        print("Note invalide !")
        note = float(input("Recommence : "))
    if note < note_minimale:
        note_minimale = note
    if note > note_maximale:
        note_maximale = note
print("Note minimale :", note_minimale)
print("Note maximale :", note_maximale)
