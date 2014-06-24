from animal_class import *

class Sheep(Animal):
    """A sheep"""

    def __init__(self,name):
        super().__init__(1,4,3)
        self._type = "Sheep"
        self._name = name

    def grow(self,food,water):
        if food >= self._food_need and water >= self._food_need:
            if self._status == "Baby" and water >= self._water_need and food >= self._food_need:
                self._weight += self._growth_rate * 1.5
            elif self._status == "Child" and water >= self._water_need and food >= self._food_need:
                self._weight += self._growth_rate * 1.25
            elif self._status == "Adult" and water >= self._water_need and food >= self._food_need:
                self._weight += self._growth_rate
            elif self._status == "Old" and water >= self._water_need and food >= self._food_need:
                self.weight += self._growth_rate * 0.75
        self._days_growing += 1
        self._update_status()

if __name__ == "__main__":
    Sheep = Sheep("Shaun")
    print(Sheep._report())
    manual_grow(Sheep)
    print(Sheep._report())
