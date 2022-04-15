from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTabWidget
from PyQt5.QtGui import QFont, QPixmap
from PyQt5 import QtCore
from Geometry import Triangle

"""
Triangle Window:
    Creates a window for geometric calculations with triangles,
    Called by the 'TabGeoCalc' class after the 'pushTriangle'
        button is clicked. This will open the 'Triangle' window
        upon the button click.        
"""
class TriangleWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.triTabs = QTabWidget()
        vbox = QVBoxLayout()

        sssTab = SSSTab()
        bhTab = BaseHeightTab()
        sasTab = SASTab()
        asaTab = ASATab()
        aasTab = AASTab()
        ssaTab = SSATab()

        self.triTabs.addTab(bhTab, "Base and Height")
        self.triTabs.addTab(sssTab, "SSS")
        self.triTabs.addTab(sasTab, "SAS")
        self.triTabs.addTab(asaTab, "ASA")
        self.triTabs.addTab(aasTab, "AAS")
        self.triTabs.addTab(ssaTab, "SSA")

        # Create new 'Triangle' Window
        self.setWindowTitle("Triangle")
        self.setGeometry(1000, 250, 1200, 1300)

        vbox.addWidget(self.triTabs)
        self.setLayout(vbox)

class SSSTab(QWidget):  
    def __init__(self):
        super().__init__()

    # Add shape
        self.labelImg = QLabel(self)
        self.sssImage = QPixmap('../images/triangle/triangleSSS.png')   
        self.labelImg.setPixmap(self.sssImage)
        self.labelImg.move(150, 300)

    # All values label
        self.sssValuesList = QLabel(self)
        self.sssValuesList.setWordWrap(True)
        self.sssValuesList.setGeometry(605, 175, 410, 410)
        self.sssValuesList.setStyleSheet("border: 2px solid black;")
        self.sssValuesList.setFont(QFont('Arial', 16))
        self.sssValuesList.setAlignment(QtCore.Qt.AlignCenter)

    # Add Labels for sides
        self.label_SA = QLabel("Side a: ", self)
        self.label_SA.setGeometry(50, 900, 325, 50)
        self.label_SA.setStyleSheet("border: 0px solid black;")
        self.label_SA_Units = QLabel("units", self)
        self.label_SA_Units.setGeometry(415, 900, 65, 50)
        self.label_SA_Units.setStyleSheet("border: 0px solid black;")

        self.label_SB = QLabel("Side b:", self)
        self.label_SB.setGeometry(50, 1000, 325, 50)
        self.label_SB.setStyleSheet("border: 0px solid black;")
        self.label_SB_Units = QLabel("units", self)
        self.label_SB_Units.setGeometry(415, 1000, 65, 50)
        self.label_SB_Units.setStyleSheet("border: 0px solid black;")

        self.label_SC = QLabel("Side c:", self)
        self.label_SC.setGeometry(50, 1100, 325, 50)
        self.label_SC.setStyleSheet("border: 0px solid black;")
        self.label_SC_Units = QLabel("units", self)
        self.label_SC_Units.setGeometry(415, 1100, 65, 50)
        self.label_SC_Units.setStyleSheet("border: 0px solid black;")

    # Add Text Boxes for sides
        self.sideA = QLineEdit(self)
        self.sideA.setGeometry(200, 900, 200, 50) 
        
        self.sideB = QLineEdit(self)
        self.sideB.setGeometry(200, 1000, 200, 50)

        self.sideC = QLineEdit(self)
        self.sideC.setGeometry(200, 1100, 200, 50)

    # Calculate Button
        self.calculateButton = QPushButton("Calculate", self)
        self.calculateButton.setFont(QFont('Arial', 11))
        self.calculateButton.setStyleSheet("background-color : darkCyan")
        self.calculateButton.setGeometry(605, 875, 180, 75)
        self.calculateButton.clicked.connect(self.calcSSSTriangle)
        
    # Clear Button
        self.clearButton = QPushButton("Clear", self)
        self.clearButton.setFont(QFont('Arial', 11))
        self.clearButton.setStyleSheet("background-color : red")
        self.clearButton.setGeometry(835, 875, 180, 75)
        self.clearButton.clicked.connect(self.clearSSSTri)

        self.show()
        vbox = QVBoxLayout()
        self.setLayout(vbox)

    # Calculates triangle and displays all values
    def calcSSSTriangle(self):
        S1 = self.sideA.text()
        S2 = self.sideB.text()
        S3 = self.sideC.text()
        allSSSVals = Triangle.sssCalc(S1, S2, S3)
        self.sssValuesList.setText(allSSSVals)

    # Clears all text boxes
    def clearSSSTri(self):
        self.sideA.setText("")
        self.sideB.setText("")
        self.sideC.setText("")
        self.sssValuesList.setText("")

