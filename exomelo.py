total = 0
cap_franchi = False
for semaine in range(1, 11):
    depot = semaine * 2
    total = total + depot
    if semaine % 3 == 0:
        total = total + 5
        print(f"Semaine {semaine} : dépôt de {depot} €, total = {total} € (+5 € bonus mamie !)")
    else:
        print(f"Semaine {semaine} : dépôt de {depot} €, total = {total} €")
    if total > 50 and not cap_franchi:
        print("🎉 Cap des 50 € franchi !")
        cap_franchi = True
if total >= 100:
    print("Objectif atteint !")
else:
    print("Continue tes efforts !")
print("Total après 10 semaines :", total, "€")
total = 0
semaine = 0
while total < 200:
    semaine = semaine + 1
    depot = semaine * 2
    total = total + depot
    if semaine % 3 == 0:
        total = total + 5
print(f"Il faut {semaine} semaines pour acheter le vélo.")
print(f"Total économisé : {total} €")
solde = 0
while True:
    print(f"\n--- Tirelire de Mélodie (solde : {solde} €) ---")
    print("1. Déposer")
    print("2. Retirer")
    print("3. Quitter")
    choix = input("Votre choix : ")
    if choix == "1":
        montant = float(input("Montant à déposer : "))
        if montant > 0:
            solde = solde + montant
            print("Dépôt effectué !")
        else:
            print("Le montant doit être positif.")
    elif choix == "2":
        montant = float(input("Montant à retirer : "))
        if montant <= 0:
            print("Le montant doit être positif.")
        elif montant > solde:
            print("Solde insuffisant.")
        else:
            solde = solde - montant
            print("Retrait effectué !")
    elif choix == "3":
        print("Au revoir !")
        break
    else:
        print("Choix invalide.")

