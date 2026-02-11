from Strategies.InvalidVacheException import InvalidVacheException
from Vaches.domain.Vache import Vache

class PieNoire (Vache):

    def __init__(self, petit_nom, poids, age):
        super().__init__(petit_nom, poids, age)