class ASATab(QWidget):
    def __init__(self):
        super().__init__()
    
    # Add shape
        self.labelImg = QLabel(self)
        self.asaImage = QPixmap('../images/triangle/triangleASA.png')   
        self.labelImg.setPixmap(self.asaImage)
        self.labelImg.move(150, 300)

    # All values label
        self.asaValuesList = QLabel(self)
        self.asaValuesList.setWordWrap(True)
        self.asaValuesList.setGeometry(605, 175, 410, 410)
        self.asaValuesList.setStyleSheet("border: 2px solid black;")
        self.asaValuesList.setFont(QFont('Arial', 16))
        self.asaValuesList.setAlignment(QtCore.Qt.AlignCenter)

    # Add Labels for sides/angles
        self.label_AA = QLabel("Angle A: ", self)
        self.label_AA.setGeometry(50, 900, 325, 50)
        self.label_AA.setStyleSheet("border: 0px solid black;")
        self.label_AA_Deg = QLabel("degrees", self)
        self.label_AA_Deg.setGeometry(415, 900, 100, 50)
        self.label_AA_Deg.setStyleSheet("border: 0px solid black;")

        self.label_SideC = QLabel("Side c: ", self)
        self.label_SideC.setGeometry(50, 1000, 325, 50)
        self.label_SideC.setStyleSheet("border: 0px solid black;")
        self.label_SideC_Units = QLabel("units", self)
        self.label_SideC_Units.setGeometry(415, 1000, 65, 50)
        self.label_SideC_Units.setStyleSheet("border: 0px solid black;")

        self.label_AB = QLabel("Angle B: ", self)
        self.label_AB.setGeometry(50, 1100, 325, 50)
        self.label_AB.setStyleSheet("border: 0px solid black;")
        self.label_AB_Deg = QLabel("degrees", self)
        self.label_AB_Deg.setGeometry(415, 1100, 100, 50)
        self.label_AB_Deg.setStyleSheet("border: 0px solid black;")

    # Add Text Boxes for sides/angles
        self.angleA = QLineEdit("",self)
        self.angleA.setGeometry(200, 900, 200, 50)  
        
        self.sideC = QLineEdit(self)
        self.sideC.setGeometry(200, 1000, 200, 50)

        self.angleB = QLineEdit(self)
        self.angleB.setGeometry(200, 1100, 200, 50)

    # Calculate Button
        self.calculateButton = QPushButton("Calculate", self)
        self.calculateButton.setFont(QFont('Arial', 11))
        self.calculateButton.setStyleSheet("background-color : darkCyan")
        self.calculateButton.setGeometry(605, 875, 180, 75)
        self.calculateButton.clicked.connect(self.calcASATriangle)

    # Clear Button
        self.clearButton = QPushButton("Clear", self)
        self.clearButton.setFont(QFont('Arial', 11))
        self.clearButton.setStyleSheet("background-color : red")
        self.clearButton.setGeometry(835, 875, 180, 75)
        self.clearButton.clicked.connect(self.clearASATri)
        
        self.show()
        vbox = QVBoxLayout()
        self.setLayout(vbox)

    # Calculates triangle and displays values
    def calcASATriangle(self):
        A1 = self.angleA.text()
        S = self.sideC.text()
        A2 = self.angleB.text()
        asaValues = Triangle.asaCalc(A1, S, A2)
        self.asaValuesList.setText(asaValues)

    # Clears all text box values
    def clearASATri(self):
        self.angleA.setText("")
        self.sideC.setText("")
        self.angleB.setText("")
        self.asaValuesList.setText("")

