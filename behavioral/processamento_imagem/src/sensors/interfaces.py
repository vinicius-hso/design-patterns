from abc import ABC, abstractclassmethod

class Isensor(ABC):
    
    @abstractclassmethod
    def fusion(self):
        pass
    
    @abstractclassmethod
    def harmonization(self):
        pass
    
    @abstractclassmethod
    def ortho(self):
        pass
    
    @abstractclassmethod
    def co_registration(self):
        pass