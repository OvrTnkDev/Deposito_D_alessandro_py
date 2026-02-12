from abc import ABC, abstractmethod

class Animale(ABC):
    @abstractmethod
    def muovi(self):
        pass
    
class Cane(Animale):
    def muovi(self):
        print("Il cane corre felice!")
        
class Pesce(Animale):
    def muovi(self):
        print("Il pesce nuota silenziosamente.")