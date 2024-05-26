from .interfaces import Isensor

class Spot(Isensor):
            
    def fusion(self, file_path):
        print(f"Spot - Fusion processing - Image {file_path}")
        
    def harmonization(self, file_path):
        print(f"Spot - Harmonization processing - Image {file_path}")

    def ortho(self, file_path):
        print(f"Spot - Ortho-retification processing - Image {file_path}")
        
    def co_registration(self, file_path):
        print(f"Spot - Co-registration processing - Image {file_path}")
