import RuminationStrategy

class NoMilkStrategy(RuminationStrategy):
    def _calculer_lait(self):
        return 0.0
    
    def _stocker_lait(self):
        return None
        
    def _post_rumination(self):
        return None