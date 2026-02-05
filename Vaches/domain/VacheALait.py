from Strategies.InvalidVacheException import InvalidVacheException
from Vaches.domain.Vache import Vache

class VacheALait (Vache):
    RENDEMENT_LAIT:float = 1.1
    PRODUCTION_LAIT_MAX:float=40.0
    lait_disponible:float
    lait_total_produit:float
    laitTotalTraite:float

    def __init__(self, petit_nom, poids, age):
        super().__init__(petit_nom, poids, age)
        self.panse = 0.0

    def _calculer_lait(self, panse_avant):
        self.lait_disponible =  (panse_avant * self.RENDEMENT_LAIT)
        return self.lait_disponible

    def _stocker_lait(self, lait):
        return super()._stocker_lait(lait)

    def ruminer(self):
        return super().ruminer()

    def traire (self, lait):
        self.lait_total_produit += lait
        return self.lait_total_produit

    def __str__(self):
        return 