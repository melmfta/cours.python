# opérateurs arithmétiques
print("7 + 2 = ", 7 + 2)
print("7 - 2 = ", 7 - 2)
print("7 * 2 = ", 7 * 2)
print("7 / 2 = ", 7 / 2)
print("7 % 2 = ", 7 % 2)

# priorité des opérateurs
print("7 + 2 * 3 = ", 7 + 2 * 3)
print("(7 + 2) * 3 = ", (7 + 2) * 3)

#comparaison : résultat boolean
print("7 > 2 = ", 7 > 2)
print("7 < 2 = ", 7 < 2)
print("7 == 2 = ", 7 == 2)
print("7 != 2 = ", 7 != 2)

# arrondi et conversion de type
print("Arrondi de 34.8416281628 : ", round(34.3416281628, 2))
print("Conversion de type : ", int(34.8416281628))
print("Conversion de type : ", float(34))

# aberration de type : flottant
print("0.1 + 0.2 = ", 0.1 + 0.2)
print("0.1 + 0.2 == 0.3 : ", 0.1 + 0.2 == 0.3)

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
moyenne = 11.5
nombre_absences = 4
a_rendu_projet = True

#and : vrai seulement si les deux conditions sont vraies
admis_sans_resevre = moyenne >= 10 and nombre_absences >= 3
print("admis_sans_resevre : ", admis_sans_resevre) # False

# or : vrai si au moins une des conditions est vraie
envoi_alerte = moyenne < 8 or nombre_absences > 3
print("envoi_alerte : ", envoi_alerte) # True

# not : inverse la valeur boléenne
print("Projet manquant : ", not a_rendu_projet) # False

# paranthèses rendent les combinaisons plus lisibles
peut_passer_jury = (moyenne >=10 or a_rendu_projet) and not nombre_absences > 10
print("peut_passer_jury : ", peut_passer_jury) # True

# if / elif / else
# icentation = 4 espaces (recommandation PEP 8 => style officiel de pyhton)
note = float(input("Quelle est la note ? ").replace(",", "."))
if note >= 10 :
    print("Bravo vous avez la moyenne")
    print("Continue comme ça !")
elif note >= 8:
    print("Vous êtes proche de la moyenne")
    print("Il faut un petit effort supplémentaire")
else:
    print("Vous n'avez pas la moyenne")
    print("Il faut travailler davantage")
    
print("Fin du programme")

# condition imbriquées
#v1
if note >= 14 :
    print("Imbrication : bon résultat")
else :
    if note >= 10 :
        print("Imbrication : résultat correct")
    else :
        print("Imbrication : résultat insuffisant")
#v2 : même logique que elif
if note >= 14 :
    print("Avec Elif : bon résultat")
elif note >= 10 :
    print("Avec Elif : résultat correct")
else :
    print("Avec Elif : résultat insuffisant")
    
# and or
# a and b : si a est faux le résultat est faux sans évaluer b
# a or b : si a est vrai le résultat est vrai sans évaluer b
nombre_de_notes = 0
sommes_des_notes = 0.0
if nombre_de_notes > 0 and sommes_des_notes / nombre_de_notes >= 10 :
    print("Moyenne suffisante")
else :
    print("Moyenne insuffisante")
    
est_delegue = True
if est_delegue or sommes_des_notes / nombre_de_notes >= 16 :
    print("Invité au conseil de classe")
    
#if sommes_des_notes / nombre_de_notes >= 10 and nombre_de_notes > 0 :
#    print("Moyenne suffisante et notes présentes")

# truthy & falsy
# fasly : False, None, 0, 0.0, ''
# truthy : tout ce qui n'est pas falsy (ex: True, 1, -1, 'texte', [1,2,3], "0")
print("bool(0) ; ", bool(0)) # False
print("bool(0.0) ; ", bool(0.0)) # False
print("bool('') : ", bool(" ")) # False
print("bool(" ") : ", bool(" ")) # True
print('bool("0") : ", bool("0")') # True
print("bool(1) : ", bool(1)) # True

nom = input("Quel est votre nom ? ")
if nom:
    print("Bonjour", nom)
else : 
    print("Vous n'avez pas saisi votre nom")
    
#while : exécute tant que la condition est vraie
compteur = 1
while compteur <= 5 :
    print("Tour numéro : ", compteur)
    compteur += 1 # sans cette ligne, la boucle ne s'arrête jamais
