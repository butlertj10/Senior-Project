from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTabWidget
from PyQt5.QtGui import QFont, QPixmap
from PyQt5 import QtCore
from Geometry import Quadrilateral

class QuadWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.quadTabs = QTabWidget()
        vbox = QVBoxLayout()

        squareTab = SquareTab()
        rectTab = RectangleTab()
        trapTab = TrapTab()
        pgramTab = ParallelogramTab()
        rhomTab = RhombusTab()

        self.quadTabs.addTab(squareTab, "Square")
        self.quadTabs.addTab(rectTab, "Rectangle")
        self.quadTabs.addTab(trapTab, "Trapezoid")
        self.quadTabs.addTab(pgramTab, "Parallelogram")
        self.quadTabs.addTab(rhomTab, "Rhombus")

        # Create new 'Triangle' Window
        self.setWindowTitle("Quadrilaterals")
        self.setGeometry(1000, 250, 1200, 1300)

        vbox.addWidget(self.quadTabs)
        self.setLayout(vbox)

class SquareTab(QWidget):
    def __init__(self):
        super().__init__()
        
        self.labelImg = QLabel(self)
        self.squareImage = QPixmap('../images/quad/square.png')   
        self.labelImg.setPixmap(self.squareImage)
        self.labelImg.move(150, 300)

    # All values label
        self.squareValuesList = QLabel(self)
        self.squareValuesList.setWordWrap(True)
        self.squareValuesList.setGeometry(605, 175, 410, 410)
        self.squareValuesList.setStyleSheet("border: 2px solid black;")
        self.squareValuesList.setFont(QFont('Arial', 16))
        self.squareValuesList.setAlignment(QtCore.Qt.AlignCenter)

    # Add Labels for sides
        self.label_SA = QLabel("Side a: ", self)
        self.label_SA.setGeometry(50, 900, 325, 50)
        self.label_SA.setStyleSheet("border: 0px solid black;")
        self.label_SA_Units = QLabel("units", self)
        self.label_SA_Units.setGeometry(415, 900, 65, 50)
        self.label_SA_Units.setStyleSheet("border: 0px solid black;")

    # Add Text Boxes for sides/angles
        self.sideA = QLineEdit("",self)
        self.sideA.setGeometry(200, 900, 200, 50)

    # Calculate Button
        self.calculateButton = QPushButton("Calculate", self)
        self.calculateButton.setFont(QFont('Arial', 11))
        self.calculateButton.setStyleSheet("background-color : darkCyan")
        self.calculateButton.setGeometry(605, 875, 180, 75)
        self.calculateButton.clicked.connect(self.calcSqaure)

    # Clear Button
        self.clearButton = QPushButton("Clear", self)
        self.clearButton.setFont(QFont('Arial', 11))
        self.clearButton.setStyleSheet("background-color : red")
        self.clearButton.setGeometry(835, 875, 180, 75)
        self.clearButton.clicked.connect(self.clearSquare)
        
        self.show()
        vbox = QVBoxLayout()
        self.setLayout(vbox)

    # Calculates the triangle and displays values
    def calcSqaure(self):
        SA = self.sideA.text()
        squareValues = Quadrilateral.squareCalc(SA)
        self.squareValuesList.setText(squareValues)

    # Clears all values of text boxes
    def clearSquare(self):
        self.sideA.setText("")
        self.squareValuesList.setText("")

