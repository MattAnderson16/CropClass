import sys
import random

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from radio_button_widget_class import *
from manual_grow_dialog_class import *

from sheep_class import *
from cow_class import *

class AnimalWindow(QMainWindow):
    """this class creates a main window to observe the growth of a simulated animal"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Animal Simulator")
        self.create_select_animal_layout()

        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.select_animal_widget)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)

    def create_select_animal_layout(self):
        self.animal_radio_buttons = RadioButtonWidget("Animal Simulation", "Please select an animal", ("Sheep", "Cow"))
        self.instantiate_button = QPushButton("Create Animal")

        self.initial_layout = QVBoxLayout()
        self.initial_layout.addWidget(self.animal_radio_buttons)
        self.initial_layout.addWidget(self.instantiate_button)

        self.select_animal_widget = QWidget()
        self.select_animal_widget.setLayout(self.initial_layout)

        self.instantiate_button.clicked.connect(self.instantiate_animal)

    def create_view_animal_layout(self):
        self.weight_label = QLabel("Weight")
        self.days_label = QLabel("Days Growing")
        self.status_label = QLabel("Animal Status")

        self.weight_line_edit = QLineEdit()
        self.days_line_edit = QLineEdit()
        self.status_line_edit = QLineEdit()

        self.manual_grow_button = QPushButton("Manually Grow")
        self.automatic_grow_button = QPushButton("Automatically Grow")

        self.grow_grid = QGridLayout()
        self.status_grid = QGridLayout()

        self.status_grid.addWidget(self.weight_label,0,0)
        self.status_grid.addWidget(self.days_label,1,0)
        self.status_grid.addWidget(self.status_label,2,0)

        self.status_grid.addWidget(self.weight_line_edit,0,1)
        self.status_grid.addWidget(self.days_line_edit,1,1)
        self.status_grid.addWidget(self.status_line_edit,2,1)

        self.grow_grid.addLayout(self.status_grid,0,1)
        self.grow_grid.addWidget(self.manual_grow_button,1,0)
        self.grow_grid.addWidget(self.automatic_grow_button,1,1)

        self.view_animal_widget = QWidget()
        self.view_animal_widget.setLayout(self.grow_grid)

        self.automatic_grow_button.clicked.connect(self.automatically_grow_animal)
        self.manual_grow_button.clicked.connect(self.manually_grow_animal)

    def instantiate_animal(self):
        animal_type = self.animal_radio_buttons.selected_button()
        if animal_type == 1:
            self.simulated_animal = Sheep("Shaun")
        elif animal_type == 2:
            self.simulated_animal = Cow("Bessie")
        self.create_view_animal_layout()
        self.stacked_layout.addWidget(self.view_animal_widget)
        self.stacked_layout.setCurrentIndex(1)

    def automatically_grow_animal(self):
        for days in range(30):
            food = random.randint(1,10)
            water = random.randint(1,10)
            self.simulated_animal.grow(food,water)
        self.update_animal_view_status()

    def manually_grow_animal(self):
        manual_values_dialog = ManualGrowDialog()
        manual_values_dialog.light_spinbox.setSuffix(" Food")
        manual_values_dialog.exec_()
        food,water = manual_values_dialog.values()
        self.simulated_animal.grow(food,water)
        self.update_animal_view_status()

    def update_animal_view_status(self):
        animal_status_report = self.simulated_animal.report()

        self.weight_line_edit.setText(str(animal_status_report["weight"]))
        self.days_line_edit.setText(str(animal_status_report["days growing"]))
        self.status_line_edit.setText(str(animal_status_report["status"]))

if __name__ == "__main__":
    animal_simulation = QApplication(sys.argv)
    animal_window = AnimalWindow()
    animal_window.show()
    animal_window.raise_()
    animal_simulation.exec_()
