from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont, QPixmap
from PyQt5 import QtCore
from sympy import symbols
from Calculus import Calculus


class DerivativeTab(QWidget):
    def __init__(self):
        super().__init__()
    
    # Add Derivative image
        self.labelDDx = QLabel(self)
        self.DDxImage = QPixmap('../images/calculus/derivative.png')   
        self.labelDDx.setPixmap(self.DDxImage)
        self.labelDDx.move(150, 300)
        
    # Result Labels 
        self.labelDeriv = QLabel("Value of the derivative :", self)
        self.labelDeriv.setGeometry(95, 650, 205, 50)
        self.labelDeriv.setStyleSheet("border: 0px solid black;")
        self.labelDeriv.setFont(QFont('Arial', 14))
        self.labelDerivResult = QLabel("", self) # Derivative Result
        self.labelDerivResult.setGeometry(300, 650, 450, 50)
        self.labelDerivResult.setStyleSheet("border: 2px solid black;")
        self.labelDerivResult.setFont(QFont('Arial', 18))

    # Guide Message
        Guide = """Enter your equation and the variable you would like to derive.\n
    NOTE: Please enter a '*' when multiplying with a variable.
        Example: '2x' should be entered as '2*x'""" 
        self.labelSteps = QLabel(Guide, self)
        self.labelSteps.setGeometry(75, 75, 550, 100)
        self.labelSteps.setStyleSheet("border: 3px solid red;")
        self.labelSteps.setFont(QFont('Arial', 14))

    # Add Text Boxes for values
        self.dSymbol = QLineEdit("", self)
        self.dSymbol.setMaxLength(1)
        self.dSymbol.setGeometry(225, 400, 50, 50)
        self.dSymbol.setPlaceholderText("X")
        self.dSymbol.setAlignment(QtCore.Qt.AlignCenter)
        self.dSymbol.setStyleSheet("border: 2px solid black;")
        self.dSymbol.setFont(QFont('Arial', 22))
        
        self.dEquation = QLineEdit("", self)
        self.dEquation.setGeometry(300, 360, 300, 50)
        self.dEquation.setPlaceholderText("Equation")
        self.dEquation.setAlignment(QtCore.Qt.AlignCenter)
        self.dEquation.setStyleSheet("border: 2px solid black;")
        self.dEquation.setFont(QFont('Arial', 18))

        # Calculate Button
        self.calculateButton = QPushButton("Calculate", self)
        self.calculateButton.setFont(QFont('Arial', 11))
        self.calculateButton.setStyleSheet("background-color : darkCyan")
        self.calculateButton.setGeometry(175, 500, 180, 75)
        self.calculateButton.clicked.connect(self.calcDerivative)

        # Clear Button
        self.clearButton = QPushButton("Clear", self)
        self.clearButton.setFont(QFont('Arial', 11))
        self.clearButton.setStyleSheet("background-color : red")
        self.clearButton.setGeometry(455, 500, 180, 75)
        self.clearButton.clicked.connect(self.clearDerivative)
        
        vbox = QVBoxLayout()
        self.show()
        self.setLayout(vbox)

    # Calculates The derivative
    def calcDerivative(self):
        symbolX = self.dSymbol.text()
        equationD = self.dEquation.text()

        resultDer = Calculus.calcDerivative(symbolX, equationD)
        self.labelDerivResult.setText(str(resultDer))

    # Clears all values of inputs
    def clearDerivative(self):
        self.dSymbol.setText("")
        self.dEquation.setText("")
        self.labelDerivResult.setText("")

