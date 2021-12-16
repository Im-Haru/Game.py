import sys




def question(question): 
    print(question)
    return sys.stdin.readline()[:-1]


attaquant = question("quel est le nom du joueur 1 ?")
adversaire = question("quel est le nom du joueur 2 ?")

joueurs = {
    attaquant:{ 
        "mana": 20,
        "pv": 300,
        "critiques"
    },
    adversaire:{
        "mana": 20,
        "pv": 300,
    }    
}

attaques =  {
    "1": {
        "degats": 20,
        "mana": 20,
        "nom": "Eclair"     
    },
    "2": {
        "degats": 10,
        "mana": 10,
        "nom": "Assaut"     
    },
    "0": {
        "degats": 0,
        "mana": 0,
        "nom": "Passez le tour"
    }
}



while True:
    
    StockerTour = attaquant

    print("Au tour de ", attaquant, "mana disponible", joueurs[attaquant]["mana"])
    print("Attaques disponibles:")
    for numero in attaques:
        print(numero, attaques[numero]["nom"], attaques[numero]["degats"], " degats", attaques[numero]["mana"], "mana")
    
    a = question("Quelle attaque utiliser ?") 

    if not a in attaques:
        print("L'attaque", a, " n'existe pas")
        continue

    damege = attaques[a]["degats"]
    mana = attaques[a]["mana"]

    if mana > joueurs[attaquant]["mana"]:
        print("Tu n'a pas assez de mana")
        continue

    joueurs[adversaire]["pv"] -= damege
    joueurs[attaquant]["mana"] -= mana

    print(adversaire," a perdu",damege,"pv Il lui reste", joueurs[adversaire]["pv"])

    if joueurs[adversaire]["pv"] <= 0:
        print("Le joueur",adversaire, "est K.O")
        break

    joueurs[attaquant]["mana"] += 15    

    attaquant = adversaire
    adversaire = StockerTour









