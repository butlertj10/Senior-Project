from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont

from Finance import Finance


class SimpleInterestTab(QWidget):
    def __init__(self):
        super().__init__()
    
    # Result Labels 
        self.labelInterest = QLabel("Interest: $ ", self)
        self.labelInterest.setGeometry(50, 650, 325, 50)
        self.labelInterest.setStyleSheet("border: 0px solid black;")
        self.labelInterest.setFont(QFont('Arial', 10))
        self.labelInterestResult = QLabel("", self) # Interest Result
        self.labelInterestResult.setGeometry(225, 650, 300, 50)
        self.labelInterestResult.setStyleSheet("border: 1px solid black;")
        self.labelInterestResult.setFont(QFont('Arial', 10))

        self.labelTotal = QLabel("Total: $ ", self)
        self.labelTotal.setGeometry(50, 750, 325, 50)
        self.labelTotal.setStyleSheet("border: 0px solid black;")
        self.labelTotal.setFont(QFont('Arial', 10))
        self.labelTotalResult = QLabel("", self) # Total Result
        self.labelTotalResult.setGeometry(225, 750, 300, 50)
        self.labelTotalResult.setStyleSheet("border: 1px solid black;")
        self.labelTotalResult.setFont(QFont('Arial', 10))

    # Add Labels for values
        self.label_P = QLabel("Principle:   $ ", self)
        self.label_P.setGeometry(50, 350, 325, 50)
        self.label_P.setStyleSheet("border: 0px solid black;")

        self.label_Rate = QLabel("Rate:     % ", self)
        self.label_Rate.setGeometry(75, 450, 325, 50)
        self.label_Rate.setStyleSheet("border: 0px solid black;")

        self.label_Time = QLabel("Time (Years): ", self)
        self.label_Time.setGeometry(50, 550, 325, 50)
        self.label_Time.setStyleSheet("border: 0px solid black;")

    # Add Text Boxes for values
        self.siPrinc = QLineEdit("",self)
        self.siPrinc.setGeometry(225, 350, 200, 50)
        
        self.siRate = QLineEdit(self)
        self.siRate.setGeometry(225, 450, 200, 50)

        self.siTime = QLineEdit(self)
        self.siTime.setGeometry(225, 550, 200, 50)

        # Calculate Button
        self.calculateButton = QPushButton("Calculate", self)
        self.calculateButton.setFont(QFont('Arial', 11))
        self.calculateButton.setStyleSheet("background-color : darkCyan")
        self.calculateButton.setGeometry(450, 350, 180, 75)
        self.calculateButton.clicked.connect(self.calcSimInt)

        # Clear Button
        self.clearButton = QPushButton("Clear", self)
        self.clearButton.setFont(QFont('Arial', 11))
        self.clearButton.setStyleSheet("background-color : red")
        self.clearButton.setGeometry(450, 525, 180, 75)
        self.clearButton.clicked.connect(self.clearSimInt)
        
        vbox = QVBoxLayout()
        self.setLayout(vbox)

    # Calculates Simple Interest
    def calcSimInt(self):
        siP = self.siPrinc.text()
        siR = self.siRate.text()
        siT = self.siTime.text()

        siI, siTotal = Finance.calcSimpleInterest(siP, siR, siT)
        self.labelInterestResult.setText(str(siI))
        self.labelTotalResult.setText(str(siTotal))

    # Clears all values of inputs
    def clearSimInt(self):

        self.siPrinc.setText("")
        self.siRate.setText("")
        self.siTime.setText("")
        self.labelInterestResult.setText("")
        self.labelTotalResult.setText("")
