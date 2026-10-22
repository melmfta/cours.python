class Personne :
    def __init__(self, nom, age,): 
        self.nom = nom
        self.age = age
    def sePresenter(self):
        return f"Je m'appelle {self.nom} et j'ai {self.age} ans"

    def vaVieillir(self) :
        self.age += 1
    
# instanciation    
alicia = Personne("Alicia", 19)
print(f"{alicia.sePresenter()}")

markErwann = Personne("Mark-Erwann", 19)
markErwann.vaVieillir()
print(f"{markErwann.sePresenter()}")

thomas = Personne("Thomas", 19)
print(f"{thomas.sePresenter()}")

coCoJojo = Personne("Coco-Jojo", 23)
print(f"{coCoJojo.sePresenter()}")


# les personnes ont la possibilité de vieillir c'est à-dire d'avoir un an de plus

  
chaine = "toto"
chaine.strip(); # corrige la faute de frappe "stip" en "strip"




# ------------------------
class CompteBancaire :
    def __init__(self, titulaire, solde) :
       # propriétés (attributs) du compte dancaire
       self.titulaire = titulaire
       self.solde = solde
    
    def deposer(self,montant) :
        if montant > 0 :
            self.solde += montant
        else :
            # on lève une exception si le montant est négatif
            raise ValueError("Le montant doit être positif por favor")
            
    def retirer(self,montant) :
        if montant > 0 :
            if self.solde >= montant :
                self.solde -= montant 
            else : 
                print("Solde insuffisant")
        else :
            # on lève une exception si le montant est négatif
            raise ValueError("Le montant doit être positif")
            
    def consulter(self) :
        return f"Titulaire: {self.titulaire}, Solde: {self.solde}€"                           




compteMelvin = CompteBancaire("Melvin",19000)
compteMelvin.deposer(5000)
compteMelvin.deposer(500000)
print(compteMelvin.consulter())