class IntegralTab(QWidget):
    def __init__(self):
        super().__init__()
    
    # Add integral images
        self.labelIntg = QLabel(self)
        self.IntegralImage = QPixmap('../images/calculus/integral.png')   
        self.labelIntg.setPixmap(self.IntegralImage)
        self.labelIntg.move(175, 300)

        self.labelInt_dx = QLabel(self)
        self.IntegraldxImage = QPixmap('../images/calculus/integral-dx.png')   
        self.labelInt_dx.setPixmap(self.IntegraldxImage)
        self.labelInt_dx.move(735, 310)
        
    # Result Labels 
        self.labelIntegral = QLabel("Value of the integral :", self)
        self.labelIntegral.setGeometry(95, 535, 205, 50)
        self.labelIntegral.setStyleSheet("border: 0px solid black;")
        self.labelIntegral.setFont(QFont('Arial', 14))
        self.labelIntegralResult = QLabel("", self) # Integral Result
        self.labelIntegralResult.setGeometry(300, 535, 450, 50)
        self.labelIntegralResult.setStyleSheet("border: 2px solid black;")
        self.labelIntegralResult.setFont(QFont('Arial', 18))

    # Guide Message
        Guide = """Enter your equation and the variable you would like to integrate.
    Enter the bounds (a,b) if you desire, otherwise leave blank.\n
    NOTE: Please enter a '*' when multiplying with a variable.
        Example: '2x' should be entered as '2*x'""" 
        self.labelSteps = QLabel(Guide, self)
        self.labelSteps.setGeometry(75, 75, 550, 150)
        self.labelSteps.setStyleSheet("border: 3px solid red;")
        self.labelSteps.setFont(QFont('Arial', 14))

    # Add Text Boxes for values
        self.IntSymbol = QLineEdit("", self)
        self.IntSymbol.setMaxLength(1)
        self.IntSymbol.setGeometry(835, 370, 50, 50)
        self.IntSymbol.setPlaceholderText("X")
        self.IntSymbol.setAlignment(QtCore.Qt.AlignCenter)
        self.IntSymbol.setStyleSheet("border: 2px solid black;")
        self.IntSymbol.setFont(QFont('Arial', 22))
        
        self.IntEquation = QLineEdit("", self)
        self.IntEquation.setGeometry(300, 375, 450, 50)
        self.IntEquation.setPlaceholderText("Equation")
        self.IntEquation.setAlignment(QtCore.Qt.AlignCenter)
        self.IntEquation.setStyleSheet("border: 2px solid black;")
        self.IntEquation.setFont(QFont('Arial', 18))

        self.IntLowerBound = QLineEdit("", self)
        self.IntLowerBound.setGeometry(270, 300, 50, 50)
        self.IntLowerBound.setPlaceholderText("b")
        self.IntLowerBound.setAlignment(QtCore.Qt.AlignCenter)
        self.IntLowerBound.setStyleSheet("border: 2px solid black;")
        self.IntLowerBound.setFont(QFont('Arial', 22))

        self.IntUpperBound = QLineEdit("", self)
        self.IntUpperBound.setGeometry(230, 450, 50, 50)
        self.IntUpperBound.setPlaceholderText("a")
        self.IntUpperBound.setAlignment(QtCore.Qt.AlignCenter)
        self.IntUpperBound.setStyleSheet("border: 2px solid black;")
        self.IntUpperBound.setFont(QFont('Arial', 22))

       # Calculate Button
        self.calculateButton = QPushButton("Calculate", self)
        self.calculateButton.setFont(QFont('Arial', 11))
        self.calculateButton.setStyleSheet("background-color : darkCyan")
        self.calculateButton.setGeometry(300, 650, 180, 75)
        self.calculateButton.clicked.connect(self.calcIntegral)

        # Clear Button
        self.clearButton = QPushButton("Clear", self)
        self.clearButton.setFont(QFont('Arial', 11))
        self.clearButton.setStyleSheet("background-color : red")
        self.clearButton.setGeometry(570, 650, 180, 75)
        self.clearButton.clicked.connect(self.clearIntegral)
        
        vbox = QVBoxLayout()
        self.show()
        self.setLayout(vbox)

    # Calculates Integral
    def calcIntegral(self):
        symbolX = self.IntSymbol.text()
        equationI = self.IntEquation.text()
        a = self.IntUpperBound.text()
        b = self.IntLowerBound.text()

        resultInt = Calculus.calcIntegral(equationI, symbolX, a, b)
        self.labelIntegralResult.setText(str(resultInt))

    # Clears all values of inputs
    def clearIntegral(self):
        self.IntSymbol.setText("")
        self.IntEquation.setText("")
        self.IntUpperBound.setText("")
        self.IntLowerBound.setText("")
        self.labelIntegralResult.setText("")

