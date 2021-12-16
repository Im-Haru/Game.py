class Personnage:

    def __init__(self, nom = "", pv = 100, mana = 20, critiques = 1):
        self.nom = nom
        self.pv = pv
        self.mana = mana
        self.critiques = critiques

    def Presentation(self):
        return self.nom

    def PrendreAttaque(self, attaque):
        self.pv -= attaque.degats
        print(self.nom, "perds", attaque.degats, "PVs")

    def Attaquer(self, attaque, ennemi):
        print(self.nom, "utilise l'attaque", attaque.nom)
        self.mana -= attaque.mana
        ennemi.PrendreAttaque(attaque)

class Mage(Personnage):
    def __init__(self):
        self.nom = "Vixou le semmeur de grabuges"
        self.pv = 80
        self.mana = 150
        self.critiques = 5

class Guerrier(Personnage):
    def __init__(self):
        self.nom = "Kit le guerrier blageur"
        self.pv = 300
        self.mana = 10
        self.critiques = 0.5



class Pretre(Personnage):
    def __init__(self):
        self.nom = "Adadaa le pretre pété"
        self.pv = 75
        self.mana = 200
        self.critiques = 2

def Presentation(self):
        return "ci la pharmacie %s" % (self.nom)