class RectangleTab(QWidget):    
    def __init__(self):
        super().__init__()

        self.labelImg = QLabel(self)
        self.rectangleImage = QPixmap('../images/quad/rectangle.png')   
        self.labelImg.setPixmap(self.rectangleImage)
        self.labelImg.move(150, 300)

  # All values label
        self.rectValuesList = QLabel(self)
        self.rectValuesList.setWordWrap(True)
        self.rectValuesList.setGeometry(605, 175, 410, 410)
        self.rectValuesList.setStyleSheet("border: 2px solid black;")
        self.rectValuesList.setFont(QFont('Arial', 16))
        self.rectValuesList.setAlignment(QtCore.Qt.AlignCenter)

    # Add Labels for sides
        self.label_Length = QLabel("Length: ", self)
        self.label_Length.setGeometry(50, 900, 325, 50)
        self.label_Length.setStyleSheet("border: 0px solid black;")
        self.label_Length_Units = QLabel("units", self)
        self.label_Length_Units.setGeometry(415, 900, 65, 50)
        
        self.label_Width = QLabel("Width: ", self)
        self.label_Width.setGeometry(50, 1000, 325, 50)
        self.label_Width.setStyleSheet("border: 0px solid black;")
        self.label_Width_Units = QLabel("units", self)
        self.label_Width_Units.setGeometry(415, 1000, 65, 50)
        self.label_Width_Units.setStyleSheet("border: 0px solid black;")

    # Add Text Boxes for sides/angles
        self.lengthRA = QLineEdit("",self)
        self.lengthRA.setGeometry(200, 900, 200, 50)

        self.widthRA = QLineEdit("",self)
        self.widthRA.setGeometry(200, 1000, 200, 50)

    # Calculate Button
        self.calculateButton = QPushButton("Calculate", self)
        self.calculateButton.setFont(QFont('Arial', 11))
        self.calculateButton.setStyleSheet("background-color : darkCyan")
        self.calculateButton.setGeometry(605, 875, 180, 75)
        self.calculateButton.clicked.connect(self.calcRectangle)

    # Clear Button
        self.clearButton = QPushButton("Clear", self)
        self.clearButton.setFont(QFont('Arial', 11))
        self.clearButton.setStyleSheet("background-color : red")
        self.clearButton.setGeometry(835, 875, 180, 75)
        self.clearButton.clicked.connect(self.clearRectangle)
        
        self.show()
        vbox = QVBoxLayout()
        self.setLayout(vbox)

    # Calculates the triangle and displays values
    def calcRectangle(self):
        length = self.lengthRA.text()
        width = self.widthRA.text()
        rectValues = Quadrilateral.rectCalc(length, width)
        self.rectValuesList.setText(rectValues)

    # Clears all values of text boxes
    def clearRectangle(self):
        self.lengthRA.setText("")
        self.widthRA.setText("")
        self.rectValuesList.setText("")

class TrapTab(QWidget):     
    def __init__(self):
        super().__init__()

        self.labelImg = QLabel(self)
        self.trapImage = QPixmap('../images/quad/trapezoid.png')   
        self.labelImg.setPixmap(self.trapImage)
        self.labelImg.move(150, 300)
       
    # All values label
        self.trapValuesList = QLabel(self)
        self.trapValuesList.setWordWrap(True)
        self.trapValuesList.setGeometry(605, 175, 410, 410)
        self.trapValuesList.setStyleSheet("border: 2px solid black;")
        self.trapValuesList.setFont(QFont('Arial', 16))
        self.trapValuesList.setAlignment(QtCore.Qt.AlignCenter)

    # Add Labels for sides/angles
        self.label_SideA_TZ = QLabel("Side a: ", self)
        self.label_SideA_TZ.setGeometry(50, 700, 325, 50)
        self.label_SideA_TZ.setStyleSheet("border: 0px solid black;")
        self.label_SideA_TZ_Units = QLabel("units", self)
        self.label_SideA_TZ_Units.setGeometry(415, 700, 100, 50)
        self.label_SideA_TZ_Units.setStyleSheet("border: 0px solid black;")

        self.label_SideB = QLabel("Side b: ", self)
        self.label_SideB.setGeometry(50, 800, 325, 50)
        self.label_SideB.setStyleSheet("border: 0px solid black;")
        self.label_SideB_Units = QLabel("units", self)
        self.label_SideB_Units.setGeometry(415, 800, 100, 50)
        self.label_SideB_Units.setStyleSheet("border: 0px solid black;")

        self.label_SideC = QLabel("Side c: ", self)
        self.label_SideC.setGeometry(50, 900, 325, 50)
        self.label_SideC.setStyleSheet("border: 0px solid black;")
        self.label_SideC_Units = QLabel("units", self)
        self.label_SideC_Units.setGeometry(415, 900, 100, 50)
        self.label_SideC_Units.setStyleSheet("border: 0px solid black;")

        self.label_SideD = QLabel("Side d: ", self)
        self.label_SideD.setGeometry(50, 1000, 325, 50)
        self.label_SideD.setStyleSheet("border: 0px solid black;")
        self.label_SideD_Units = QLabel("units", self)
        self.label_SideD_Units.setGeometry(415, 1000, 100, 50)
        self.label_SideD_Units.setStyleSheet("border: 0px solid black;")

        self.label_Height = QLabel("Height: ", self)
        self.label_Height.setGeometry(50, 1100, 325, 50)
        self.label_Height.setStyleSheet("border: 0px solid black;")
        self.label_Height_Units = QLabel("units", self)
        self.label_Height_Units.setGeometry(415, 1100, 65, 50)
        self.label_Height_Units.setStyleSheet("border: 0px solid black;")

    # Add Text Boxes for sides/angles
        self.sideA = QLineEdit("",self)
        self.sideA.setGeometry(200, 700, 200, 50) 
        
        self.sideB = QLineEdit(self)
        self.sideB.setGeometry(200, 800, 200, 50)

        self.sideC = QLineEdit("",self)
        self.sideC.setGeometry(200, 900, 200, 50) 
        
        self.sideD = QLineEdit(self)
        self.sideD.setGeometry(200, 1000, 200, 50)

        self.heightTZ = QLineEdit(self)
        self.heightTZ.setGeometry(200, 1100, 200, 50)

    # Calculate Button
        self.calculateButton = QPushButton("Calculate", self)
        self.calculateButton.setFont(QFont('Arial', 11))
        self.calculateButton.setStyleSheet("background-color : darkCyan")
        self.calculateButton.setGeometry(605, 875, 180, 75)
        self.calculateButton.clicked.connect(self.calcTrap)

    # Clear Button
        self.clearButton = QPushButton("Clear", self)
        self.clearButton.setFont(QFont('Arial', 11))
        self.clearButton.setStyleSheet("background-color : red")
        self.clearButton.setGeometry(835, 875, 180, 75)
        self.clearButton.clicked.connect(self.clearTrap)
        
        self.show()
        vbox = QVBoxLayout()
        self.setLayout(vbox)

    # function that calcualtes the triangle and displays values
    def calcTrap(self):
        SA = self.sideA.text()
        SB = self.sideB.text()
        SC = self.sideC.text()
        SD = self.sideD.text()
        height = self.heightTZ.text()
        trapValues = Quadrilateral.trapezoidCalc(SA, SB, SC, SD, height)
        self.trapValuesList.setText(trapValues)

    # function to clear all text boxes
    def clearTrap(self):
        self.sideA.setText("")
        self.sideB.setText("")
        self.sideC.setText("")
        self.sideD.setText("")
        self.heightTZ.setText("")
        self.trapValuesList.setText("")