class CompoundInterestTab(QWidget):
    def __init__(self):
        super().__init__()
    
    # Result Labels
        self.labelInterest = QLabel("Accrued Amount: $ ", self)
        self.labelInterest.setGeometry(50, 750, 325, 50)
        self.labelInterest.setStyleSheet("border: 0px solid black;")
        self.labelInterest.setFont(QFont('Arial', 10))

        self.labelInterestResult = QLabel("", self)
        self.labelInterestResult.setGeometry(355, 750, 365, 50)
        self.labelInterestResult.setStyleSheet("border: 1px solid black;")
        self.labelInterestResult.setFont(QFont('Arial', 10))

    # Add Labels for values
        self.label_P = QLabel("Principle:              $", self)
        self.label_P.setGeometry(50, 350, 325, 50)
        self.label_P.setStyleSheet("border: 0px solid black;")

        self.label_Rate = QLabel("Rate (%): ", self)
        self.label_Rate.setGeometry(50, 450, 325, 50)
        self.label_Rate.setStyleSheet("border: 0px solid black;")

        self.label_Time = QLabel("Time (Years): ", self)
        self.label_Time.setGeometry(50, 550, 325, 50)
        self.label_Time.setStyleSheet("border: 0px solid black;")

        self.label_Comp = QLabel("Compound (12/Yr): ", self)
        self.label_Comp.setGeometry(50, 650, 325, 50)
        self.label_Comp.setStyleSheet("border: 0px solid black;")

    # Add Text Boxes for values
        self.ciPrinc = QLineEdit("",self)
        self.ciPrinc.setGeometry(300, 350, 200, 50) 
        
        self.ciRate = QLineEdit(self)
        self.ciRate.setGeometry(300, 450, 200, 50)

        self.ciTime = QLineEdit(self)
        self.ciTime.setGeometry(300, 550, 200, 50)

        self.ciComp = QLineEdit(self)
        self.ciComp.setGeometry(300, 650, 200, 50)

    # Calculate Button
        self.calculateButton = QPushButton("Calculate", self)
        self.calculateButton.setFont(QFont('Arial', 11))
        self.calculateButton.setStyleSheet("background-color : darkCyan")
        self.calculateButton.setGeometry(525, 350, 180, 75)
        self.calculateButton.clicked.connect(self.calcCompInt)
        
    # Clear Button
        self.clearButton = QPushButton("Clear", self)
        self.clearButton.setFont(QFont('Arial', 11))
        self.clearButton.setStyleSheet("background-color : red")
        self.clearButton.setGeometry(525, 525, 180, 75)
        self.clearButton.clicked.connect(self.clearCompInt)
        
        vbox = QVBoxLayout()
        self.setLayout(vbox)

# Calculates Compound Interest
    def calcCompInt(self):
        ciP = self.ciPrinc.text()
        ciR = self.ciRate.text()
        ciT = self.ciTime.text()
        ciN = self.ciComp.text()

        ciA = Finance.calcCompoundInterest(ciP, ciR, ciT, ciN)
        self.labelInterestResult.setText(str(ciA))

# Clears all values of inputs
    def clearCompInt(self):
        self.ciPrinc.setText("")
        self.ciRate.setText("")
        self.ciTime.setText("")
        self.ciComp.setText("")
        self.labelInterestResult.setText("")
class PresentValueTab(QWidget):
    def __init__(self):
        super().__init__()
    
    # Result Labels
        self.labelInterest = QLabel("Present Value: $ ", self)
        self.labelInterest.setGeometry(50, 650, 325, 50)
        self.labelInterest.setStyleSheet("border: 0px solid black;")
        self.labelInterest.setFont(QFont('Arial', 10))

        self.labelInterestResult = QLabel("", self)
        self.labelInterestResult.setGeometry(320, 650, 300, 50)
        self.labelInterestResult.setStyleSheet("border: 1px solid black;")
        self.labelInterestResult.setFont(QFont('Arial', 10))

    # Add Labels for values
        self.label_FV = QLabel("Future Value: $ ", self)
        self.label_FV.setGeometry(50, 350, 325, 50)
        self.label_FV.setStyleSheet("border: 0px solid black;")

        self.label_Rate = QLabel("Rate (%):  ", self)
        self.label_Rate.setGeometry(50, 450, 325, 50)
        self.label_Rate.setStyleSheet("border: 0px solid black;")

        self.label_Per = QLabel("Periods: ", self)
        self.label_Per.setGeometry(50, 550, 325, 50)
        self.label_Per.setStyleSheet("border: 0px solid black;")

    # Add Text Boxes for values
        self.pvFutVal = QLineEdit("",self)
        self.pvFutVal.setGeometry(250, 350, 200, 50) 

        self.pvRate = QLineEdit(self)
        self.pvRate.setGeometry(250, 450, 200, 50) 

        self.pvPeriods = QLineEdit(self)
        self.pvPeriods.setGeometry(250, 550, 200, 50)

    # Calculate Button
        self.calculateButton = QPushButton("Calculate", self)
        self.calculateButton.setFont(QFont('Arial', 11))
        self.calculateButton.setStyleSheet("background-color : darkCyan")
        self.calculateButton.setGeometry(475, 350, 180, 75)
        self.calculateButton.clicked.connect(self.calcPresentVal)

    # Clear Button
        self.clearButton = QPushButton("Clear", self)
        self.clearButton.setFont(QFont('Arial', 11))
        self.clearButton.setStyleSheet("background-color : red")
        self.clearButton.setGeometry(475, 525, 180, 75)
        self.clearButton.clicked.connect(self.clearPresentVal)
        
        vbox = QVBoxLayout()
        self.setLayout(vbox)

