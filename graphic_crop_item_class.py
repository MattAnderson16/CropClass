from graphic_field_item_class import *

class CropGraphicsPixmap(FieldItemGraphicsPixmapItem):
    """this class provides a pixmap item with a preset image for the crop"""

    #constructor
    def __init__(self,graphics_list):
        super().__init__(graphics_list)
        
        self.crop = None

    def update_status(self):
        if self.crop_status == "Seed":
            self.setPixmap(QPixmap(self.available_graphics[0]).scaledToWidth(25,1))
        elif self.crop._status = ="Seedling":
            self.setPixmap(QPixmap(self.available_graphics[1]).scaledToWidth(25,1))
        elif self.crop_status == "Young":
            self.setPixmap(QPixmap(self.available_graphics[3]).scaledToWidth(25,1))
        elif self.crop._status = ="Mature":
            self.setPixmap(QPixmap(self.available_graphics[4]).scaledToWidth(25,1))
        elif self.crop._status = ="Old":
            self.setPixmap(QPixmap(self.available_graphics[5]).scaledToWidth(25,1))        
