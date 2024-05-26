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
        
    def execute(self, file_path) -> None:
        self._sensor.process_image(file_path)