# Calculates Present Value
    def calcPresentVal(self):
        pvFV = self.pvFutVal.text()
        pvP = self.pvPeriods.text()
        pvR = self.pvRate.text()

        presentValue = Finance.calcPresentValue(pvFV, pvP, pvR)
        self.labelInterestResult.setText(str(presentValue))

# Clears all values of inputs
    def clearPresentVal(self):
        self.pvFutVal.setText("")
        self.pvPeriods.setText("")
        self.pvRate.setText("")
        self.labelInterestResult.setText("")
class FutureValueTab(QWidget):
    def __init__(self):
        super().__init__()
    
    # Result Labels
        self.labelInterest = QLabel("Future Value: $ ", self)
        self.labelInterest.setGeometry(50, 650, 325, 50)
        self.labelInterest.setStyleSheet("border: 0px solid black;")
        self.labelInterest.setFont(QFont('Arial', 10))

        self.labelInterestResult = QLabel("", self)
        self.labelInterestResult.setGeometry(300, 650, 300, 50)
        self.labelInterestResult.setStyleSheet("border: 1px solid black;")
        self.labelInterestResult.setFont(QFont('Arial', 10))

    # Add Labels for values
        self.label_PV = QLabel("Present Value: $ ", self)
        self.label_PV.setGeometry(50, 350, 325, 50)
        self.label_PV.setStyleSheet("border: 0px solid black;")

        self.label_Rate = QLabel("Rate (%):  ", self)
        self.label_Rate.setGeometry(50, 450, 325, 50)
        self.label_Rate.setStyleSheet("border: 0px solid black;")

        self.label_Per = QLabel("Periods: ", self)
        self.label_Per.setGeometry(50, 550, 325, 50)
        self.label_Per.setStyleSheet("border: 0px solid black;")

    # Add Text Boxes for values
        self.fvPresVal = QLineEdit("",self)
        self.fvPresVal.setGeometry(260, 350, 200, 50)

        self.fvRate = QLineEdit(self)
        self.fvRate.setGeometry(260, 450, 200, 50)    

        self.fvPeriods = QLineEdit(self)
        self.fvPeriods.setGeometry(260, 550, 200, 50)

        # Calculate Button
        self.calculateButton = QPushButton("Calculate", self)
        self.calculateButton.setFont(QFont('Arial', 11))
        self.calculateButton.setStyleSheet("background-color : darkCyan")
        self.calculateButton.setGeometry(485, 350, 180, 75)
        self.calculateButton.clicked.connect(self.calcFutureVal)

        # Clear Button
        self.clearButton = QPushButton("Clear", self)
        self.clearButton.setFont(QFont('Arial', 11))
        self.clearButton.setStyleSheet("background-color : red")
        self.clearButton.setGeometry(485, 525, 180, 75)
        self.clearButton.clicked.connect(self.clearFutureVal)
        
        vbox = QVBoxLayout()
        self.setLayout(vbox)

# Calculates Future Value
    def calcFutureVal(self):
        fvPV = self.fvPresVal.text()
        fvP = self.fvPeriods.text()
        fvR = self.fvRate.text()

        presentValue = Finance.calcFutureValue(fvPV, fvP, fvR)
        self.labelInterestResult.setText(str(presentValue))

# Clears all values of inputs
    def clearFutureVal(self):
        self.fvPresVal.setText("")
        self.fvPeriods.setText("")
        self.fvRate.setText("")
        self.labelInterestResult.setText("")
