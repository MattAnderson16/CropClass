class Crop:
    """Generic Crop"""
    
    def __init__(self,growth_rate,light_need,water_need):
        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"
        #These attributes are private and are only accessed from within the class

    def needs(self):
        return {"light need":self._light_need,"water_need":self._water_need}

    def report(self):
        return {"type":self._type,"status":self._status,"growth":self._growth,"days growing":self._days_growing}


def main():
    new_crop = Crop(1,4,3)
    print(new_crop.needs())
    print(new_crop.report())
    new_crop2 = Crop(2,5,7)
    print(new_crop2.needs())
    print(new_crop2.report())


    
if __name__ == "__main__":
    main()
    
