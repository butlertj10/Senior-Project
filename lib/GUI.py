from asyncio.windows_events import NULL
from PyQt5 import Qt, QtCore
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QWidget, QLabel, QDialog, QPushButton, QVBoxLayout, QTabWidget, QApplication
from PyQt5.QtGui import QFont
from Operations import Math
from pandas import *
from Calculus import Calculus
import TriangleUI, CircleUI, QuadUI, FinanceUI, AlgebraUI, CalculusUI, StatisticsUI
import sys
import Operations
from Operations import Checks

class Tab(QDialog):
    def __init__(self):
        super().__init__()

        vbox = QVBoxLayout()
        self.tabWidget = QTabWidget()
        
        # setting title
        self.setWindowTitle("Advanced Calculator")

        # setting geometry
        self.setGeometry(0, 0, 2000, 1100)

        basicCalc = TabBasicCalc()
        algCalc = TabAlgCalc()
        geoCalc = TabGeoCalc()
        calcCalc = TabCalcCalc()
        statsCalc = TabStatsCalc()
        finCalc = TabFinCalc()
        graphCalc = TabGraphCalc()
        exportTab = TabExport()
        settingsTab = TabSettings()

        self.tabWidget.addTab(basicCalc, "Basic Calculator")
        self.tabWidget.addTab(algCalc, "Alegbra")
        self.tabWidget.addTab(geoCalc, "Geometry")
        self.tabWidget.addTab(calcCalc, "Calculus")
        self.tabWidget.addTab(statsCalc, "Statistics")
        self.tabWidget.addTab(finCalc, "Finance")
        self.tabWidget.addTab(graphCalc, "Graph")
        self.tabWidget.addTab(exportTab, "Export")
        self.tabWidget.addTab(settingsTab, "Settings")

        vbox.addWidget(self.tabWidget)
        self.setLayout(vbox)

        # connect slots to signals
       # basicCalc.pushButton.clicked.connect(self.next_tab)
       # algCalc.pushButton_2.clicked.connect(self.prev_tab)

    def next_tab(self):
        cur_index = self.tabWidget.currentIndex()
        if cur_index < len(self.tabWidget)-1:
            self.tabWidget.setCurrentIndex(cur_index+1)

    def prev_tab(self):
        cur_index = self.tabWidget.currentIndex()
        if cur_index > 0:
            self.tabWidget.setCurrentIndex(cur_index-1)