class SASTab(QWidget):
    def __init__(self):
        super().__init__()
    
    # Add shape
        self.labelImg = QLabel(self)
        self.sasImage = QPixmap('../images/triangle/triangleSAS.png')   
        self.labelImg.setPixmap(self.sasImage)
        self.labelImg.move(150, 300)
    
    # All values label
        self.sasValuesList = QLabel(self)
        self.sasValuesList.setWordWrap(True)
        self.sasValuesList.setGeometry(605, 175, 410, 410)
        self.sasValuesList.setStyleSheet("border: 2px solid black;")
        self.sasValuesList.setFont(QFont('Arial', 16))
        self.sasValuesList.setAlignment(QtCore.Qt.AlignCenter)

    # Add Labels for sides/angles
        self.label_SB = QLabel("Side b: ", self)
        self.label_SB.setGeometry(50, 900, 325, 50)
        self.label_SB.setStyleSheet("border: 0px solid black;")
        self.label_SB_Units = QLabel("units", self)
        self.label_SB_Units.setGeometry(415, 900, 65, 50)
        self.label_SB_Units.setStyleSheet("border: 0px solid black;")

        self.label_AngleA = QLabel("Angle A: ", self)
        self.label_AngleA.setGeometry(50, 1000, 325, 50)
        self.label_AngleA.setStyleSheet("border: 0px solid black;")
        self.label_AngleA_Deg = QLabel("degrees", self)
        self.label_AngleA_Deg.setGeometry(415, 1000, 100, 50)
        self.label_AngleA_Deg.setStyleSheet("border: 0px solid black;")

        self.label_SC = QLabel("Side c: ", self)
        self.label_SC.setGeometry(50, 1100, 325, 50)
        self.label_SC.setStyleSheet("border: 0px solid black;")
        self.label_SC_Units = QLabel("units", self)
        self.label_SC_Units.setGeometry(415, 1100, 65, 50)
        self.label_SC_Units.setStyleSheet("border: 0px solid black;")

    # Add Text Boxes for sides/angles
        self.sideB = QLineEdit("",self)
        self.sideB.setGeometry(200, 900, 200, 50) 
        
        self.angleA = QLineEdit("",self)
        self.angleA.setGeometry(200, 1000, 200, 50)

        self.sideC = QLineEdit("",self)
        self.sideC.setGeometry(200, 1100, 200, 50)

    # Calculate Button
        self.calculateButton = QPushButton("Calculate", self)
        self.calculateButton.setFont(QFont('Arial', 11))
        self.calculateButton.setStyleSheet("background-color : darkCyan")
        self.calculateButton.setGeometry(605, 875, 180, 75)
        self.calculateButton.clicked.connect(self.calcSASTriangle)

    # Clear Button
        self.clearButton = QPushButton("Clear", self)
        self.clearButton.setFont(QFont('Arial', 11))
        self.clearButton.setStyleSheet("background-color : red")
        self.clearButton.setGeometry(835, 875, 180, 75)
        self.clearButton.clicked.connect(self.clearSASTri)
        
        self.show()
        vbox = QVBoxLayout()
        self.setLayout(vbox)

    # Calculates triangle and displays values
    def calcSASTriangle(self):
        S1 = self.sideB.text()
        A = self.angleA.text()
        S2 = self.sideC.text()
        allSASValues = Triangle.sasCalc(S1, A, S2)
        self.sasValuesList.setText(allSASValues)

    # Clears all text boxes
    def clearSASTri(self):
        self.sideB.setText("")
        self.angleA.setText("")
        self.sideC.setText("")
        self.sasValuesList.setText("")

