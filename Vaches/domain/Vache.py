from Strategies.InvalidVacheException import InvalidVacheException
import itertools

class Vache:
    id_iter = itertools.count()
    AGE_MAX = 25
    POIDS_MAX = 1000.0
    PANSE_MAX = 50.0
    POIDS_MIN_PANSE = 2.0
    petit_nom:str
    poids:float
    panse:float = 0.0
    age:int
    RENDEMENT_RUMINATION:float=0.25

    def __init__(self, petit_nom, poids, age):
        self.petit_nom = petit_nom
        self.age = age
        self.poids = poids
        self.id = next(self.id_iter)
        self.valider_etat()

    def __str__(self):
        return print(f"{self.id} La vache {self.petitn_om} a {self.age} et pèse {self.poids}" )
    
    def valider_etat (self):
        if self.petit_nom.isspace() or self.petit_nom == "" or self.age <= 0 or self.poids <= 0 or self.poids > self.POIDS_MAX or self.age > self.AGE_MAX:
            raise InvalidVacheException(f"La vache {self.id} n'est pas valide")

    def ajouter_panse(self, quantite):
        if quantite > 0:
            self.panse+=quantite

    def brouter(self, quantite, nourriture=None):
        self.ajouter_panse(quantite)
        if nourriture != None or quantite <= 0:
            raise InvalidVacheException("Le type de nourriture n'est pas bon ")
        print(f"{self.panse}")

        if self.panse > self.PANSE_MAX:
            raise InvalidVacheException("La quantite excéde la capacité maximale de la panse")

    def vieillir (self):
        if self.age < 25:
            self.age +=1
        else:
            raise InvalidVacheException("La vache a atteint l'age limte")
    
    def valider_rumination_possible(self):
        if self.panse <=0:
            raise InvalidVacheException("La rumination ne peut être effectue car la panse est vide")

    def _calculer_lait(self, panse_avant):
        lait = self.RENDEMENT_RUMINATION * panse_avant
        return lait
    
    def _stocker_lait(self, lait):
        self.poids += lait
        
    
    def _post_rumination(self):
        self.panse = 0.0

    def ruminer(self):
        self.valider_rumination_possible()
        self._stocker_lait(self._calculer_lait(self.panse))
        self._post_rumination()
