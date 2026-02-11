from Strategies.InvalidVacheException import InvalidVacheException
from Vaches.domain.VacheALait import VacheALait
from nourriture.TypeNourriture import TypeNourriture

class PieNoire (VacheALait):
    nb_taches_noires : int
    nb_taches_blanches : int

    COEFFICIENT_NUTRITIONNEL: dict[TypeNourriture, float] = {
        TypeNourriture.MARGUERITE: 1.1,
        TypeNourriture.HERBE: 1.0,
        TypeNourriture.FOIN: 0.9,
        TypeNourriture.PAILLE: 0.4,
        TypeNourriture.CEREALES: 1.3,
    }

    _ration : dict[TypeNourriture, float]

    def __init__(self, petit_nom, poids, age, nb_taches_noires, nb_taches_blanches):
        super().__init__(petit_nom, poids, age)
        self.nb_taches_blanches = nb_taches_blanches
        self.nb_taches_noires = nb_taches_noires
        self._ration = {}
        if type(self.nb_taches_noires) != int or type(self.nb_taches_blanches) != int:
            raise InvalidVacheException ("Le nombre de taches noires ou blanches doit etre un entier") 
        elif self.nb_taches_blanches <= 0:
            raise InvalidVacheException("Nombre de taches blanches nul ou negatif")
        elif self.nb_taches_noires <= 0:
            raise InvalidVacheException("Nombre de taches noires nul ou negatif") 
        
    @property
    def ration(self) -> dict[TypeNourriture, float]:
        return self._ration.copy()

    def brouter(self, quantite, nourriture=None):
        super().brouter(quantite, None)

        if nourriture is not None:
            if nourriture in self._ration:
                self._ration[nourriture] += quantite
            else:
                self._ration[nourriture] = quantite

    def _post_rumination(self, panse_avant, lait):
        super()._post_rumination(panse_avant, lait)
        self._ration.clear()

    def _calculer_lait(self, panse_avant):
        if not self._ration:
            return super()._calculer_lait(panse_avant)
        total_nutritionnel = 0.0
        for aliment, quantite in self._ration.items():
            coeff = self.COEFFICIENT_NUTRITIONNEL.get(aliment, 1.0)
            total_nutritionnel += quantite * coeff
        return total_nutritionnel * self.RENDEMENT_LAIT

    def __str__(self):
        message_de_base = super().__str__()
        return f"{message_de_base} (C'est une Pie Noire avec {self.nb_taches_noires} taches noires et {self.nb_taches_blanches} taches blanches)"