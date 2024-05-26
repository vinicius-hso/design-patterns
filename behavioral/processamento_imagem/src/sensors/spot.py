from .interfaces import Isensor

class Spot(Isensor):
            
    def process_image(self, file_path):
        print(f"Spot processing image {file_path}")
