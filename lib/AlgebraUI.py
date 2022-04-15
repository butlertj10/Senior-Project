from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5 import QtCore
from Algebra import AlgCalc


class PolyRootsTab(QWidget):
    def __init__(self):
        super().__init__()
    
    # Result Labels 
        self.labelRoots = QLabel("Roots of the polynomial are :", self)
        self.labelRoots.setGeometry(95, 650, 205, 50)
        self.labelRoots.setStyleSheet("border: 0px solid black;")
        self.labelRoots.setFont(QFont('Arial', 14))
        self.labelRootsResult = QLabel("", self) # Roots Result
        self.labelRootsResult.setGeometry(310, 650, 450, 50)
        self.labelRootsResult.setStyleSheet("border: 2px solid black;")
        self.labelRootsResult.setFont(QFont('Arial', 18))

    # Add Text Boxes for values
        self.labelRootsSymbol = QLabel("Variable to solve:", self)
        self.labelRootsSymbol.setGeometry(95, 250, 205, 50)
        self.labelRootsSymbol.setStyleSheet("border: 0px solid black;")
        self.labelRootsSymbol.setFont(QFont('Arial', 14))
        self.rootsSymbol = QLineEdit("", self)
        self.rootsSymbol.setMaxLength(1)
        self.rootsSymbol.setGeometry(250, 250, 50, 50)
        self.rootsSymbol.setPlaceholderText("X")
        self.rootsSymbol.setAlignment(QtCore.Qt.AlignCenter)
        self.rootsSymbol.setStyleSheet("border: 2px solid black;")
        self.rootsSymbol.setFont(QFont('Arial', 22))
        
        self.labelRootsEq = QLabel("Equation:", self)
        self.labelRootsEq.setGeometry(160, 360, 205, 50)
        self.labelRootsEq.setStyleSheet("border: 0px solid black;")
        self.labelRootsEq.setFont(QFont('Arial', 14))
        self.rootsEquation = QLineEdit("", self)
        self.rootsEquation.setGeometry(250, 360, 350, 50)
        self.rootsEquation.setPlaceholderText("Equation")
        self.rootsEquation.setAlignment(QtCore.Qt.AlignCenter)
        self.rootsEquation.setStyleSheet("border: 2px solid black;")
        self.rootsEquation.setFont(QFont('Arial', 18))

        # Calculate Button
        self.calculateButton = QPushButton("Calculate", self)
        self.calculateButton.setFont(QFont('Arial', 11))
        self.calculateButton.setStyleSheet("background-color : darkCyan")
        self.calculateButton.setGeometry(175, 500, 180, 75)
        self.calculateButton.clicked.connect(self.calcRoots)

        # Clear Button
        self.clearButton = QPushButton("Clear", self)
        self.clearButton.setFont(QFont('Arial', 11))
        self.clearButton.setStyleSheet("background-color : red")
        self.clearButton.setGeometry(455, 500, 180, 75)
        self.clearButton.clicked.connect(self.clearRoots)
        
        vbox = QVBoxLayout()
        self.show()
        self.setLayout(vbox)

    # Calculates The Roots
    def calcRoots(self):
        symbolX = self.rootsSymbol.text()
        equationRoots = self.rootsEquation.text()

        resultRoots = AlgCalc.calcPolyRoots(symbolX, equationRoots)
        self.labelRootsResult.setText(str(resultRoots))

    # Clears all values of inputs
    def clearRoots(self):
        self.rootsSymbol.setText("")
        self.rootsEquation.setText("")
        self.labelRootsResult.setText("")

class FactorTab(QWidget):
    def __init__(self):
        super().__init__()
    
    # Result Labels 
        self.labelExpSimp = QLabel("Expanded/Simplified polynomial is :", self)
        self.labelExpSimp.setGeometry(25, 360, 310, 50)
        self.labelExpSimp.setStyleSheet("border: 0px solid black;")
        self.labelExpSimp.setFont(QFont('Arial', 14))
        self.labelExpSimpResult = QLabel("", self) # Exp/Simp Result
        self.labelExpSimpResult.setGeometry(335, 360, 450, 50)
        self.labelExpSimpResult.setStyleSheet("border: 2px solid black;")
        self.labelExpSimpResult.setFont(QFont('Arial', 18))

    # Add Text Boxes for values
        self.labelESEq = QLabel("Equation:", self)
        self.labelESEq.setGeometry(160, 240, 205, 50)
        self.labelESEq.setStyleSheet("border: 0px solid black;")
        self.labelESEq.setFont(QFont('Arial', 14))
        self.esEquation = QLineEdit("", self)
        self.esEquation.setGeometry(250, 240, 350, 50)
        self.esEquation.setPlaceholderText("Equation")
        self.esEquation.setAlignment(QtCore.Qt.AlignCenter)
        self.esEquation.setStyleSheet("border: 2px solid black;")
        self.esEquation.setFont(QFont('Arial', 18))

        # Calculate Expand Button
        self.calculateButton = QPushButton("Expand", self)
        self.calculateButton.setFont(QFont('Arial', 11))
        self.calculateButton.setStyleSheet("background-color : darkCyan")
        self.calculateButton.setGeometry(175, 500, 180, 75)
        self.calculateButton.clicked.connect(self.calcExp)

        # Calculate Simplify Button
        self.calculateButton = QPushButton("Simplfy", self)
        self.calculateButton.setFont(QFont('Arial', 11))
        self.calculateButton.setStyleSheet("background-color : darkCyan")
        self.calculateButton.setGeometry(735, 500, 180, 75)
        self.calculateButton.clicked.connect(self.calcSimp)

        # Clear Button
        self.clearButton = QPushButton("Clear", self)
        self.clearButton.setFont(QFont('Arial', 11))
        self.clearButton.setStyleSheet("background-color : red")
        self.clearButton.setGeometry(455, 500, 180, 75)
        self.clearButton.clicked.connect(self.clearExpSimp)
        
        vbox = QVBoxLayout()
        self.show()
        self.setLayout(vbox)

    # Calculates The expansion
    def calcExp(self):
        equationExp = self.esEquation.text()

        resultExp = AlgCalc.calcExpand(equationExp)
        self.labelExpSimpResult.setText(str(resultExp))

    # Calculates The simplified equation
    def calcSimp(self):
        equationSimp = self.esEquation.text()
        
        resultSimp = AlgCalc.calcSimp(equationSimp)
        self.labelExpSimpResult.setText(str(resultSimp))

    # Clears all values of inputs
    def clearExpSimp(self):
        self.esEquation.setText("")
        self.labelExpSimpResult.setText("")

class InequalityTab(QWidget):
    def __init__(self):
        super().__init__()

