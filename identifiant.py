def creer_identifiant(prenom, nom) :
    prenom = prenom.replace(" ", "")
    nom = nom.replace(" ", "").replace("-", "")
    identifiant = prenom[0] + nom
    return identifiant.lower()[:8]

def masquer_telephone(numero):
    numero = numero.replace(" ", "").replace(".", "")
    nb_star = max(0, len(numero) - 4)
    return numero[:2] + "*" * nb_star + numero[-2:]

def est_code_postal_valide(code) : # Crée fonction est_code_postal_valide qui reçoit  information code
    code = code.strip() # ça enlève les espaces au début et à la fin du code.
    return code.isdigit() and len(code) == 5 # vérifie si le code contient exactement 5 caractères et renvoie True si oui, sinon False.

def compter_mots(phrase) :
    phrase = phrase.strip()
    return phrase.count(" ") + 1

def main() :
    print(creer_identifiant("Melvin", "Mafuta"))
    print(masquer_telephone("0102030405"))
    print(est_code_postal_valide("75020"))
    print(compter_mots("ahahahaha Hello yall niggas my name is Melvin im a futur billionnairy how i know that ? cuz im to beautiful nigga and im the futur best in the world i feel it cuz i know o can't quit that im going to improve myself proprely don't worry guys im good i got it i keep going for my people for my country for my beautiful love my futur fiance my futur wife my futur baby mama big mama big mama big mama not you Latto but i talk about my wife Serena and fok you my nigga who tf are you bruv get the fok out g so and im tired ah fok i hope i can improve myself pls God help me i need to work at home i don't have choice i need to do some white night and do some exercice i need it drako"))

main()


    

