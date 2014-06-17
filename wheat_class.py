from crop_class import *

class Wheat(Crop):
    """A wheat crop"""

    def __init__(self):
        super().__init__(growth_rate,light_need,water_need)
        self._type = "Wheat"

    def grow(self,light,water):
        if light >= light_need and water >= water_need:
            if self._status == "Seedling":
                growth += growth_rate * 1.5
        