class AASTab(QWidget):
    def __init__(self):
        super().__init__()
    
    # Add shape
        self.labelImg = QLabel(self)
        self.aasImage = QPixmap('../images/triangle/triangleAAS.png')   
        self.labelImg.setPixmap(self.aasImage)
        self.labelImg.move(150, 300)
    
    # All values label
        self.aasValuesList = QLabel(self)
        self.aasValuesList.setWordWrap(True)
        self.aasValuesList.setGeometry(605, 175, 410, 410)
        self.aasValuesList.setStyleSheet("border: 2px solid black;")
        self.aasValuesList.setFont(QFont('Arial', 16))
        self.aasValuesList.setAlignment(QtCore.Qt.AlignCenter)

    # Add Labels for sides/angles
        self.label_AngleA = QLabel("Angle A: ", self)
        self.label_AngleA.setGeometry(50, 900, 325, 50)
        self.label_AngleA.setStyleSheet("border: 0px solid black;")
        self.label_AngleA_Deg = QLabel("degrees", self)
        self.label_AngleA_Deg.setGeometry(415, 900, 100, 50)
        self.label_AngleA_Deg.setStyleSheet("border: 0px solid black;")

        self.label_AngleB = QLabel("Angle B: ", self)
        self.label_AngleB.setGeometry(50, 1000, 325, 50)
        self.label_AngleB.setStyleSheet("border: 0px solid black;")
        self.label_AngleB_Deg = QLabel("degrees", self)
        self.label_AngleB_Deg.setGeometry(415, 1000, 100, 50)
        self.label_AngleB_Deg.setStyleSheet("border: 0px solid black;")

        self.label_SA = QLabel("Side a: ", self)
        self.label_SA.setGeometry(50, 1100, 325, 50)
        self.label_SA.setStyleSheet("border: 0px solid black;")
        self.label_SA_Units = QLabel("units", self)
        self.label_SA_Units.setGeometry(415, 1100, 65, 50)
        self.label_SA_Units.setStyleSheet("border: 0px solid black;")

    # Add Text Boxes for sides/angles
        self.angleA = QLineEdit("",self)
        self.angleA.setGeometry(200, 900, 200, 50) 
        
        self.angleB = QLineEdit(self)
        self.angleB.setGeometry(200, 1000, 200, 50)

        self.sideA = QLineEdit(self)
        self.sideA.setGeometry(200, 1100, 200, 50)

    # Calculate Button
        self.calculateButton = QPushButton("Calculate", self)
        self.calculateButton.setFont(QFont('Arial', 11))
        self.calculateButton.setStyleSheet("background-color : darkCyan")
        self.calculateButton.setGeometry(605, 875, 180, 75)
        self.calculateButton.clicked.connect(self.calcAASTriangle)

    # Clear Button
        self.clearButton = QPushButton("Clear", self)
        self.clearButton.setFont(QFont('Arial', 11))
        self.clearButton.setStyleSheet("background-color : red")
        self.clearButton.setGeometry(835, 875, 180, 75)
        self.clearButton.clicked.connect(self.clearAASTri)
        
        self.show()
        vbox = QVBoxLayout()
        self.setLayout(vbox)

    # function that calcualtes the triangle and displays values
    def calcAASTriangle(self):
        A1 = self.angleA.text()
        A2 = self.angleB.text()
        S1 = self.sideA.text()
        aasValues = Triangle.aasCalc(A1, A2, S1)
        self.aasValuesList.setText(aasValues)

    # function to clear all text boxes
    def clearAASTri(self):
        self.angleA.setText("")
        self.angleB.setText("")
        self.sideA.setText("")
        self.aasValuesList.setText("")

class SSATab(QWidget):
    def __init__(self):
        super().__init__()
        
    # Add shape image
        self.labelImg = QLabel(self)
        self.ssaImage = QPixmap('../images/triangle/triangleSSA.png')   
        self.labelImg.setPixmap(self.ssaImage)
        self.labelImg.move(150, 300)
    
    # All values label
        self.ssaValuesList = QLabel(self)
        self.ssaValuesList.setWordWrap(True)
        self.ssaValuesList.setGeometry(605, 175, 410, 410)
        self.ssaValuesList.setStyleSheet("border: 2px solid black;")
        self.ssaValuesList.setFont(QFont('Arial', 16))
        self.ssaValuesList.setAlignment(QtCore.Qt.AlignCenter)

    # Add Labels for sides/angles
        self.label_SA = QLabel("Side a: ", self)
        self.label_SA.setGeometry(50, 900, 325, 50)
        self.label_SA.setStyleSheet("border: 0px solid black;")
        self.label_SA_Units = QLabel("units", self)
        self.label_SA_Units.setGeometry(415, 900, 65, 50)
        self.label_SA_Units.setStyleSheet("border: 0px solid black;")

        self.label_SB = QLabel("Side b: ", self)
        self.label_SB.setGeometry(50, 1000, 325, 50)
        self.label_SB.setStyleSheet("border: 0px solid black;")
        self.label_SB_Units = QLabel("units", self)
        self.label_SB_Units.setGeometry(415, 1000, 65, 50)
        self.label_SB_Units.setStyleSheet("border: 0px solid black;")
        
        self.label_Angle = QLabel("Angle A: ", self)
        self.label_Angle.setGeometry(50, 1100, 325, 50)
        self.label_Angle.setStyleSheet("border: 0px solid black;")
        self.label_Angle_Deg = QLabel("degrees", self)
        self.label_Angle_Deg.setGeometry(415, 1100, 100, 50)
        self.label_Angle_Deg.setStyleSheet("border: 0px solid black;")

    # Add Text Boxes for sides/angles
        self.sideA = QLineEdit("",self)
        self.sideA.setGeometry(200, 900, 200, 50)
        
        self.sideB = QLineEdit(self)
        self.sideB.setGeometry(200, 1000, 200, 50)

        self.angleA = QLineEdit(self)
        self.angleA.setGeometry(200, 1100, 200, 50)

    # Calculate Button
        self.calculateButton = QPushButton("Calculate", self)
        self.calculateButton.setFont(QFont('Arial', 11))
        self.calculateButton.setStyleSheet("background-color : darkCyan")
        self.calculateButton.setGeometry(605, 875, 180, 75)
        self.calculateButton.clicked.connect(self.calcSSATriangle)

    # Clear Button
        self.clearButton = QPushButton("Clear", self)
        self.clearButton.setFont(QFont('Arial', 11))
        self.clearButton.setStyleSheet("background-color : red")
        self.clearButton.setGeometry(835, 875, 180, 75)
        self.clearButton.clicked.connect(self.clearSSATri)
        
        self.show()
        vbox = QVBoxLayout()
        self.setLayout(vbox)

    # Calculates the triangle and displays values
    def calcSSATriangle(self):
        S1 = self.sideA.text()
        S2 = self.sideB.text()
        A1 = self.angleA.text()
        ssaValues = Triangle.ssaCalc(S1, S2, A1)
        self.ssaValuesList.setText(ssaValues)

    # Clears all values of text boxes
    def clearSSATri(self):
        self.sideA.setText("")
        self.sideB.setText("")
        self.angleA.setText("")
        self.ssaValuesList.setText("")

