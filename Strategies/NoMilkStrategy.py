from Strategies.protocols.RuminationStrategy import RuminationStrategy

class NoMilkStrategy(RuminationStrategy):

    def _calculer_lait(self, vache_o, panse_avant):
        lait = vache_o.RENDEMENT_RUMINATION * panse_avant
        return lait
    
    def _stocker_lait(self, vache_o, lait):
        vache_o.poids += lait
        
    def _post_rumination(self, vache_o, panse_avant, lait):
        vache_o.panse = 0.0
