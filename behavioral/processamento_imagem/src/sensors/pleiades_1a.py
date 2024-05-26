from .interfaces import Isensor

class Pleiades1A(Isensor):
            
    def fusion(self, file_path):
        print(f"Pleiades 1A - Fusion processing - Image {file_path}")
        
    def harmonization(self, file_path):
        print(f"Pleiades 1A - Harmonization processing - Image {file_path}")

    def ortho(self, file_path):
        print(f"Pleiades 1A - Ortho-retification processing - Image {file_path}")
        
    def co_registration(self, file_path):
        print(f"Pleiades 1A - Co-registration processing - Image {file_path}")