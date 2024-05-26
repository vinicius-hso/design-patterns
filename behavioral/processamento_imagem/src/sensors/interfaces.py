from abc import ABC, abstractclassmethod

class Isensor(ABC):
    
    @abstractclassmethod
    def process_image(self, file_path):
        pass