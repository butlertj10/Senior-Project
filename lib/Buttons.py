# from PyQt5.QtWidgets import *
# from PyQt5 import QtCore, QtGui
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
# from PyQt5 import QtCore, QtWidgets

# class Buttons():

#     def numberPad(self):
#         #super().__init__()

#     # creating a label
#         self.label = QLabel(self)
  
#         # setting geometry to the label
#         self.label.setGeometry(960, 440, 559, 70)
  
#         # creating label multi line
#         self.label.setWordWrap(True)
  
#         # setting style sheet to the label
#         self.label.setStyleSheet("QLabel"
#                                  "{"
#                                  "border : 4px solid black;"
#                                  "background : white;"
#                                  "}")
  
#         # setting alignment to the label
#         self.label.setAlignment(Qt.AlignRight)
  
#         # setting font
#         self.label.setFont(QFont('Arial', 15))
    
#     # adding number button to the screen
#         # creating a push button
#         push1 = QPushButton("1", self)
#         push1.setGeometry(960, 755, 80, 80)
  
#         # creating a push button
#         push2 = QPushButton("2", self)
#         push2.setGeometry(1040, 755, 80, 80)
  
#         # creating a push button
#         push3 = QPushButton("3", self)
#         push3.setGeometry(1120, 755, 80, 80)
  
#         # creating a push button
#         push4 = QPushButton("4", self)
#         push4.setGeometry(960, 675, 80, 80)
  
#         # creating a push button
#         push5 = QPushButton("5", self)
#         push5.setGeometry(1040, 675, 80, 80)
  
#         # creating a push button
#         push6 = QPushButton("6", self)
#         push6.setGeometry(1120, 675, 80, 80)
  
#         # creating a push button
#         push7 = QPushButton("7", self)
#         push7.setGeometry(960, 595, 80, 80)
  
#         # creating a push button
#         push8 = QPushButton("8", self)
#         push8.setGeometry(1040, 595, 80, 80)
  
#         # creating a push button
#         push9 = QPushButton("9", self)
#         push9.setGeometry(1120, 595, 80, 80)
  
#         # creating a push button
#         push0 = QPushButton("0", self)
#         push0.setGeometry(960, 835, 80, 80)
  
#     # adding operator push button
  
#     #### ADD FUNTIONALITY TO THE FOLLOWING ####

#         # Any number raised to an exponent
#         pushExpo = QPushButton("^", self)
#         pushExpo.setGeometry(1280, 595, 80, 80)

#         # Any number squared
#         pushSqr = QPushButton("x²", self)
#         pushSqr.setGeometry(1360, 595, 80, 80)

#         # Squareroot
#         pushSqrt = QPushButton("√", self)
#         pushSqrt.setGeometry(1440, 595, 80, 80)

#         # Natural Log
#         pushLn = QPushButton("ln", self)
#         pushLn.setGeometry(1280, 675, 80, 80)

#         # Log **find out if base change is possible**
#         pushLog = QPushButton("log", self)
#         pushLog.setGeometry(1360, 675, 80, 80)

#         # e^
#         push_e = QPushButton("e^", self)
#         push_e.setGeometry(1440, 675, 80, 80)

#         # 10^
#         push10 = QPushButton("10^", self)
#         push10.setGeometry(1280, 755, 80, 80)

#         # pi
#         pushPi = QPushButton("π", self)
#         pushPi.setGeometry(1360, 755, 80, 80)

#         # approx
#         pushApprox = QPushButton("≈", self)
#         pushApprox.setGeometry(1440, 755, 80, 80)

#         # (-)
#         pushNeg = QPushButton("(-)", self)
#         pushNeg.setGeometry(1120, 835, 80, 80)

#         # (
#         push_LHS_paren = QPushButton("(", self)
#         push_LHS_paren.setGeometry(1280, 835, 80, 80)

#         # )
#         push_RHS_paren = QPushButton(")", self)
#         push_RHS_paren.setGeometry(1360, 835, 80, 80)

#         # ANS -> copy previous result
#         pushANS = QPushButton("ANS", self)
#         pushANS.setGeometry(1440, 835, 80, 80)
# ##########################################################################

#         # push button for: +
#         pushPlus = QPushButton("+", self)
#         pushPlus.setGeometry(1200, 755, 80, 80)
  
#         # push button for: -
#         pushMinus = QPushButton("-", self)
#         pushMinus.setGeometry(1200, 675, 80, 80)
  
#         # push button for: *
#         pushMul = QPushButton("*", self)
#         pushMul.setGeometry(1200, 595, 80, 80)
  
#         # push button for: / 
#         pushDiv = QPushButton("/", self)
#         pushDiv.setGeometry(1200, 835, 80, 80)
  
#         # push button for: .
#         pushPoint = QPushButton(".", self)
#         pushPoint.setGeometry(1040, 835, 80, 80)
  
#         # clear button
#         pushClear = QPushButton("Clear", self)
#         pushClear.setGeometry(960, 515, 185, 80)
  
#         # del one character button
#         pushDel = QPushButton("Delete", self)
#         pushDel.setGeometry(int(1147.5), 515, 185, 80)

