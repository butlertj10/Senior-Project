from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont, QPixmap
from Geometry import Circle

class CircleWindow(QWidget):
    def __init__(self):
        super().__init__()

    # Create new 'Circle' Window
        self.setWindowTitle("Circle")
        self.setStyleSheet("background-color : white")
        self.setGeometry(1000, 250, 1200, 1300)

    # Add shape image
        self.labelImg = QLabel(self)
        self.circleImage = QPixmap('../images/circle/circle.png')   
        self.labelImg.setPixmap(self.circleImage)
        self.labelImg.move(450, 300)

    # Add Labels
       # Side Labels
        self.label_radius = QLabel("Radius: ", self)
        self.label_radius.setGeometry(50, 800, 325, 50)
        self.label_radius.setStyleSheet("border: 0px solid black;")
        self.label_radius_Units = QLabel("units", self)
        self.label_radius_Units.setGeometry(415, 800, 65, 50)
        self.label_radius_Units.setStyleSheet("border: 0px solid black;")

        self.label_diameter = QLabel("Diameter: ", self)
        self.label_diameter.setGeometry(50, 900, 325, 50)
        self.label_diameter.setStyleSheet("border: 0px solid black;")
        self.label_diameter_Units = QLabel("units", self)
        self.label_diameter_Units.setGeometry(415, 900, 65, 50)
        self.label_diameter_Units.setStyleSheet("border: 0px solid black;")

        self.label_area = QLabel("Area: ", self)
        self.label_area.setGeometry(700, 800, 325, 50)
        self.label_area.setStyleSheet("border: 0px solid black;")
        self.label_area_Units = QLabel("units²", self)
        self.label_area_Units.setGeometry(1085, 800, 75, 50)
        self.label_area_Units.setStyleSheet("border: 0px solid black;")

        self.label_circm = QLabel("Circumference: ", self)
        self.label_circm.setGeometry(650, 900, 325, 50)
        self.label_circm.setStyleSheet("border: 0px solid black;")
        self.label_circm_Units = QLabel("units", self)
        self.label_circm_Units.setGeometry(1085, 900, 65, 50)
        self.label_circm_Units.setStyleSheet("border: 0px solid black;")

    # Add Text Boxes 
        # Side Text Boxes
        self.radius = QLineEdit("",self)
        self.radius.setGeometry(200, 800, 200, 50) 
        
        self.diameter = QLineEdit(self)
        self.diameter.setGeometry(200, 900, 200, 50)

        self.area = QLineEdit(self)
        self.area.setGeometry(870, 800, 200, 50) 

        self.circumference = QLineEdit(self)
        self.circumference.setGeometry(870, 900, 200, 50)

        # Calculate Button
        self.calculateButton = QPushButton("Calculate", self)
        self.calculateButton.setFont(QFont('Arial', 11))
        self.calculateButton.setStyleSheet("background-color : darkCyan")
        self.calculateButton.setGeometry(375, 675, 180, 75)
        self.calculateButton.clicked.connect(self.calcCirc)

        # Clear Button
        self.clearButton = QPushButton("Clear", self)
        self.clearButton.setFont(QFont('Arial', 11))
        self.clearButton.setStyleSheet("background-color : red")
        self.clearButton.setGeometry(625, 675, 180, 75)
        self.clearButton.clicked.connect(self.clearCirc)

        self.show()
        vbox = QVBoxLayout()
        self.setLayout(vbox)

# Calculates all circle values and disaplys them
    def calcCirc(self):

        r = self.radius.text()
        d = self.diameter.text()
        a = self.area.text()
        c = self.circumference.text()

        r, d, a, c = Circle.calcCircle(r, d, a, c)
        self.radius.setText(r)
        self.diameter.setText(d)
        self.area.setText(a)
        self.circumference.setText(c)

# Clears all values of circle inputs
    def clearCirc(self):
        self.radius.setText("")
        self.diameter.setText("")
        self.area.setText("")
        self.circumference.setText("")