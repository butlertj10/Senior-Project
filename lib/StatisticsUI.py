from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5 import QtCore
from Statistics import StatsCalc

class StatisticsTab(QWidget):
    def __init__(self):
        super().__init__()
    
    # Result Labels  !!! Use for import? !!!
        # self.labelStats = QLabel("Expanded/Simplified polynomial is :", self)
        # self.labelStats.setGeometry(25, 360, 310, 50)
        # self.labelStats.setStyleSheet("border: 0px solid black;")
        # self.labelStats.setFont(QFont('Arial', 14))
        # self.labelStatsResult = QLabel("", self) # Exp/Simp Result
        # self.labelStatsResult.setGeometry(335, 360, 450, 50)
        # self.labelStatsResult.setStyleSheet("border: 2px solid black;")
        # self.labelStatsResult.setFont(QFont('Arial', 18))
        self.labelStatList = QLabel("Set Statistics:", self)
        self.labelStatList.setGeometry(720, 135, 205, 50)
        self.labelStatList.setStyleSheet("border: 0px solid black;")
        self.labelStatList.setFont(QFont('Arial', 16))
        self.statList = QLabel(self)
        self.statList.setWordWrap(True)
        self.statListVisual = QLabel(self)
        self.statListVisual.setGeometry(750, 175, 410, 410)
        self.statListVisual.setStyleSheet("border: 2px solid black;")
        self.statList.setGeometry(750, 175, 410, 410)
        self.statList.setStyleSheet("border: 3px solid cyan;")
        self.statList.setFont(QFont('Arial', 16))
        #self.statList.setAlignment(QtCore.Qt.AlignCenter)

    # Add Text Boxes for values
        self.labelSet = QLabel("Number Set:", self)
        self.labelSet.setGeometry(115, 240, 205, 50)
        self.labelSet.setStyleSheet("border: 0px solid black;")
        self.labelSet.setFont(QFont('Arial', 14))
        self.numberSet = QLineEdit("", self)
        self.numberSet.setGeometry(250, 240, 450, 50)
        self.numberSet.setPlaceholderText("Number Set to process")
        self.numberSet.setAlignment(QtCore.Qt.AlignCenter)
        self.numberSet.setStyleSheet("border: 2px solid black;")
        self.numberSet.setFont(QFont('Arial', 18))

        # Calculate Expand Button
        self.calculateButton = QPushButton("Calculate", self)
        self.calculateButton.setFont(QFont('Arial', 11))
        self.calculateButton.setStyleSheet("background-color : darkCyan")
        self.calculateButton.setGeometry(175, 500, 180, 75)
        self.calculateButton.clicked.connect(self.calcStats)

        # Clear Button
        self.clearButton = QPushButton("Clear", self)
        self.clearButton.setFont(QFont('Arial', 11))
        self.clearButton.setStyleSheet("background-color : red")
        self.clearButton.setGeometry(455, 500, 180, 75)
        self.clearButton.clicked.connect(self.clearStats)
        
        vbox = QVBoxLayout()
        self.show()
        self.setLayout(vbox)

    # Calculates The expansion
    def calcStats(self):
        numSet = self.numberSet.text()

        resultStats = StatsCalc.mainStats(numSet)
        self.statList.setText(str(resultStats))

    # Clears all values of inputs
    def clearStats(self):
        self.numberSet.setText("")
        self.statList.setText("")