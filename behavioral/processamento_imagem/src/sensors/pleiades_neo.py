from .interfaces import Isensor

class PleiadesNeo(Isensor):
            
    def process_image(self, file_path):
        print(f"Pleiades Neo processing image {file_path}")
