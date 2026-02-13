from abc import abstractmethod

class RuminationStrategy:

    @abstractmethod
    def _calculer_lait(self, vache_o, panse_avant):
        pass
    
    @abstractmethod
    def _stocker_lait(self, vache_o, lait):
        pass
        
    @abstractmethod    
    def _post_rumination(self, vache_o, panse_avant, lait):
        pass