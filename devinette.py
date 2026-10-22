print("====== DEVINETTE ======")
import random
nombre_secret = random.randint(1, 20)
gagne = False
print("Devinez le nombre entre 1 et 20 !")
for tentative in range(1, 6):
    print("Tentative", tentative,"/ 5")
    nombre = int(input("Entrez un nombre : "))
    if nombre == nombre_secret:
        print("Bravo ! Tu as trouvé", nombre_secret, "en", tentative, "tentatives !")
        gagne = True
        break
    elif nombre < nombre_secret:
        print("C'est plus grand !")
    else:
        print("C'est plus petit !")
if not gagne:
    print("Dommage ! Tu as perdu.")
print("Le nombre secret était :", nombre_secret)

    
    
    
    