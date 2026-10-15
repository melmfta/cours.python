# saisi avec input()
age_saisi = input("Quel est ton âge ? ")
print("Dans deux ans tu auras : ", int(age_saisi) + 2)

prix = round(float(input("Quel est le prix du produit ?")), 2)
prix_formate = str(prix).replace(".", ",")
print("Prix TTC : ", prix_formate, "€")

#formater avec f-strings
print(f"Prix TTC : {prix_formate} €")

nom = "Melvin"
moyenne = 16.5
nombre_de_notes = 3
print(f"Nom : {nom}, Moyenne : {moyenne}, Nombre de notes : {nombre_de_notes}")

#.2f pour arrondir à 2 décimales
print(f"Nom : {nom}, Moyenne : {moyenne:.2f}, Nombre de notes : {nombre_de_notes}")

# :>10 pour aligner à droite sur 10 caractères
print(f"Nom : {nom:>16}, Moyenne : {moyenne:.2f}, Nombre de notes : {nombre_de_notes}")

# :<10 pour aligner à gauche sur 10 caractères
print(f"Nom : {nom:<17}, Moyenne : {moyenne:.2f}, Nombre de notes : {nombre_de_notes}")

# :^10 pour aligner à gauche sur 10 caractères
print(f"Nom : {nom:^17}, Moyenne : {moyenne:.2f}, Nombre de notes : {nombre_de_notes}")

#les caractères d'échappement
#saut de ligne : \n
print("Ceci est une ligne\nCeci est une autre ligne")

#tabulation : \t
print("Nom\tMoyenne\tNombre de notes")

# guillemets : \" et \'
print("il a dit : \"Bonjour !\"")

# backslash : \\
print("Dossier Windows : c:\\Users\\Melvin")

# conditions et logiques booléens
# == opérateur d'égalité
print("5 == 5 : ", 5 == 5) # True
print("5 == 3 : ", 5 == 3) # False
print("melvin == melvin : ", "melvin" == "melvin") # True
print("melvin == melvin : ", "melvin" == "Melvin") # False => sensible à la casse

# comparaison chainées
note = 15
print("10 <= note 20 : ", 10 <= note <= 20) # True

# différencier = et ==
note_parfaite = note == 20
print("note_parfaite : ", note_parfaite) # False

# conditions and, or, not
moyenne = 11,5
nombre_absences = 4
a_rendu_projet = True

#and : vrai seulement si les deux conditions sont vraies
admis_sans_resevre = moyenne >= 10 and nombre_absences <= 3
print("admis_sans_resevre : ", admis_sans_resevre) # False

# or : vrai si au moins une des conditions est vraie
envoi_alerte = moyenne < 8 or nombre_absences > 3
print("envoi_alerte : ", envoi_alerte) # True

# not : inverse la valeur boléenne
print("Projet manquant : ", not a_rendu_projet) # False

# paranthèses rendent les combinaisons plus lisibles
peut_passer_jury = (moyenne >=10 or a_rendu_projet) and not nombre_absences > 10
print("peut_passer_jury : ", peut_passer_jury) # True
