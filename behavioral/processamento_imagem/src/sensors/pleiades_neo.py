from .interfaces import Isensor

class PleiadesNeo(Isensor):
            
    def fusion(self, file_path):
        print(f"Pleiades Neo - Fusion processing - Image {file_path}")
        
    def harmonization(self, file_path):
        print(f"Pleiades Neo - Harmonization processing - Image {file_path}")

    def ortho(self, file_path):
        print(f"Pleiades Neo - Ortho-retification processing - Image {file_path}")
        
    def co_registration(self, file_path):
        print(f"Pleiades Neo - Co-registration processing - Image {file_path}")
