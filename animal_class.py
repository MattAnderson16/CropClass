import random

class Animal:
    """Animal base class"""
    def __init__(self,growth_rate,food_need,water_need):
        self._weight = 15
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._food_need = food_need
        self._water_need = water_need
        self._status = "Baby"
        self._type = "Generic"
        self._name = "Generic Animal"

    def needs(self):
        return{"food need":self._food_need, "water need":self._water_need}

    def report(self):
        return {"type":self._type,"status":self._status,"weight":self._weight,"days growing":self._days_growing}

    def _update_status(self):
        if self._weight > 75:
            self._status = "Old"
        elif self._weight > 50:
            self._status = "Adult"
        elif self._weight > 25:
            self._status = "Child"
        elif self._weight == 15:
            self._status = "Baby"

    def grow(self,food,water):
        if water >= self._water_need and food >= self._food_need:
            self._weight += self._growth_rate
        self._days_growing += 1
        self._update_status()

def auto_grow(animal, days):
    for day in range(days):
        food = random.randint(1,10)
        water = random.randint(1,10)
        animal.grow(food,water)

def manual_grow(animal):
    valid = False
    while not valid:
        try:
            food = int(input("Please enter a food value (1-10) >>> "))
            if 1 <= food <= 10:
                valid = True
            else:
                print("Value entered is invalid - Please enter a value between 1 and 10")
        except ValueError:
            print("Value entered is invalid - Please enter a value between 1 and 10")
    valid = False
    while not valid:
        try:
            water = int(input("Please enter a water value (1-10) >>> "))
            if 1 <= water <= 10:
                valid = True
            else:
                print("Value entered is invalid - Please enter a value between 1 and 10")
        except ValueError:
            print("Value entered is invalid - Please enter a value between 1 and 10")

def display_menu():
    print("1. Grow manually over 1 day")
    print("2. Grow automatically over 30 days")
    print("3. Report status")
    print("0. Exit program")
    print()

def get_menu_choice():
    option_valid = False
    while not option_valid:
        try:
            choice = int(input("Please select an option from the above menu >>> "))
            if 0 <= choice <= 4:
                option_valid = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
    return choice

def manage_animal(animal):
    print("This is the animal management program")
    print()
    noexit = True
    while noexit:
        display_menu()
        option = get_menu_choice()
        if option == 1:
            manual_grow(animal)
            print()
        elif option == 2:
            auto_grow(animal,30)
            print()
        elif option == 3:
            print(animal.report())
            print()
        elif option == 0:
            noexit = False
            print()
    print("Thank you for using the animal management program")

if __name__ == "__main__":
   new_animal = Animal(3,4,4)
   manage_animal(new_animal)
        
            