#         pushEqual = QPushButton("Enter", self)
#         pushEqual.setGeometry(int(1334.5), 515, 185, 80)
  
#         # adding action to each of the button
#         pushMinus.clicked.connect(self.actionMinus)
#         pushEqual.clicked.connect(self.actionEqual)
#         push0.clicked.connect(self.action0)
#         push1.clicked.connect(self.action1)
#         push2.clicked.connect(self.action2)
#         push3.clicked.connect(self.action3)
#         push4.clicked.connect(self.action4)
#         push5.clicked.connect(self.action5)
#         push6.clicked.connect(self.action6)
#         push7.clicked.connect(self.action7)
#         push8.clicked.connect(self.action8)
#         push9.clicked.connect(self.action9)
#         pushDiv.clicked.connect(self.actionDiv)
#         pushMul.clicked.connect(self.actionMul)
#         pushPlus.clicked.connect(self.actionPlus)
#         pushPoint.clicked.connect(self.actionDecimal)
#         pushClear.clicked.connect(self.actionClear)
#         pushDel.clicked.connect(self.actionDel)
#         pushExpo.clicked.connect(self.actionExpo)
#         pushSqr.clicked.connect(self.actionSqr)
#         pushSqrt.clicked.connect(self.actionSqrt)
#         pushLn.clicked.connect(self.actionLn)
#         pushLog.clicked.connect(self.actionLog)
#         push_e.clicked.connect(self.action_e)
#         push10.clicked.connect(self.action10)
#         pushPi.clicked.connect(self.actionPi)
#         pushApprox.clicked.connect(self.actionApprox)
#         pushNeg.clicked.connect(self.actionNeg)
#         push_LHS_paren.clicked.connect(self.action_LHS_paren)
#         push_RHS_paren.clicked.connect(self.action_RHS_paren)
#         pushANS.clicked.connect(self.actionANS)

#     def actionPlus(self):
#         # append +
#         text = self.label.text()
#         self.label.setText(text + " + ")
  
#     def actionMinus(self):
#         # append -
#         text = self.label.text()
#         self.label.setText(text + " - ")
  
#     def actionDiv(self):
#         # append /
#         text = self.label.text()
#         self.label.setText(text + " / ")
  
#     def actionMul(self):
#         # append *
#         text = self.label.text()
#         self.label.setText(text + " * ")
  
#     def actionDecimal(self):
#         # append .
#         text = self.label.text()
#         self.label.setText(text + ".")
  
#     def action0(self):
#         # append 0
#         text = self.label.text()
#         self.label.setText(text + "0")
  
#     def action1(self):
#         # append 1
#         text = self.label.text()
#         self.label.setText(text + "1")
  
#     def action2(self):
#         # append 2
#         text = self.label.text()
#         self.label.setText(text + "2")
  
#     def action3(self):
#         # append 3
#         text = self.label.text()
#         self.label.setText(text + "3")
  
#     def action4(self):
#         # append 4
#         text = self.label.text()
#         self.label.setText(text + "4")
  
#     def action5(self):
#         # append 5
#         text = self.label.text()
#         self.label.setText(text + "5")
  
#     def action6(self):
#         # append 6
#         text = self.label.text()
#         self.label.setText(text + "6")
  
#     def action7(self):
#         # append 7
#         text = self.label.text()
#         self.label.setText(text + "7")
  
#     def action8(self):
#         # append 8
#         text = self.label.text()
#         self.label.setText(text + "8")
  
#     def action9(self):
#         # append 9
#         text = self.label.text()
#         self.label.setText(text + "9")
  
#     def actionClear(self):
#         # Clear input text
#         self.label.setText("")
  
#     def actionDel(self):
#         # Delete a single digit
#         text = self.label.text()
#         #print(text[:len(text)-1]) # prints to terminal
#         self.label.setText(text[:len(text)-1])

# ######### Added functionality, terminal based only #########
#     def actionExpo(self):
#         text = self.label.text()
#         self.label.setText(text + "^")

#     def actionSqr(self):
#         text = self.label.text()
#         self.label.setText(text + "\u00b2") 
  
#     def actionSqrt(self):
#         text = self.label.text()
#         self.label.setText(text + "√(")

#     def actionLn(self):
#         text = self.label.text()
#         self.label.setText(text + "ln(")

#     def actionLog(self):
#         text = self.label.text()
#         self.label.setText(text + 'log(')

#     def action_e(self):
#         text = self.label.text()
#         self.label.setText(text + "e^")

#     def action10(self):
#         text = self.label.text()
#         self.label.setText(text + "10^")
# ###############################################################

#     def actionPi(self):
#         text = self.label.text()
#         self.label.setText(text + "π")
    
#     def actionNeg(self):
#         text = self.label.text()
#         self.label.setText(" -" + text)

#     def action_LHS_paren(self):
#         text = self.label.text()
#         self.label.setText(text + "(")  

#     def action_RHS_paren(self):
#         text = self.label.text()
#         self.label.setText(text + ")")        
        
#     def actionANS(self):
#         text = self.label.text()
#         self.label.setText(text + "ANS") 

#     # Should not display on screen, should act similar to enter button, add to that row
#     def actionApprox(self):
#         text = self.label.text()
#         self.label.setText(text + "≈") 