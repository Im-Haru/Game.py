import sys

from Attaques import Attaque
from Personnages import Mage, Guerrier, Pretre

def question(question): 
    print(question)
    return sys.stdin.readline()[:-1]


class Joueurs():
    def __init__(self):
        self.nom = question("Joueur, quel est ton nom ?")


        
        availableClass = [Mage, Guerrier, Pretre]
        i = 0
        print("Classe disponible :")
        for a in availableClass:
            print(i, ":", a.__name__)
            i += 1
        a = question("Quelle classe choississez vous ?")
        if int(a) >= 0 and int(a) < len(availableClass):
            self.personnages = availableClass[int(a)]()