print("Fin de la boucle. Valeur de compteur : ", compteur)

somme = 0
nombre =  1
while nombre <= 4 :
    somme += nombre
    print(f"Nombre : {nombre}, Somme : {somme}")
    nombre += 1
print("Fin de la boucle. Valeur de nombre : ", nombre)
print("Fin de la boucle. Valeur de somme : ", somme)

note = float(input("Saissisez votre note /20").replace(",", "."))
while note < 0 or note > 20 :
    print("Note invalide. Veuillez saisir une note en tre 0 et 20.")
    note = float(input("Saissaisez votre bote /20").replace(",", "."))
print("Note valide : ", f"{note: .2f}")


# boucle infinie
# compteur = 1
# somme = 0
# while compteur <= 3 :
#      somme += compteur

# print("Somme : ", somme)

# for répete son bloc pour chaque éléments d'une séquence.
# range() : génère une séquence de nombres, ex : range(5) -> 0, 1, 2, 3, 4
# range(fin) : range(0) => -1
# range(début, fin) : range(3, 9) -> 3, 4, 5, 6, 7, 8
# range(début, fin, pas) : range(2, 10, 2) -> 2, 4, 6, 8

for i in range(5) :
    print("Tour numéro : ", i, end=" ")
print()

for note in range(3, 21, 5) :
    print("Note : ", note, end=" ") # 0 5 10 15 20
print()

#3 => -9
nombre = 3
while nombre >= -9:
    print(nombre)
    nombre -= 1
    
# break : permet de sortir immédiatement d'une boucle
# continue : permet de passer immédiatment- à l'itération suivante de la boucle
print('Nombres impairs de 1 à 9')
for iteration in range(1,10) :
    if iteration % 2 == 0 :
        continue # nombre pair, on passe à l'itération suivante
    print(iteration, end=" ") # nombre impair
print()

print('Recherche du premier multiple de 7 à partir de 50 : ')
for nombre in range(50, 100) :
    if nombre % 7 == 0 :
        print('Trouvé : ', nombre)
        break
print('Fin de la recherche.')

while True :
    responseUser = input("Tapez la touche h pour quitter : ")
    if responseUser.lower() == "h" :
        break
print("Fin de la boucle infinie.")

# les boucles imbriquées
# en-tête
print("   ", end="")
for colonne in range(1, 6) :
    print(f" {colonne:>4} ", end="")
print()
print("-" * 24)

for ligne in range(1, 6) :
    print(f"{ligne:>2} | ", end="")
    for colonne in range(1, 6) :
        print(f" {ligne * colonne:>4} ", end="")
    print()
    

# les fonctions
# def : introduit ka définition
# paramètre : valeurs que la fonctiond peut recevoir pour effectuer son traitement
# return : permet d renvoyer une valeur depuis la fonction
def calculer_age(annee_de_naissance) :
    return 2026 - annee_de_naissance


age = calculer_age(1984)
print(f"Vous avez {age} ans.")

# sans paramètre
def faire_des_lignes() :
    print("-" * 40)
    
faire_des_lignes()
faire_des_lignes()
faire_des_lignes()
faire_des_lignes()

# avec paramètre
def faire_des_lignes_avec_param(nb_de_fois) :
    print("-" * nb_de_fois)
    
faire_des_lignes_avec_param(10)
faire_des_lignes_avec_param(20)
faire_des_lignes_avec_param(30)

def carre(nombre) :
    return nombre * nombre

print(carre(5)) # 25
print(carre(10)) # 100
print(carre(0)) # 0

def calculatrice(operante1, operante2, operateur) :
    if operateur == "+" :
        print(operante1 + operante2)
    elif operateur == "-" :
        print(operante1 - operante2)
    elif operateur == "*" :
        print(operante1 * operante2)
    elif operateur == "/" :
        if operante2 != 0 :
            print(operante1 / operante2)
        else :
            print("Erreur : division par zéro.")
    else :
        print("Erreur : opérateur inconnu.")
    
calculatrice (10, 5, "+")
calculatrice (1, 32, "*")
calculatrice (9, 5, "-")
calculatrice (3, 1, "/")
calculatrice (10, 0, "/") # test division par zéro
calculatrice (5, 5, "^") # test opérateur inconnu