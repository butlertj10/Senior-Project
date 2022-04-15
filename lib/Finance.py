class Finance():
    def __init__(self):
        super().__init__()

    def calcSimpleInterest(P, R, T):
        
        try:        
            P = float(P)
            R = float(R)
            T = float(T)
            
            if(P <= 0 or R <= 0 or T <= 0):
                I = "Values must be greater than 0"
                Total = "Values must be greater than 0"
                return I, Total

            R = R/100
            I = P * R * T
            Total = I + P

            Total = Finance.formatValue(Total)
            I = Finance.formatValue(I)
            
            return I, Total
        
        # catch exception if cannot be calculated
        except ValueError:
            I = "Error Computing/Converting Values" 
            Total = "Verify only numbers were entered"
            return I, Total

    def calcCompoundInterest(P, R, T, N):
        
        try:        
            P = float(P)
            R = float(R)
            T = float(T)
            N = float(N)
            
            if(P <= 0 or R <= 0 or T <= 0 or N <= 0):
                A = "Error - Check Values"
                return A

            R = R/100
            expo = N * T
            temp = 1 + R/N
            A = P * (temp**expo)

            A = Finance.formatValue(A)

            return A
        
        # catch exception if cannot be calculated
        except ValueError:
            A = "Error - Check Values"
            return A

    def calcPresentValue(FV, P, R):
            
        try:        
            FV = float(FV)
            P = float(P)
            R = float(R)
            
            if(FV <= 0 or P <= 0 or R <= 0):
                PV = "Error - Check Values"
                return PV
            
            PV = FV/(1+R/100)**P

            PV = Finance.formatValue(PV)

            return PV
        
        # catch exception if cannot be calculated
        except ValueError:
            PV = "Error - Check Values"
            return PV

    # NEEDS WORK; result incorrect 
    # https://www.calculator.net/future-value-calculator.html
    def calcFutureValue(PV, P, R):
            
        try:        
            PV = float(PV)
            P = float(P)
            R = float(R)
            
            if(PV <= 0 or P <= 0 or R <= 0):
                FV = "Error - Check Values"
                return FV

            FV = PV/(1+R/100)**P

            FV = Finance.formatValue(FV)

            return FV
        
        # catch exception if cannot be calculated
        except ValueError:
            FV = "Error - Check Values"
            return FV

    '''
        formatValue
            This function takes in a number and removes all 
            characters two places after the decimal point. 
            It also removes any unwanted values (namely '+' and 'j') 
            that appear after calculations. It also cleans up any remaining
            0's that appear after the decimal (i.e. '54.00' will
            be trimmed to '54'). The formatted number will then 
            be returned. 

        @param number (string)
        @return number (string)

    '''
    def formatValue(number):
        
        number = "{0:.2f}".format(number)

        if( '+' in number):
            plusSym = number.find('+')
            number = number[:plusSym]
        
        for e in number:
            if('0' == number[-1]):
                number = number[:-1]
        
        if(number[-1] == '.'):
            number = number[:-1]
                    

        return number