class TabBasicCalc(QWidget):

    ans = ""
    
    def __init__(self):
        super().__init__()
        # self.pushButton = QPushButton("Go to next")

        vbox = QVBoxLayout()
       # vbox.addWidget(self.pushButton)
        self.setLayout(vbox)
        labelFont = QFont('Arial', 11)
        
        # creating an input label
        self.label = QLabel(self)
        self.label.setGeometry(960, 440, 559, 70)
        self.label.setWordWrap(True)
        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 4px solid black;"
                                 "background : white;"
                                 "}")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('Arial', 15))

        # creating a history label2
        self.label2 = QLabel(self)
        self.label2.setGeometry(100, 100, 600, 100)
        self.label2.setWordWrap(True)
        self.label2.setStyleSheet("QLabel"
                                 "{"
                                 "border : 4px solid black;"
                                 "background : white;"
                                 "}")
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setFont(labelFont)

        
    
    # adding number button to the screen
        # creating a push button
        push1 = QPushButton("1", self)
        push1.setFont(labelFont)
        push1.setStyleSheet("background-color : lightgrey")
        push1.setGeometry(960, 755, 80, 80)
  
        # creating a push button
        push2 = QPushButton("2", self)
        push2.setFont(labelFont)
        push2.setStyleSheet("background-color : lightgrey")
        push2.setGeometry(1040, 755, 80, 80)
  
        # creating a push button
        push3 = QPushButton("3", self)
        push3.setFont(labelFont)
        push3.setStyleSheet("background-color : lightgrey")
        push3.setGeometry(1120, 755, 80, 80)
  
        # creating a push button
        push4 = QPushButton("4", self)
        push4.setFont(labelFont)
        push4.setStyleSheet("background-color : lightgrey")
        push4.setGeometry(960, 675, 80, 80)
  
        # creating a push button
        push5 = QPushButton("5", self)
        push5.setFont(labelFont)
        push5.setStyleSheet("background-color : lightgrey")
        push5.setGeometry(1040, 675, 80, 80)
  
        # creating a push button
        push6 = QPushButton("6", self)
        push6.setFont(labelFont)
        push6.setStyleSheet("background-color : lightgrey")
        push6.setGeometry(1120, 675, 80, 80)
  
        # creating a push button
        push7 = QPushButton("7", self)
        push7.setFont(labelFont)
        push7.setStyleSheet("background-color : lightgrey")
        push7.setGeometry(960, 595, 80, 80)
  
        # creating a push button
        push8 = QPushButton("8", self)
        push8.setFont(labelFont)
        push8.setStyleSheet("background-color : lightgrey")
        push8.setGeometry(1040, 595, 80, 80)
  
        # creating a push button
        push9 = QPushButton("9", self)
        push9.setFont(labelFont)
        push9.setStyleSheet("background-color : lightgrey")
        push9.setGeometry(1120, 595, 80, 80)
  
        # creating a push button
        push0 = QPushButton("0", self)
        push0.setFont(labelFont)
        push0.setStyleSheet("background-color : lightgrey")
        push0.setGeometry(960, 835, 80, 80)
  
    # adding operator push button
  
    #### ADD FUNTIONALITY TO THE FOLLOWING ####

        # Any number raised to an exponent
        pushExpo = QPushButton("^", self)
        pushExpo.setFont(labelFont)
        pushExpo.setGeometry(1280, 595, 80, 80)

        # Any number squared
        pushSqr = QPushButton("x²", self)
        pushSqr.setFont(labelFont)
        pushSqr.setGeometry(1360, 595, 80, 80)

        # Squareroot
        pushSqrt = QPushButton("√", self)
        pushSqrt.setFont(labelFont)
        pushSqrt.setGeometry(1440, 595, 80, 80)

        # Natural Log
        pushLn = QPushButton("ln", self)
        pushLn.setFont(labelFont)
        pushLn.setGeometry(1280, 675, 80, 80)

        # Log **find out if base change is possible**
        pushLog = QPushButton("log", self)
        pushLog.setFont(labelFont)
        pushLog.setGeometry(1360, 675, 80, 80)

        # e^
        push_e = QPushButton("e^", self)
        push_e.setFont(labelFont)
        push_e.setGeometry(1440, 675, 80, 80)

        # 10^
        push10 = QPushButton("10^", self)
        push10.setFont(labelFont)
        push10.setGeometry(1280, 755, 80, 80)

        # pi
        pushPi = QPushButton("π", self)
        pushPi.setFont(labelFont)
        pushPi.setGeometry(1360, 755, 80, 80)

        # approx
        pushComma = QPushButton(",", self)
        pushComma.setFont(labelFont)
        pushComma.setGeometry(1440, 755, 80, 80)

        # ]
        pushCloseBrack = QPushButton("]", self)
        pushCloseBrack.setFont(labelFont)
        pushCloseBrack.setGeometry(1120, 835, 80, 80)

        # (
        push_LHS_paren = QPushButton("(", self)
        push_LHS_paren.setFont(labelFont)
        push_LHS_paren.setGeometry(1280, 835, 80, 80)

        # )
        push_RHS_paren = QPushButton(")", self)
        push_RHS_paren.setFont(labelFont)
        push_RHS_paren.setGeometry(1360, 835, 80, 80)

        # ANS -> copy previous result
        pushANS = QPushButton("ANS", self)
        pushANS.setFont(labelFont)
        pushANS.setGeometry(1440, 835, 80, 80)
