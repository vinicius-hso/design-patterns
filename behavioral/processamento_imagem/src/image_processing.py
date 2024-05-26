# context
from __future__ import annotations
from .sensors import Isensor

class ImageProcessing():
    
    def __init__(self, sensor: Isensor) -> None:
        self._sensor = sensor
        
    @property
    def sensor(self) -> Isensor:
        return self._sensor
    
    @sensor.setter
    def sensor(self, sensor: Isensor) -> None:
        self._sensor = sensor
        
    def execute_fusion(self, file_path) -> None:
        self._sensor.fusion(file_path)
        
    def execute_harmonization(self, file_path) -> None:
        self._sensor.harmonization(file_path)
        
    def execute_ortho(self, file_path) -> None:
        self._sensor.ortho(file_path)
        
    def execute_co_registration(self, file_path) -> None:
        self._sensor.co_registration(file_path)