class BaseHeightTab(QWidget):
    def __init__(self):
        super().__init__()
        
        # Add shape
        self.labelImg = QLabel(self)
        self.bhImage = QPixmap('../images/triangle/triangleBH.png')   
        self.labelImg.setPixmap(self.bhImage)
        self.labelImg.move(150, 300)
    
    # Result Labels; Area
        # Area Label with Area Result Label
        self.labelArea = QLabel("Area:                                            units²", self)
        self.labelArea.setGeometry(555, 1000, 600, 50)
        self.labelArea.setStyleSheet("border: 0px solid black;")
        self.labelArea.setFont(QFont('Arial', 10))

        self.labelAreaResult_BH = QLabel("", self) # Area Result
        self.labelAreaResult_BH.setGeometry(700, 1000, 300, 50)
        self.labelAreaResult_BH.setStyleSheet("border: 1px solid black;")
        self.labelAreaResult_BH.setFont(QFont('Arial', 10))

    # Add Labels for base/height
       # Side Labels
        self.label_Base = QLabel("Base: ", self)
        self.label_Base.setGeometry(50, 1000, 325, 50)
        self.label_Base.setStyleSheet("border: 0px solid black;")
        self.label_BaseUnits = QLabel("units", self)
        self.label_BaseUnits.setGeometry(415, 1000, 65, 50)
        self.label_BaseUnits.setStyleSheet("border: 0px solid black;")

        self.label_Height = QLabel("Height: ", self)
        self.label_Height.setGeometry(50, 1100, 325, 50)
        self.label_Height.setStyleSheet("border: 0px solid black;")
        self.label_BaseUnits = QLabel("units", self)
        self.label_BaseUnits.setGeometry(415, 1100, 65, 50)
        self.label_BaseUnits.setStyleSheet("border: 0px solid black;")

    # Add Text Boxes for base/height
        # Side Text Boxes
        self.base = QLineEdit("",self)
        self.base.setGeometry(175, 1000, 200, 50)
        
        self.heightBH = QLineEdit(self)
        self.heightBH.setGeometry(175, 1100, 200, 50)

        # Calculate Button
        self.calculateButton = QPushButton("Calculate", self)
        self.calculateButton.setFont(QFont('Arial', 11))
        self.calculateButton.setStyleSheet("background-color : darkCyan")
        self.calculateButton.setGeometry(320, 875, 180, 75)
        self.calculateButton.clicked.connect(self.calcBHTriangle)

        # Clear Button
        self.clearButton = QPushButton("Clear", self)
        self.clearButton.setFont(QFont('Arial', 11))
        self.clearButton.setStyleSheet("background-color : red")
        self.clearButton.setGeometry(650, 875, 180, 75)
        self.clearButton.clicked.connect(self.clearBHTri)
        
        self.show()
        vbox = QVBoxLayout()
        self.setLayout(vbox)

    def calcBHTriangle(self):
    
        # Set variables to pass and change to text
        b = self.base.text()
        h = self.heightBH.text()

        area = Triangle.baseHeightCalc(b, h)
        area = str(area)

        self.labelAreaResult_BH.setText(area)

    # Clears all values of triangle inputs
    def clearBHTri(self):

        self.base.setText("")
        self.heightBH.setText("")
        self.labelAreaResult_BH.setText("")