##########################################################################

        # push button for: +
        pushPlus = QPushButton("+", self)
        pushPlus.setFont(labelFont)
        pushPlus.setGeometry(1200, 755, 80, 80)
  
        # push button for: -
        pushMinus = QPushButton("-", self)
        pushMinus.setFont(labelFont)
        pushMinus.setGeometry(1200, 675, 80, 80)
  
        # push button for: *
        pushMul = QPushButton("*", self)
        pushMul.setFont(labelFont)
        pushMul.setGeometry(1200, 595, 80, 80)
  
        # push button for: / 
        pushDiv = QPushButton("/", self)
        pushDiv.setFont(labelFont)
        pushDiv.setGeometry(1200, 835, 80, 80)
  
        # push button for: .
        pushPoint = QPushButton(".", self)
        pushPoint.setFont(labelFont)
        pushPoint.setGeometry(1040, 835, 80, 80)
  
        # clear button
        pushClear = QPushButton("Clear", self)
        pushClear.setFont(labelFont)
        pushClear.setStyleSheet("background-color : orange")
        pushClear.setGeometry(960, 515, 185, 80)
  
        # del one character button
        pushDel = QPushButton("Delete", self)
        pushDel.setFont(labelFont)
        pushDel.setStyleSheet("background-color : red")
        pushDel.setGeometry(int(1147.5), 515, 185, 80)

        pushEqual = QPushButton("Enter", self)
        pushEqual.setFont(labelFont)
        pushEqual.setStyleSheet("background-color : cyan")
        pushEqual.setGeometry(int(1334.5), 515, 185, 80)
  
        # adding action to each of the button
        pushMinus.clicked.connect(self.actionMinus)
        pushEqual.clicked.connect(self.actionEqual)
        push0.clicked.connect(self.action0)
        push1.clicked.connect(self.action1)
        push2.clicked.connect(self.action2)
        push3.clicked.connect(self.action3)
        push4.clicked.connect(self.action4)
        push5.clicked.connect(self.action5)
        push6.clicked.connect(self.action6)
        push7.clicked.connect(self.action7)
        push8.clicked.connect(self.action8)
        push9.clicked.connect(self.action9)
        pushDiv.clicked.connect(self.actionDiv)
        pushMul.clicked.connect(self.actionMul)
        pushPlus.clicked.connect(self.actionPlus)
        pushPoint.clicked.connect(self.actionDecimal)
        pushClear.clicked.connect(self.actionClear)
        pushDel.clicked.connect(self.actionDel)
        pushExpo.clicked.connect(self.actionExpo)
        pushSqr.clicked.connect(self.actionSqr)
        pushSqrt.clicked.connect(self.actionSqrt)
        pushLn.clicked.connect(self.actionLn)
        pushLog.clicked.connect(self.actionLog)
        push_e.clicked.connect(self.action_e)
        push10.clicked.connect(self.action10)
        pushPi.clicked.connect(self.actionPi)
        pushComma.clicked.connect(self.actionComma)
        pushCloseBrack.clicked.connect(self.actionCloseBracket)
        push_LHS_paren.clicked.connect(self.action_LHS_paren)
        push_RHS_paren.clicked.connect(self.action_RHS_paren)
        pushANS.clicked.connect(self.actionANS)


    # To Help Create Calculations: https://github.com/neilbalch/SimplePythonTutorial/blob/master/Advanced%20Calculator%20Tutorial.md
    #                              https://codereview.stackexchange.com/questions/86389/recursive-math-expression-eval

    # P   Parentheses, then
    # E   Exponents, then
    # MD  Multiplication and division, left to right, then
    # AS  Addition and subtraction, left to right


    def actionEqual(self):
  
        # get the label text
        equation = self.label.text()
        self.ans = Math.getNewResult(equation)
        print("PREVIOUS RESULT: ", self.ans)
        if('Error' in self.ans):
            self.label2.setText("Previous Result: \n" + self.ans)
            
        else:
            self.label2.setText("Previous Result: \n" + equation + " = " + self.ans)
            self.label.setText(self.ans)
        
        #return ans
        

  
    def actionPlus(self):
        # append +
        text = self.label.text()
        self.label.setText(text + "+")
  
    def actionMinus(self):
        # append -
        text = self.label.text()
        self.label.setText(text + "-")
  
    def actionDiv(self):
        # append /
        text = self.label.text()
        self.label.setText(text + "/")
  
    def actionMul(self):
        # append *
        text = self.label.text()
        self.label.setText(text + "*")
  
    def actionDecimal(self):
        # append .
        text = self.label.text()
        self.label.setText(text + ".")
  
    def action0(self):
        # append 0
        text = self.label.text()
        self.label.setText(text + "0")
  
    def action1(self):
        # append 1
        text = self.label.text()
        self.label.setText(text + "1")
  
    def action2(self):
        # append 2
        text = self.label.text()
        self.label.setText(text + "2")
  
    def action3(self):
        # append 3
        text = self.label.text()
        self.label.setText(text + "3")
  
    def action4(self):
        # append 4
        text = self.label.text()
        self.label.setText(text + "4")
  
    def action5(self):
        # append 5
        text = self.label.text()
        self.label.setText(text + "5")
  
    def action6(self):
        # append 6
        text = self.label.text()
        self.label.setText(text + "6")
  
    def action7(self):
        # append 7
        text = self.label.text()
        self.label.setText(text + "7")
  
    def action8(self):
        # append 8
        text = self.label.text()
        self.label.setText(text + "8")
  
    def action9(self):
        # append 9
        text = self.label.text()
        self.label.setText(text + "9")
  
    def actionClear(self):
        # Clear input text
        self.label.setText("")
  
    def actionDel(self):
        # Delete a single digit
        text = self.label.text()
        #print(text[:len(text)-1]) # prints to terminal
        self.label.setText(text[:len(text)-1])

    def actionExpo(self):
        text = self.label.text()
        self.label.setText(text + "^")

    def actionSqr(self):
        text = self.label.text()
        self.label.setText(text + "\u00b2") 
  
    def actionSqrt(self):
        text = self.label.text()
        self.label.setText(text + "√(")

    def actionLn(self):
        text = self.label.text()
        self.label.setText(text + "ln[")

    def actionLog(self):
        text = self.label.text()
        self.label.setText(text + "log[")

    def action_e(self):
        text = self.label.text()
        self.label.setText(text + "e^(")

    def action10(self):
        text = self.label.text()
        self.label.setText(text + "10^")

    def actionPi(self):
        text = self.label.text()
        self.label.setText(text + "π")
    
    def actionCloseBracket(self):
        text = self.label.text()
        self.label.setText(text + "]")

    def action_LHS_paren(self):
        text = self.label.text()
        self.label.setText(text + "(")  

    def action_RHS_paren(self):
        text = self.label.text()
        self.label.setText(text + ")")        
        
    def actionANS(self):
        print("ANS: ", self.ans)
        if self.ans != "":
            text = self.label.text()
            self.label.setText(text + "(" + self.ans + ")") 

    # Should not display on screen, should act similar to enter button, add to that row
    def actionComma(self):
        text = self.label.text()
        self.label.setText(text + ",")  

    # function to convert to subscript - from G4G
    def get_sub(x):
        normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
        sub_s = "ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
        res = x.maketrans(''.join(normal), ''.join(sub_s))
        return x.translate(res)
    # display subscript
    # print('H{}SO{}'.format(get_sub('2'),get_sub('4'))) #H₂SO₄
    
    # function to convert to superscript - from G4G
    def get_super(x):
        normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
        super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
        res = x.maketrans(''.join(normal), ''.join(super_s))
        return x.translate(res)
    # display superscipt
    # print(get_super('GeeksforGeeks')) #ᴳᵉᵉᵏˢᶠᵒʳᴳᵉᵉᵏˢ

