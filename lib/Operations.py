from cmath import log
# from dataclasses import replace
# from operator import eq
# from pickle import FALSE
import math
#from tkinter import E
from itertools import compress
from pandas import *

# Link for solving Quadratic Equations: https://www.geeksforgeeks.org/python-program-to-solve-quadratic-equation/
class Math():
    def __init__(self):
        super().__init__()

    def logrithim(base, number):
        
        # if 'e' is entered, change it from a char to the 'number' e 
        if(base == 'e'):
            base = math.e
        else: # Convert the string to a int
            base = int(base)
        
        number = int(number) # convert the number to int
        
        # Default base is e
        if(base == 0):
            result = "Base of 0 is Undefined"
        elif(number == 0):
            result = "Undefinded"
        elif(number < 0):
            result = "Error: Domain Error"
        elif((Checks.isNumber(base) == True)):
            result = log(number, base)
        else:  
            result = "Invaild Base (Not a Number)" #result = log(number, base)

        print("log with base " , base , " of " , number , " is: " , result)
        return result

    def naturalLog(value):
        base = math.e
                
        value = float(value)
        result = math.log(value, base)
        result = str(result)

        return result
    
    def sqRoot(number):
        number = float(number)

        result = math.sqrt(number) 
        result = str(result)

        return result
    
    def pi():
        pi = math.pi
        pi = str(pi)
        return pi

    def getValues(equation):
        
        #opsLeft = True

        while(Checks.functionsCheck(equation) == True):
            if 'ln' in equation:
                equation = Checks.addFuncMulti(equation)
                natLog = equation.find('ln')                    ### *** ISSUE BELOW DUE TO GETTING LAST PAREN *** --- 3ln(3+3)+2ln(1+1) -> 3+3)+2*ln(1+1 ###
                closingLn = equation.find(']')                 ### SECOND ISSUE - ln(x)ln(y) should be -> ln(x)*ln(y)   (look in .addFuncMulti)
                lnEquation = equation[natLog+3:closingLn]
                #print("lnEquation: ", lnEquation)
                
                firstRHS_Bracket = equation.find(']')
                eqLHS = equation[0:natLog]
                eqRHS = equation[firstRHS_Bracket+1:len(equation)]
                equation = equation[natLog:firstRHS_Bracket+1]
                #print("LHS: ", eqLHS)
                #print("RHS: ", eqRHS)
                #print("Equation ln: ", equation)

            # Checks for ')(' then solves the ln equation
                try:
                    if(Checks.parenCheck(lnEquation) == True):
                        lnEquation = Checks.addMulti(lnEquation)        ### Add functionallity for double operations; FOR ALL THE FOLLOWING ### -> might need to move this section
                        ans = eval(lnEquation)
                    else:
                        ans = eval(lnEquation)
                
            
                # Conducts the ln operation with computed parameteres
                    result = Math.naturalLog(ans)
                    #result = Checks.formatFloat(result)
                # print("STR: ", result)
                    equation = ''.join([eqLHS, result, eqRHS])
                # print("Final: ", equation)
                    # print("lnEquation: ", lnEquation)
                except:
                    equation = "Error: Non-real Result"
            elif 'log' in equation:
                findLog = equation.find('log')
                findBase = equation.find(',')
                closingLog = equation.find(']')
               # print("\nfindLog: ", findLog)
               # print("findBase: ", findBase)
               # print("closingLog: ", closingLog)
                logBase = equation[findLog+4:findBase]
               # print("Base: ", logBase)
                logEquation = equation[findBase+1:closingLog]
               # print("\nlog: ", logEquation)
                           
                firstRHS_Paren = equation.find(']')
                eqLHS = equation[0:findLog]
                eqRHS = equation[firstRHS_Paren+1:len(equation)]
                equation = equation[findLog:firstRHS_Paren+1]
                #print("\nLHS: ", eqLHS)
               # print("RHS: ", eqRHS)
               # print("Equation log: ", equation)
                try:
                    if(Checks.parenCheck(logEquation) == True):
                        logEquation = Checks.addMulti(logEquation)
                        ans = eval(logEquation)
                    else:
                        ans = eval(logEquation)
                    
                # print("Parse ANS: ", ans)
                    result = Math.logrithim(logBase, ans) ### add base before paren?
                    result = Checks.formatFloat(result)
                # print("RESULT: ", result)
                    equation = ''.join([eqLHS, result, eqRHS])
                    #print("FULL EQ: ", equation)
                    # print("Final: ", simpEq)
                    # print("logEquation: ", logEquation)
                except:
                    equation = "Error: Non-real Result"
            elif '√' in equation:
                equation = Checks.addFuncMulti(equation)
                #print("add multi1: ", equation)
                findSqrt = equation.find('√')
                closingLog = equation.find(']')
                sqrtEquation = equation[findSqrt+2:closingLog]
                #print("sqrt: ", sqrtEquation)

                
                firstRHS_Paren = equation.find(']')
                eqLHS = equation[0:findSqrt]
                eqRHS = equation[firstRHS_Paren+1:len(equation)]
                equation = equation[findSqrt:firstRHS_Paren+1]
                # print("LHS: ", eqLHS)
                # print("RHS: ", eqRHS)
                # print("Equation Sqrt: ", equation)

                if(Checks.parenCheck(sqrtEquation) == True):
                    sqrtEquation = Checks.addMulti(sqrtEquation)
                    ans = eval(sqrtEquation)
                else:
                    ans = eval(sqrtEquation)
                
                result = Math.sqRoot(ans)
                # print("STR: ", result)
                equation = ''.join([eqLHS, result, eqRHS])
                #print("Sqrt Eq: ", equation)
            else:
                #print("No opperations remaining")
                #print("\nEqaution: ", equation)
                break #opsLeft = False       #**These both hit when all conditions werent met
           # print("Functions? ", Checks.functionsCheck(equation))      #**shouldnt need but add proper else when verified 

        return equation
    
    def getNewResult(equation):

        if(Checks.symbolSyntax(equation) == True):
            ans = "Syntax Error; Operations" # Increase box size to fit text
            return ans 
        elif(Checks.parenSyntaxCheck(equation) == False):
            ans = "Syntax Error; Parenthesis Mismatch" # Increase box size to fit text
            return ans
        else:
            try:
                if(Checks.functionsCheck(equation) == True):
                    if(Checks.imbeddedFunc(equation) == True):
                        equation = Math.getFuncInterior(equation)
                    equation = Checks.addMulti(equation)
                    #print("Equation After addMutli: ", equation)
                    equation = Checks.addFuncMulti(equation)
                    #print("Equation After addMutliFunc: ", equation)
                    equation = Checks.swapSymbols(equation)
                    #print("Equation After Swap: ", equation)
                    equation = Math.getValues(equation)
                else:
                    equation = Checks.addMulti(equation)
                   # print("Equation After addMutli: ", equation)
 
                # getting the ans
                if 'Error' not in equation:
                    ans = Checks.formatFloat(float(eval(equation))) #ans = float(str(eval(equation)))
                else:
                    ans = equation
                return ans
   
            except:
                ans = "Wrong Input"
                return ans


    # Error:  3+ln[69]+log[10,23ln[3+3]+1]*2   --- Check for nested func ---
    #    Call imbeddedFunc, get result, place back in, scan until no more imbedded func
    #       Fix string breakdown according to log, ln, sqrt --> subset of lists 
    #
    #   --- Error: quantity of square root squared results in error ---
    #               i.e. sqrt(4)^2 -> Error    (or sqrt(4^2) idr) 
    def getFuncInterior(equation):

        equation = Checks.addFuncMulti(equation)
        lOcc = Checks.findOccurrences(equation, "l")
        sqrtOcc = Checks.findOccurrences(equation, "√") 
        #eOcc = Checks.findOccurrences(equation, "e")
        
        funcOcc = lOcc + sqrtOcc #+ eOcc
        print("funcOcc: ", funcOcc)

        for x in reversed(funcOcc): #while brackOcc != 1:
            print("X = ", x)
            lastBrack = equation.find(']')
            M = equation[x:lastBrack+1] # insideEq
            M = Checks.swapSymbols(M)
            
            L = equation[0:x] # LHS
            print("L: ", L)
            print("M: ", M)
            R = equation[lastBrack+1:len(equation)] # RHS
            print("R: ", R)

            M = Math.getValues(M)

            equation = ''.join([L, M, R])
        
        #if 'Error' not in equation:
            #ans = eval(equation)
            #ans = str(ans)
        print("Return EQ: ", equation)
        return equation #ans

