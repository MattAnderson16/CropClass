from sheep_class import *
from cow_class import *

def display_menu():
    print()
    print("Which animal would you like to create?")
    print()
    print("1. Sheep")
    print("2. Cow")
    print()

def select_option():
    valid_option = False
    while not valid_option:
        try:
            choice = int(input("Please choose an option from the above menu >>> "))
            if choice in (1,2):
                valid_option = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
            print()
    return choice

def create_animal():
    display_menu()
    choice = select_option()
    if choice == 1:
        new_animal = Sheep()
    elif choice == 2:
        new_animal = Cow()
    return new_animal

if __name__ == "__main__":
    new_animal = create_animal()
    manage_animal(new_animal)
