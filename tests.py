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