# Multivariate Solver: https://www.delftstack.com/howto/python/python-equation-solver/
class TabAlgCalc(QWidget):
    def __init__(self):
        super().__init__()
        
        self.algebraTab = QTabWidget()
        vbox = QVBoxLayout()

        PolyRootsTab = AlgebraUI.PolyRootsTab()
        FactorTab = AlgebraUI.FactorTab()
        InequalityTab = AlgebraUI.InequalityTab()

        self.algebraTab.addTab(PolyRootsTab, "Find Polyroots")
        self.algebraTab.addTab(FactorTab, "Factor")
        self.algebraTab.addTab(InequalityTab, "System of Inequalities")

        vbox.addWidget(self.algebraTab)
        self.setLayout(vbox)
class TabGeoCalc(QWidget):
    def __init__(self):
        super().__init__()
       # self.pushButton_2 = QPushButton("Previous")
       # self.pushButton_2 = QPushButton("Next")

        vbox = QVBoxLayout()

        self.setWindowTitle("Label")
        
        # 'Pick a Shape' Label
        self.label1 = QLabel("Pick a Shape:", self)
        self.label1.setGeometry(100, 100, 425, 75)
        self.label1.setStyleSheet("border: 0px solid black;")
        self.label1.setFont(QFont('Arial', 18))

        # Triangle Push Button
        self.pushTriangle = QPushButton("Triangle", self)
        self.pushTriangle.setFont(QFont('Arial', 15))
        self.pushTriangle.setGeometry(375, 200, 350, 100)

        # Circle Push Button
        self.pushCircle = QPushButton("Circle", self)
        self.pushCircle.setFont(QFont('Arial', 15))
        self.pushCircle.setGeometry(375, 350, 350, 100)

        # Quadrilateral Push Button
        self.pushQuad = QPushButton("Quadrilaterals", self)
        self.pushQuad.setFont(QFont('Arial', 15))
        self.pushQuad.setGeometry(375, 500, 350, 100)

        self.setLayout(vbox)

        self.pushTriangle.clicked.connect(self.triWindow)
        self.pushCircle.clicked.connect(self.circWindow)
        self.pushQuad.clicked.connect(self.quadWindow)

    def triWindow(self):
        self.w = TriangleUI.TriangleWindow()
        self.w.show()

    def circWindow(self):
        self.w = CircleUI.CircleWindow()
        self.w.show()

    def quadWindow(self):
        self.w = QuadUI.QuadWindow()
        self.w.show()
