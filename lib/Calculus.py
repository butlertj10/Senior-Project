#from sympy import derivative 
from sympy import Derivative, Symbol, integrate, limit

class Calculus():
    def __init__(self):
        super().__init__()

# Add variable multiplication using symbol - Note: 2xy^2 is a vaild entery; keep track of the non-symbol variable 
#   Allow for entering of ln, log, e, sqrt, etc - look into simplifying with variables
#   ***Add/look into infinity for limit function - Check Panda docs

    '''
        calcDerivative
            This function requires a symbol and equation.
            When passed in, covert the symbol to a string
            and set it as a symbol. This symbol will be 
            the variable the given equation is derived from.
            Formatting is done before and after calculations.

        @param symbol, equation
        @return answer (result of derivation with given equation and symbol)

    '''
    def calcDerivative(symbol, equation):

        try:  
            symD = str(symbol)
            x = Symbol(symD)
            
            # remove '^' and replace with '**'
            equation = Calculus.formatForCalc(equation)

            # Calculating Derivative
            derivative_f = Derivative(equation, x)
            answer = ("{}".format(derivative_f.doit()))
            
            # remove '**' and replace with '^'
            answer = Calculus.formatForDisp(answer)
            
            return answer
        
        except ValueError:
            answer = "Error - Verify the given equation"
            return answer

    '''
        calcIntegral
            This function requires a symbol and equation.
            An upper and lowerbound are optional, if they
            are entered, the function computes with them,
            otherwise it will calculate without bounds.
            When values are passed in, covert the symbol 
            to a string and set it as a symbol. This symbol 
            will be the variable the given equation is 
            integrated from. Formatting is done before 
            and after calculations.

        @param equation, symbol, lowerbound, upperbound
        @return answer (result of integration with given equation and symbols)

    '''
    def calcIntegral(equation, symbol, lowerbound, upperbound):
        
        try:  
            symI = str(symbol)
            x = Symbol(symI)

            if(lowerbound == '' and upperbound == ''): # WITHOUT BOUNDS
                # remove '^' and replace with '**'
                equation = Calculus.formatForCalc(equation)

                # Calculating Integral
                integral_f = integrate(equation, x)
                answer = ("{}".format(integral_f.doit()))
                
                # remove '**' and replace with '^'
                answer = Calculus.formatForDisp(answer)
                
                return answer
            elif((lowerbound == '' and upperbound != '') or (lowerbound != '' and upperbound == '')):
                answer = "Error - Must enter both bounds"
                return answer
            else:
                a = str(lowerbound)
                b = str(upperbound)

                # remove '^' and replace with '**'
                equation = Calculus.formatForCalc(equation)

                # Calculating Integral
                integral_f = integrate(equation, (x, a, b))
                answer = ("{}".format(integral_f.doit()))
                
                # remove '**' and replace with '^'
                answer = Calculus.formatForDisp(answer)
                
                return answer
        
        except ValueError:
            answer = "Error - Verify the given equation"
            return answer
    
    '''
        calcLimit
            This function requires an equation as well as
            a 'x' and 'a'. As 'x' approaches 'a' this 
            function will calculate the limit of the given
            equation. Formatting is done before and after 
            calculations. Checks are done to verify that 
            both 'x' and 'a' are entered, not just one.

        @param equation, x, a
        @return answer (result of the limit with given equation and symbols)

    ''' 
    def calcLimit(equation, x, a):
         
        try:  
            xStr = str(x)
            xLim = Symbol(xStr)

            if((x == '' and a != '') or (x != '' and a == '')):
                answer = "Error - Must enter both 'x' and 'a'"
                return answer
            else:
                a = str(a)

                # remove '^' and replace with '**'
                equation = Calculus.formatForCalc(equation)

                # Calculating Integral
                limit_f = limit(equation, xLim, a)
                answer = ("{}".format(limit_f.doit()))
                
                # remove '**' and replace with '^'
                answer = Calculus.formatForDisp(answer)
                
                return answer # Compute total answer with panda
        
        except ValueError:
            answer = "Error - Verify the given equation"
            return answer
       
    '''
        formatForCalc
            This function removes the '^' character and
            replaces it with '**' for calculations. If 
            '^' does not appear, return the original 
            equation.
        
        @param equation (string)
        @return newEq (string of formatted equation)

    '''
    def formatForCalc(equation):
        
        equation = str(equation)
        
        if('^' in equation):
            equation = equation.replace('^', '**')

        return equation

    '''
        formatForDisp
            This function removes the '**' character and
            replaces it with '^' for displaying to screen. 
            If '**' does not appear, return the original 
            equation.
        
        @param equation (string)
        @return newEq (string of formatted equation)

    '''
    def formatForDisp(equation):
        
        equation = str(equation)
        
        if('**' in equation):
            equation = equation.replace('**', '^')

        if('sqrt' in equation):
            equation = equation.replace('sqrt', '√')

        return equation
