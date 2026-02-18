from Strategies.protocols.RuminationStrategy import RuminationStrategy

class StandardMilkStrategy(RuminationStrategy):
    def _calculer_lait(self, vache_o, panse_avant):
       return panse_avant * vache_o.RENDEMENT_LAIT
    
    def _stocker_lait(self, vache_o, lait):
       vache_o.poids += lait 
       vache_o.lait_disponible += lait
       vache_o.lait_total_produit += lait
        
    def _post_rumination(self, vache_o, panse_avant, lait):
        vache_o.panse = 0.0