class TabCalcCalc(QWidget):
    def __init__(self):
        super().__init__()
        
        self.calcTabs = QTabWidget()
        vbox = QVBoxLayout()

        derivativeTab = CalculusUI.DerivativeTab()
        integralTab = CalculusUI.IntegralTab()
        limitsTab = CalculusUI.LimitTab()

        self.calcTabs.addTab(derivativeTab, "Derivatives")
        self.calcTabs.addTab(integralTab, "Integrals")
        self.calcTabs.addTab(limitsTab, "Limits")

        vbox.addWidget(self.calcTabs)
        self.setLayout(vbox)
class TabStatsCalc(QWidget):
    def __init__(self):
        super().__init__()

        stats = StatisticsUI.StatisticsTab()
        vbox = QVBoxLayout()

        vbox.addWidget(stats)
        self.setLayout(vbox)
class TabFinCalc(QWidget):
    def __init__(self):
        super().__init__()
        
        self.finTabs = QTabWidget()
        vbox = QVBoxLayout()

        siTab = FinanceUI.SimpleInterestTab()
        ciTab = FinanceUI.CompoundInterestTab()
        pvTab = FinanceUI.PresentValueTab()
        fvTab = FinanceUI.FutureValueTab()

        self.finTabs.addTab(siTab, "Simple Interest")
        self.finTabs.addTab(ciTab, "Compound Interest")
        self.finTabs.addTab(pvTab, "Present Value")
        self.finTabs.addTab(fvTab, "Future Value")

        vbox.addWidget(self.finTabs)
        self.setLayout(vbox)
class TabGraphCalc(QWidget):
    def __init__(self):
        super().__init__()
       # self.pushButton_2 = QPushButton("Previous")
       # self.pushButton_2 = QPushButton("Next")

        vbox = QVBoxLayout()
      #  vbox.addWidget(self.pushButton_2)
      #  vbox.addWidget(self.pushButton_2)

        self.setLayout(vbox)
class TabExport(QWidget):
    def __init__(self):
        super().__init__()
       # self.pushButton_2 = QPushButton("Previous")
       # self.pushButton_2 = QPushButton("Next")

        vbox = QVBoxLayout()
      #  vbox.addWidget(self.pushButton_2)
      #  vbox.addWidget(self.pushButton_2)

        self.setLayout(vbox)
class TabSettings(QWidget):
    def __init__(self):
        super().__init__()
       # self.pushButton_2 = QPushButton("Previous")
       # self.pushButton_2 = QPushButton("Next")

        vbox = QVBoxLayout()
      #  vbox.addWidget(self.pushButton_2)
      #  vbox.addWidget(self.pushButton_2)

        self.setLayout(vbox)

def handle_high_resolution_display():
    if hasattr(Qt, 'AA_EnableHighDpiScaling'):
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

if __name__ == "__main__":
    # Enable High DPI display with PyQt5
    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    tabdialog = Tab()    
    #tabdialog.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowType_Mask)
    tabdialog.showMaximized()
    tabdialog.show()
    app.exec()

    #equation = "3+log[10,3+ln[2+ln[10+2e^(2)(5+1)]+2]]+1" #"3+log(5+4*sqrt((2+4*sqrt(4+4)+3)))+1"
    #equation = "3+ln[3+ln[2+2+ln[10+2]+2]]+1"
    #equation = "2e^(2)(5+1)"
    #equation = "3+ln[3+4√(e^(2)(5+1))+2]" #"3+ln[3+4*sqrt(2+2)+2*exp(2)(5+1)]"
    #equation = "ln[100+2+e^(2)(5+1)]"
    # equation = "3+log[10,23+1]+ln[69]*2"
    # print("Equation1: ", equation)
    # ans = Operations.Math.getNewResult(equation)
    # print("E RESULT: ", ans)
