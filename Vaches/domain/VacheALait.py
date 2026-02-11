from Strategies.InvalidVacheException import InvalidVacheException
from Vaches.domain.Vache import Vache

class VacheALait (Vache):
    RENDEMENT_LAIT:float = 1.1
    PRODUCTION_LAIT_MAX:float=40.0
    lait_disponible:float
    lait_total_produit:float
    lait_total_traite:float

    def __init__(self, petit_nom, poids, age):
        super().__init__(petit_nom, poids, age)
        self.lait_total_produit = 0.0
        self.lait_total_traite = 0.0
        self.lait_disponible = 0.0

    def _calculer_lait(self, panse_avant):
        return panse_avant * self.RENDEMENT_LAIT

    def _stocker_lait(self, lait):
        super()._stocker_lait(lait)
        self.lait_total_produit += lait
        self.lait_disponible += lait

    def ruminer(self):
        if self.lait_disponible> self.PRODUCTION_LAIT_MAX :
            raise InvalidVacheException("Production exceder")
        elif (self.panse * self.RENDEMENT_LAIT) + self.lait_disponible > self.PRODUCTION_LAIT_MAX:
            raise InvalidVacheException("Le lait disponible excede la production max")
        super().ruminer()

    def traire (self, litres):
        if litres <= 0:
            raise InvalidVacheException("Quantité trait invalide")
        elif litres > self.lait_disponible:
            raise InvalidVacheException("La quantité de lait a traire est superieure au lait disponible")
        self.lait_disponible -= litres
        self.lait_total_traite += litres
        return self.lait_total_traite

    def __str__(self):
        return f"Lait total trait : {self.lait_total_traite} L in {super().__str__()} Lait disponible : {self.lait_disponible} L in {super().__str__()}"
    
  