class Checks():  
    def __init__(self):
        super().__init__()

    # Check that there are no mismatched parenthesis
    def parenSyntaxCheck(equation):

        parenLHS = 0
        parenRHS = 0
        
        for x in equation:
            if x == '(':
                parenLHS = parenLHS + 1
            
            if x == ')':
                parenRHS = parenRHS + 1

        if(parenLHS == parenRHS):
            check = True
        else:
            check = False

        return check

    # Implementation of isNumber() function 
    def isNumber(s):

        # try to convert the string to int
        try:
            n = int(s)
            return True
        # catch exception if cannot be converted
        except ValueError:
            return False


    '''
    Other 'isNumber()' codeblock
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass
 
        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass
 
        return False
    '''        
    def addMulti(equation):

        parenPrefixIndex = 0
        parenIndex = 0 
        
        parenList = Checks.findOccurrences(equation, '(')
        for x in equation:
            if(x == '(' and x != 0):
                parenIndex = parenList.pop()
                parenPrefixIndex = parenIndex-1
                prefixValue = equation[parenPrefixIndex]
                if(Checks.isNumber(prefixValue) == True):
                    equation = equation[:parenPrefixIndex+1] + '*' + equation[parenIndex:]

        equation = Checks.doubleParenMulti(equation)
        return equation 

    # verifies that no two operations are NOT next to each other
    def symbolSyntax(equation):
        
        addList = Checks.findOccurrences(equation, '+')
        subList = Checks.findOccurrences(equation, '-')
        divList = Checks.findOccurrences(equation, '/')
        mulList = Checks.findOccurrences(equation, '*')
        decList = Checks.findOccurrences(equation, '.')
        symbolList = addList + subList + divList + mulList + decList
        symbolList.sort()

        if(len(symbolList) == 0):
            return False
        # Check if beginning or end of equation start with an operator
        elif(symbolList[0] == 0 or symbolList[-1] == (len(equation)-1)):
            #equation = "Invaild Operation Syntax"
            # return equation
            return True
        else: # Check if duplicate symbols appear
            temp = symbolList[0:1]
            for i in range(len(symbolList)-1):
                if symbolList[i] != symbolList[i+1]:
                    temp.append(symbolList[i+1])
                    if(1+(symbolList[i]) == symbolList[i+1]):
                       # equation = "Invaild Operation Syntax"
                       # return equation
                        return True
        return False
    
    # Checks to see if the equation contains parenthesis
    def parenCheck(equation):
        
        if '(' in equation:
            return True
        else:
            return False     

    # Finds occrrences of each given symbol in the given equation
    def findOccurrences(equation, symbol):
        return [i for i, letter in enumerate(equation) if letter == symbol]

    def functionsCheck(equation):
        
        functionsBool = False
        
        if 'ln' in equation:
            functionsBool = True
        elif 'log' in equation:
            functionsBool = True
        elif 'e' in equation:
            functionsBool = True
        elif '10^' in equation:
            functionsBool = True
        elif '√' in equation:
            functionsBool = True
        elif 'π' in equation:
            functionsBool = True
        else:
            functionsBool = False

        return functionsBool

    def symbolCheck(equation):
            
        symbolBool = False
        
        if '+' in equation:
            symbolBool = True
        elif '-' in equation:
            symbolBool = True
        elif '*' in equation:
            symbolBool = True
        elif '/' in equation:
            symbolBool = True
        # elif '√' in equation:
        #     symbolBool = True
        # elif 'π' in equation:
        #     symbolBool = True
        else:
            symbolBool = False

        return symbolBool

    ## add catch for: ...+3)x where x = e or x = pi (check other instances)
    '''add catch for ln[3+4√[2+2]+3]
    
        take insides of ln[] so in this case, 3+4√[2+2]+3. 
        check if it contains [] 
        if it does
            take first '[' and last ']'
        then 
            recursivley check until there are no more []
        
    
    '''
    def addFuncMulti(equation):
       # newEquation = equation
        prefixIndex = 0
        symIndex = 0 
        
        if 'l' in equation:
            L_List = Checks.findOccurrences(equation, 'l')
            for x in equation:
                if(x == 'l' and equation[0] != 'l'):
                    symIndex = L_List.pop()
                    prefixIndex = symIndex-1
                    prefixValue = equation[prefixIndex]
                    if(Checks.isNumber(prefixValue) == True or prefixValue == ')' or prefixValue == 'π' or prefixValue == ']'):
                        equation = equation[:prefixIndex+1] + '*' + equation[symIndex:]
                        
        if '√' in equation: # √ = \u221A
            sqrtList = Checks.findOccurrences(equation, '√')
            for x in equation:
                if(x == '√' and equation[0] != '√'):
                    symIndex = sqrtList.pop()
                    prefixIndex = symIndex-1
                    prefixValue = equation[prefixIndex]
                    if(Checks.isNumber(prefixValue) == True or prefixValue == ')' or prefixValue == 'π' or prefixValue == ']'):
                        equation = equation[:prefixIndex+1] + '*' + equation[symIndex:]

        #if 'π' in equation: # √ = \u221A
        if 'π' in equation:
            piList = Checks.findOccurrences(equation, 'π')
            for x in equation:
                if(x == 'π' and equation[0] != 'π'):
                    symIndex = piList.pop()
                    prefixIndex = symIndex-1
                    prefixValue = equation[prefixIndex]
                    if(Checks.isNumber(prefixValue) == True or prefixValue == ')' or prefixValue == 'π' or prefixValue == ']'):
                        equation = equation[:prefixIndex+1] + '*' + equation[symIndex:]
                elif(equation[0] == 'π' and len(piList) != 1):
                    symIndex = piList.pop()
                    prefixIndex = symIndex-1
                    prefixValue = equation[prefixIndex]
                    equation = equation[:prefixIndex+1] + '*' + equation[symIndex:]
                    if len(piList) == 1:
                        break

        if 'e' in equation: 
            eList = Checks.findOccurrences(equation, 'e')
            
            for x in equation:
                if(x == 'e' and equation[0] != 'e'):
                    symIndex = eList.pop()
                    prefixIndex = symIndex-1
                    prefixValue = equation[prefixIndex]
                    if(Checks.isNumber(prefixValue) == True or prefixValue == ')' or prefixValue == 'π' or prefixValue == ']'):
                        equation = equation[:prefixIndex+1] + '*' + equation[symIndex:]
                elif(equation[0] == 'π' and len(eList) != 1):
                    symIndex = eList.pop()
                    prefixIndex = symIndex-1
                    prefixValue = equation[prefixIndex]
                    equation = equation[:prefixIndex+1] + '*' + equation[symIndex:]
                    if len(eList) == 1:
                        break
       
        return equation # √ π
  
    '''
        doubleParenMulti
            This function removes the ')(' from the equaion, 
            if found, and replaces it with ')*(' for calculations. 
            If ')(' does not appear, return the original 
            equation.
        
        @param equation (string)
        @return newEq (string of formatted equation)

    '''
    def doubleParenMulti(equation):
        
        equation = str(equation)
        
        if(')(' in equation):
            equation = equation.replace(')(', ')*(')

        return equation

    def swapSymbols(equation):
        
        equation = str(equation)
        
        if '√' in equation:
            equation = equation.replace('√', 'sqrt')

        if 'π' in equation:
            equation = equation.replace('π', "math.pi")

        if 'e^' in equation:
            equation = equation.replace('e^', 'exp')

        if '^' in equation:
            equation = equation.replace('^', '**')
        
        return equation

    '''
        formatFloat
            This function takes in a number and removes all 
            characters 16 places after the decimal point. 
            It also removes any unwanted values (namely '+' and 'j') 
            that appear after calculations. It also cleans up any remaining
            0's that appear after the decimal (i.e. '54.00000' will
            be trimmed to '54'). The formatted number will then 
            be returned. 

        @param number (string)
        @return number (string)

    '''
    def formatFloat(number):
        
        number = "{0:.3f}".format(number)
        # number = "{0:.16f}".format(number)

        if( '+' in number):
            plusSym = number.find('+')
            number = number[:plusSym]
        
        for e in number:
            if('0' == number[-1]):
                number = number[:-1]
        
        if(number[-1] == '.'):
            number = number[:-1]

        if(number[-1] == ')'):
            number = number[:-1]
                    

        return number

    def imbeddedFunc(equation):

        if '[' in equation:
            firstBrack = equation.find('[')
            lastBrack = equation.rfind(']')
            insideEq = equation[firstBrack+1:lastBrack-1]
            #print("INSIDE EQ: ", insideEq)
            if '[' in insideEq:
                fBool = True
            else:
                fBool = False
        else:
            fBool = False
        
        return fBool