class ParallelogramTab(QWidget):   
    def __init__(self):
        super().__init__()

        self.labelImg = QLabel(self)
        self.pgramImage = QPixmap('../images/quad/parallelogram.png')   
        self.labelImg.setPixmap(self.pgramImage)
        self.labelImg.move(150, 300)
        
    # All values label
        self.plgValuesList = QLabel(self)
        self.plgValuesList.setWordWrap(True)
        self.plgValuesList.setGeometry(605, 175, 410, 410)
        self.plgValuesList.setStyleSheet("border: 2px solid black;")
        self.plgValuesList.setFont(QFont('Arial', 16))
        self.plgValuesList.setAlignment(QtCore.Qt.AlignCenter)

    # Add Labels for sides
        self.label_sideA = QLabel("Side a: ", self)
        self.label_sideA.setGeometry(50, 900, 325, 50)
        self.label_sideA.setStyleSheet("border: 0px solid black;")
        self.label_sideA_Units = QLabel("units", self)
        self.label_sideA_Units.setGeometry(415, 900, 65, 50)
        
        self.label_sideB = QLabel("Side b: ", self)
        self.label_sideB.setGeometry(50, 1000, 325, 50)
        self.label_sideB.setStyleSheet("border: 0px solid black;")
        self.label_sideB_Units = QLabel("units", self)
        self.label_sideB_Units.setGeometry(415, 1000, 65, 50)
        self.label_sideB_Units.setStyleSheet("border: 0px solid black;")

        self.label_Height = QLabel("Height: ", self)
        self.label_Height.setGeometry(50, 1100, 325, 50)
        self.label_Height.setStyleSheet("border: 0px solid black;")
        self.label_Height_Units = QLabel("units", self)
        self.label_Height_Units.setGeometry(415, 1100, 65, 50)
        self.label_Height_Units.setStyleSheet("border: 0px solid black;")

    # Add Text Boxes for sides/angles
        self.sideA = QLineEdit("",self)
        self.sideA.setGeometry(200, 900, 200, 50)

        self.sideB = QLineEdit("",self)
        self.sideB.setGeometry(200, 1000, 200, 50)

        self.heightPG = QLineEdit("",self)
        self.heightPG.setGeometry(200, 1100, 200, 50)

    # Calculate Button
        self.calculateButton = QPushButton("Calculate", self)
        self.calculateButton.setFont(QFont('Arial', 11))
        self.calculateButton.setStyleSheet("background-color : darkCyan")
        self.calculateButton.setGeometry(605, 875, 180, 75)
        self.calculateButton.clicked.connect(self.calcParallelogram)

    # Clear Button
        self.clearButton = QPushButton("Clear", self)
        self.clearButton.setFont(QFont('Arial', 11))
        self.clearButton.setStyleSheet("background-color : red")
        self.clearButton.setGeometry(835, 875, 180, 75)
        self.clearButton.clicked.connect(self.clearParallelogram)
        
        self.show()
        vbox = QVBoxLayout()
        self.setLayout(vbox)

    # Calculates the triangle and displays values
    def calcParallelogram(self):
        sideA = self.sideA.text()
        sideB = self.sideB.text()
        height = self.heightPG.text()
        plgValues = Quadrilateral.parallelogramCalc(sideA, sideB, height)
        self.plgValuesList.setText(plgValues)

    # Clears all values of text boxes
    def clearParallelogram(self):
        self.sideA.setText("")
        self.sideB.setText("")
        self.heightPG.setText("")
        self.plgValuesList.setText("")

