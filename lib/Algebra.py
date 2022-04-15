from sympy import Symbol, expand, simplify, symbols, factor, solve
from Operations import Checks
from Calculus import Calculus

class AlgCalc():
    def __init__(self):
        super().__init__()

    '''
        calcPolyRoots
            This function takes in an equation along with 
                a symbol to find the roots of the given 
                polynomial. If there is an error finding the 
                roots, an error message will be displayed
                to the screen, else the roots will be
                displayed
                
        @param symbol
        @return eqRoots

        *** Check calculations as well as add potential solving for sqrt, e, etc. ***

    '''
    def calcPolyRoots(symbol, equation):
        try:
            symbol = Symbol(str(symbol))
            equation = str(equation)
            print("Equation: ", equation)

            equation = Checks.swapSymbols(equation)
            print("Equation Swap: ", equation)
            
            eqRoots = solve(equation, symbol)
            print("eqRoots: ", eqRoots)

            eqRoots = Calculus.formatForDisp(eqRoots)


            return eqRoots
        
        except:
            eqRoots = "Error: No Roots found"
            return eqRoots

    '''
        calcExpand
            This function takes in an equation and expand
            it from simplest form. If there is an error 
            converting or expanding an error will be 
            displayed, else the expanded function will
            be displayed.
                
        @return eqExpand

        *** Check calculations as well as add potential solving for sqrt, e, etc. ***

    '''
    def calcExpand(equation):
        try:

            equation = str(equation)
            print("Equation: ", equation)

            eqExpand = expand(equation)

            eqExpand = Calculus.formatForDisp(eqExpand)

            return eqExpand
        
        except:
            eqExpand = "Error: Equation cannot be expanded"
            return eqExpand

    '''
        calcSimp
            This function takes in an equation and expand
            it from simplest form. If there is an error 
            converting or expanding an error will be 
            displayed, else the expanded function will
            be displayed.
                
        @return eqExpand

        *** Check calculations as well as add potential solving for sqrt, e, etc. ***

    '''
    def calcSimp(equation):
        try:

            equation = str(equation)
            print("Equation: ", equation)

            eqSimp = simplify(equation)

            eqSimp = Calculus.formatForDisp(eqSimp)

            return eqSimp
        
        except:
            eqSimp = "Error: Equation cannot be expanded"
            return eqSimp

        ### Add symbol multiplication ###
        
        