class LimitTab(QWidget):
    def __init__(self):
        super().__init__()
    
    # Add limit image 
        self.labelLim = QLabel(self)
        self.LimitImage = QPixmap('../images/calculus/limit.png')   
        self.labelLim.setPixmap(self.LimitImage)
        self.labelLim.move(175, 300)

    # Result Labels 
        self.labelLimit = QLabel("Value of the Limit :", self)
        self.labelLimit.setGeometry(130, 535, 205, 50)
        self.labelLimit.setStyleSheet("border: 0px solid black;")
        self.labelLimit.setFont(QFont('Arial', 14))
        self.labelLimitResult = QLabel("", self) # Integral Result
        self.labelLimitResult.setGeometry(315, 535, 450, 50)
        self.labelLimitResult.setStyleSheet("border: 2px solid black;")
        self.labelLimitResult.setFont(QFont('Arial', 18))

    # Guide Message
        Guide = """Enter your equation and the variables for 'x' approaching 'a'.\n
    NOTE: Please enter a '*' when multiplying with a variable.
        Example: '2x' should be entered as '2*x'""" 
        self.labelSteps = QLabel(Guide, self)
        self.labelSteps.setGeometry(75, 75, 550, 100)
        self.labelSteps.setStyleSheet("border: 3px solid red;")
        self.labelSteps.setFont(QFont('Arial', 14))

    # Add Text Boxes for values
        self.LimitEquation = QLineEdit("", self)
        self.LimitEquation.setGeometry(315, 350, 450, 50)
        self.LimitEquation.setPlaceholderText("Equation")
        self.LimitEquation.setAlignment(QtCore.Qt.AlignCenter)
        self.LimitEquation.setStyleSheet("border: 2px solid black;")
        self.LimitEquation.setFont(QFont('Arial', 18))

        self.LimitA = QLineEdit("", self)
        self.LimitA.setGeometry(255, 395, 50, 50)
        self.LimitA.setPlaceholderText("a")
        self.LimitA.setAlignment(QtCore.Qt.AlignCenter)
        self.LimitA.setStyleSheet("border: 2px solid black;")
        self.LimitA.setFont(QFont('Arial', 22))

        self.LimitX = QLineEdit("", self)
        self.LimitX.setMaxLength(1)
        self.LimitX.setGeometry(160, 395, 50, 50)
        self.LimitX.setPlaceholderText("x")
        self.LimitX.setAlignment(QtCore.Qt.AlignCenter)
        self.LimitX.setStyleSheet("border: 2px solid black;")
        self.LimitX.setFont(QFont('Arial', 22))

       # Calculate Button
        self.calculateButton = QPushButton("Calculate", self)
        self.calculateButton.setFont(QFont('Arial', 11))
        self.calculateButton.setStyleSheet("background-color : darkCyan")
        self.calculateButton.setGeometry(300, 650, 180, 75)
        self.calculateButton.clicked.connect(self.calcLimit)

        # Clear Button
        self.clearButton = QPushButton("Clear", self)
        self.clearButton.setFont(QFont('Arial', 11))
        self.clearButton.setStyleSheet("background-color : red")
        self.clearButton.setGeometry(570, 650, 180, 75)
        self.clearButton.clicked.connect(self.clearLimit)
        
        vbox = QVBoxLayout()
        self.show()
        self.setLayout(vbox)

    # Calculates Limit
    def calcLimit(self):
        equationI = self.LimitEquation.text()
        x = self.LimitX.text()
        a = self.LimitA.text()

        resultLimit = Calculus.calcLimit(equationI, x, a)
        self.labelLimitResult.setText(str(resultLimit))

    # Clears all values of inputs
    def clearLimit(self):
        self.LimitEquation.setText("")
        self.LimitX.setText("")
        self.LimitA.setText("")
        self.labelLimitResult.setText("")