class RhombusTab(QWidget):   
    def __init__(self):
        super().__init__()

        self.labelImg = QLabel(self)
        self.rhombusImage = QPixmap('../images/quad/rhombus.png')   
        self.labelImg.setPixmap(self.rhombusImage)
        self.labelImg.move(150, 300)
        
    # All values label
        self.rhValuesList = QLabel(self)
        self.rhValuesList.setWordWrap(True)
        self.rhValuesList.setGeometry(605, 175, 410, 410)
        self.rhValuesList.setStyleSheet("border: 2px solid black;")
        self.rhValuesList.setFont(QFont('Arial', 16))
        self.rhValuesList.setAlignment(QtCore.Qt.AlignCenter)

    # Add Labels for sides
        self.label_sideA = QLabel("Side a: ", self)
        self.label_sideA.setGeometry(50, 900, 325, 50)
        self.label_sideA.setStyleSheet("border: 0px solid black;")
        self.label_sideA_Units = QLabel("units", self)
        self.label_sideA_Units.setGeometry(415, 900, 65, 50)
        
        self.label_Height = QLabel("Height: ", self)
        self.label_Height.setGeometry(50, 1000, 325, 50)
        self.label_Height.setStyleSheet("border: 0px solid black;")
        self.label_Height_Units = QLabel("units", self)
        self.label_Height_Units.setGeometry(415, 1000, 65, 50)
        self.label_Height_Units.setStyleSheet("border: 0px solid black;")

    # Add Text Boxes for sides/angles
        self.sideA = QLineEdit("",self)
        self.sideA.setGeometry(200, 900, 200, 50)

        self.heightRH = QLineEdit("",self)
        self.heightRH.setGeometry(200, 1000, 200, 50)

    # Calculate Button
        self.calculateButton = QPushButton("Calculate", self)
        self.calculateButton.setFont(QFont('Arial', 11))
        self.calculateButton.setStyleSheet("background-color : darkCyan")
        self.calculateButton.setGeometry(605, 875, 180, 75)
        self.calculateButton.clicked.connect(self.calcRhombus)

    # Clear Button
        self.clearButton = QPushButton("Clear", self)
        self.clearButton.setFont(QFont('Arial', 11))
        self.clearButton.setStyleSheet("background-color : red")
        self.clearButton.setGeometry(835, 875, 180, 75)
        self.clearButton.clicked.connect(self.clearRhombus)
        
        self.show()
        vbox = QVBoxLayout()
        self.setLayout(vbox)

    # Calculates the triangle and displays values
    def calcRhombus(self):
        sideA = self.sideA.text()
        height = self.heightRH.text()
        rectValues = Quadrilateral.rhombusCalc(sideA, height)
        self.rhValuesList.setText(rectValues)

    # Clears all values of text boxes
    def clearRhombus(self):
        self.sideA.setText("")
        self.heightRH.setText("")
        self.rhValuesList.setText("")
