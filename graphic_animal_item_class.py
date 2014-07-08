from graphic_field_item_class import *

class AnimalGraphicsPixmap(FieldItemGraphicsPixmapItem):
    """this class provides a pixmap item with a preset image for the animal"""

    #constructor
    def __init__(self,graphics_list):
        super().__init__(graphics_list)
        
        self.amimal = None

    def update_status(self):
        if self.animal_status == "Baby":
            self.setPixmap(QPixmap(self.available_graphics[0]).scaledToWidth(25,1))
        elif self.animal._status = ="Young":
            self.setPixmap(QPixmap(self.available_graphics[1]).scaledToWidth(25,1))
        elif self.animal_status == "Mature":
            self.setPixmap(QPixmap(self.available_graphics[3]).scaledToWidth(25,1))
        elif self.animal._status = ="Old":
            self.setPixmap(QPixmap(self.available_graphics[4]).scaledToWidth(25,1))   
