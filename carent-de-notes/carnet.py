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
note_1 = float(input("Note 1 : (sur 20)")).replace(",", ".")
note_2 = float(input("Note 2 : (sur 20)")).replace(",", ".")
note_3 = float(input("Note 3 : (sur 20)")).replace(",", ".")

nombre_de_notes = 3
moyenne = (note_1 + note_2 + note_3) / nombre_de_notes

print(f"Etudiant : ", nom_etudiant)
print(f"Notes : {note_1:.2f}, {note_2:.2f}, {note_3:.2f}")
print(f"Moyenne : {moyenne:.2f}")