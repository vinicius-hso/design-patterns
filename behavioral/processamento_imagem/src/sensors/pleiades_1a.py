from .interfaces import Isensor

class Pleiades1A(Isensor):
            
    def process_image(self, file_path):
        print(f"Pleiades 1A processing image {file_path}")
