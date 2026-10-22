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


# manipulation de chaînes
mot = 'Python'
print(mot[0]) # affiche le premier caractère P
print(mot[-1]) # affiche le dernier caractère n
print(mot[-2]) # affiche l'avant-dernier caractère o
print(mot[1:4]) # affiche les caractères de l'index 1 à 3 (yht)
print(mot[:3]) # affiche les trois premiers caractères (Pyt)
print(mot[3:]) # affiche les caractères à partir de l'index 3 (hon)

print(len(mot)) # affiche la longueur de la chaîne (6)

# print(mot[9]) => erreur IndexError car l'index 0 n'existe pas dans la chaîne 'Python'
mot[::-1] # 'nohtyP'

# strip() supprime les espaces au début et à la fin d'une chaîne
texte ="    Bonjour    "
print(texte.strip()) # 'Bonjour'
# lower() convertit tous les caractères d'une chaîne en minuscules
print(texte.lower()) # '  bonjour  '
#upper() convertit tous les caractères d'une chaîne en majuscules
print(texte.upper()) # '  BONJOUR  '

#title() : convertit la première lettre de chaque mot en majuscule
prenom = "mark kamte"
print(prenom.title()) # 'Mark Kamte'

#replace() : remplace une sous-chaîne par une autre
texte_modifie = texte.replace("Bonjour", "Bonsoir").strip()
print(texte_modifie) # 'Bonsoir'

# find() : retourne l'index de la première occurence d'une sous-chaîne, ou -1 si elle n'existe pas
phrase = "Bonjour tout le monde"
print(phrase.find("le")) # 12
print(phrase.find("la")) # -1

# in : retourne True si une sous-chaîne est présente dans ka chaîne, False sinon
print("Bonjour" in phrase) # True
print("Python" in phrase) # False

# isdigit() : retourne True si tous les caractères de la chaîne sont des chiffres, False sinon
print("12345".isdigit()) # True
print("123a45".isdigit()) # False

# isalpha() : retourne True si tous les caractères de la chaîne sont des lettres, False sinon
print("abcde".isalpha()) # True
print("abc123".isalpha()) # False

# les liste : collection ordonnée et modifiable
listePrenom = ["Mark", "Alicia", "Thomas", "Sélomey"]
# accéder à un élément de la liste en se référant à son index
print(listePrenom[1]) # affiche le premier de la liste "Mark"
print(listePrenom[-1]) # affiche le dernier de la liste donc "Sélomey"
# slicing : liste[debut:fin]
print(listePrenom[:2]) # affiche les deux derniers de la liste donc "Thomas" et "Sélomey"
print(listePrenom[1:2])

vide = []
print(vide) # affiche []

plusieursTypes = ["Melvin", 25, True, ["jaune", ["orange","citron"],"rouge"]]
print(plusieursTypes[3][0])
print(plusieursTypes[3][1][1])

nouvelExemple = [["Melvin", 23, True, ["jaune", ["raisins", "citron"], "bleu"]], ["Alicia", 30, False, ["bleu", ["vert", "violet"], "noir"]]]
print(nouvelExemple[0][0], "a", nouvelExemple[0][1], "ans, il aime les", nouvelExemple[0][3][1][0], "et sa couleur c'est le", nouvelExemple[0][3][2])
print(nouvelExemple[1][0], "a", nouvelExemple[1][1], "ans, elle aime les couleurs", nouvelExemple[1][3][1][0], nouvelExemple[1][3][0], nouvelExemple[1][3][1][1], "et le", nouvelExemple[1][3][2])


# les méthodes de liste
# ajouter / insère, retirer, remplace des éléments
notes = [12.0, 15.5, 18.25]
print("Départ : ", notes)
# ajouter un élément à la fin de la liste : append()
notes.append(16.0)
print("Après append : ", notes)
# retirer : retire et renvoie ke dernier élément : pop()
derniere = notes.pop()
print(f"pop() a renvoyé {derniere} , reste : {notes}")
premiere = notes.pop()
print(f"pop( a retiré {premiere} , reste :{notes}")
notes.remove(15.5)
print(f"Après remove(15.5)() , reste:{notes}")

# nouvel insertion : insert(index,val)
notes.insert(1,16)
print(f"Après insert(1,16) , reste :{notes}")

# remplacer un élément :
notes[1] = 14.25
print(f"Après remplacement de l'élément, reste :{notes}")

#parcours une liste :
prenoms = ["Mélodie","Timothée","Mark-Erwann","Sélomey","Thomas","Alicia","Coco"]
for prenom in prenoms :
    print(f"{prenom}")

# nombre de valeurs dans une liste
print(len(prenoms)) 

# boucler à partir des index (= indices = clé = key)
for index in range(0,len(prenoms)) :
    print(f"{prenoms[index]}") # affiche les prénoms correspondant aux index 0 1 2 3 4 5
    
# une fonction c'est une économie de code


# les tuples : collections ordonnées et immuable (elle doit se finir par une virgule ,)
exemple_tuple = ("Melvin", 23, True)
print(exemple_tuple[0])
print(exemple_tuple[-1])

uneSeuleValeur = ("Melvin",) # pour créer un tuple avec une seule valeur, il faut mettre une virgule à la fin

date = (22,"octobre",2026)
# déballage : une variable pour chaque élément du tuple
jour, mois, annee = date
print(f"Jour : {jour}, Mois : {mois}, Année : {annee}")

def statistiques(notes) :
    return(sum(notes) / len(notes), max(notes), min(notes))

resultat = statistiques([12.0, 15.5, 18.25])

print(resultat)
moyenne, maximum, minimum = resultat

note_min, note_max, moyenne = statistiques([12.0, 15.5, 18.25])
print(f"Note min : {note_min}, Note max : {note_max}, Moyenne : {moyenne:.2f}")

etudiant = ("Melvin","Tim","Tom")
etudiant[0] # affiche "Melvin"
# etudiant[1] = "Mélodie" => TypeError car les tuples sont immuables

#dictionnaire : collection non ordonné de paires clé-valeur
etudiant = {"prenom" : "Sélomey", "promo" : "B1DEV", "age" : 21}
print(etudiant)
print(etudiant["prenom"])
print(etudiant["promo"])
print(etudiant["age"])
print(f"Dans la promo de {etudiant["promo"]} il y a {etudiant["prenom"]} qui a {etudiant["age"]} ans", )

# tester la présence d'une clé :
print("prenom" in etudiant) # True
print("nom" in etudiant) # False
# get : permet de récupérer la valeur associée à une clé, avec une valeur par défaut si la clé n'existe pas
print(etudiant.get("prenom")) # Sélomey
print(etudiant.get("nom", "Inconnu")) # "Inconnu" car la clé "nom" n'existe pas

# ajputer une nouvelle paire clé-valeur
etudiant["nom"] = "Dupont"
print(f"{etudiant['prenom']} {etudiant['nom']}")

# modification :
etudiant["age"] = 18
print(f"Après modification, l'âge de l'étudiant est : {etudiant['age']}")

# suppression :
del etudiant["age"]
print(f"Après suppression, l'étudiant est : {etudiant}")

etudiant["nom"] = ["Dupont", "Martin"]
etudiant["prenom"] = {"prenom1" : "Sélomey", "prenom2" : "Timothée"}

print(f"Etudiant après modification des noms et prénoms : {etudiant['prenom']['prenom1']} {etudiant['prenom']['prenom2']}")