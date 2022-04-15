import math
from cmath import sin, sqrt

class Geo:
    def __init__(self):
        super().__init__()

    '''
        formatFloat
            This function takes in a number and removes all 
            characters five places after the decimal point. 
            It also removes any unwanted values (namely '+' and 'j') 
            that appear after calculations. It also cleans up any remaining
            0's that appear after the decimal (i.e. '54.00000' will
            be trimmed to '54'). The formatted number will then 
            be returned. 

        @param number (string)
        @return number (string)

    '''
    def formatFloat(number):
        
        number = "{0:.5f}".format(number)

        if( '+' in number):
            plusSym = number.find('+')
            number = number[:plusSym]
        
        for e in number:
            if('0' == number[-1]):
                number = number[:-1]
        
        if(number[-1] == '.'):
            number = number[:-1]
                    

        return number
    
    '''
        formatAngle
            This function takes in a number and removes all 
            characters two places after the decimal point. 
            It also removes any unwanted values (namely '+' and 'j') 
            that appear after calculations.The formatted number will 
            then be returned. 

        @param number (string)
        @return number (string)

    '''
    def formatAngle(number):
            
        number = "{0:.2f}".format(number)

        if( '+' in number):
            plusSym = number.find('+')
            number = number[:plusSym]

        number = float(number)
        
        return number

    '''
        checkFloat
            This function will check if the value passed in
            is not a character. If it is a character (meaning
            it cannot be converted to a float), the function 
            will return 'False'. If the value can be converted 
            to a float, 'True' will be returned.

        @param value
        @return bool
    '''
    def checkFloat(value):
        testVal = value
        try:
            float(value)
            return True
        except:
            return False

# Add catch for invalid triangle if possible - nested try/except?
class Triangle():
    def __init__(self):
        super().__init__()

    '''
    baseHeightCalc(base, height):
        This function will take in a base and height from a user 
        and calculate the area. If either base or height is 
        less than or equal to zero, and error message will 
        be returned to be displayed. Otherwise, the calculated 
        area will be displayed.

    @param: base, height
    @return: area

    '''
    def baseHeightCalc(base, height):

        try:
            base = float(base)
            height = float(height)

            # verify that values are greater than 0
            if(base <= 0 or height <=0):
                area = "Error:\n" + "Base and Height must be greater than 0"
                return area

            area = float(0.5) * base * height
            area = Geo.formatFloat(area)
            return area
        except ValueError:
            area = "Error:\n" + "Calculation/Conversion error\n" + "Verify only numbers were entered"
            return area
    
    '''
        sssCalc(S1, S2, S3):
            This function finds the area, perimeter, and all side/angles
             of a triangle given three sides. If any of the following 
             occurr it will return an error message to be displayed:
                - If anything other than a number is entered
                - If any of the sides are less than or equal to 0
                - If the sum of two sides is less than the third side
           
            Otherwise, it will return the calculated area and perimeter
        
        @param: S1, S2, S3 (three sides input by user)
        @return: string (string of all triangle values)

    '''
    def sssCalc(S1, S2, S3):
        
        try:        
            sideA = float(S1)
            sideB = float(S2)
            sideC = float(S3)

            # verify that sides are greater than 0
            if(sideA <= 0 or sideB <=0 or sideC <=0):
                allSSSValues = "Error:\n" + "Sides must be greater than 0"
                return allSSSValues
            
            if((sideA + sideB <= sideC) or (sideA + sideC <= sideB) or (sideB + sideC) <= sideA):
                allSSSValues = "Error:\n" + "The sum of two sides must be larger than the third"
                return allSSSValues

            # Get other values
            angleA = Triangle.lawOfCos(sideA, sideB, sideC)
            angleB = Triangle.lawOfCos(sideB, sideA, sideC)
            angleB = float(angleB)
            angleC = 180 - (angleA + angleB)
            
            angleA = Geo.formatAngle(angleA)
            angleB = Geo.formatAngle(angleB)
            angleC = Geo.formatAngle(angleC)
            sideA = Geo.formatFloat(sideA)
            sideB = Geo.formatFloat(sideB)
            sideC = Geo.formatFloat(sideC)
            
           # Get area/perimeter
            area = Triangle.areaTriCalc(sideA, sideB, angleC)
            perim = Triangle.perimTriCalc(sideA, sideB, sideC)
            allSSSValues = Triangle.triValuesList(area, perim, sideA, sideB, sideC, angleA, angleB, angleC)

            return allSSSValues
        
        # catch exception if cannot be calculated
        except ValueError:
            #area = "Error - Check Values"
            allSSSValues = "Error:\n" + "Calculation/Conversion error\n" + "Verify only numbers were entered"
            return allSSSValues

    '''
        sasCalc(S1, A, S2):
            This function finds the area, perimeter, and all sides/angles 
            of a triangle given two sides with an angle between them. If 
            greater than or equal to 180 It will return an error message 
            to be displayed if any of the following occur:
                - If anything other than a number is entered
                - If the angle entered is less than or equal to zero
                - If the angle greater than or equal to 180
                - If either side is less than or equal to zero

            Otherwise, it will return the calculated area and perimeter
        
        @param: S1, A, S2 (two sides and an angle input by user)
        @return string (string of all triangle values)

        NOTE: For finding all values of a triangle using SAS: https://www.mathsisfun.com/algebra/trig-solving-sas-triangles.html

    '''
    def sasCalc(S1, A, S2):

        try:        
            sideB = float(S1)
            angleA = float(A)
            sideC = float(S2)
            
            if(angleA <= 0 or angleA >= 180):
                allSASValues = "Error:\n" + "Angle A must be greater than 0 and less than 180"
                return allSASValues
            elif(sideB <= 0 or sideC <=0 ):
                allSASValues = "Error:\n" + "Sides must be greater than 0"
                return allSASValues

            # Get other sides/angles
            sideA = Triangle.cosineRule(sideB, angleA, sideC)
            angleC = Triangle.lawOfCos(sideC, sideA, sideB)
            angleB = 180 - (angleA + angleC)
            sideA = Geo.formatFloat(sideA)
            angleB = Geo.formatAngle(angleB)
            angleC = Geo.formatAngle(angleC)
            
            # Calculate area and perimeter
            area = Triangle.areaTriCalc(sideA, sideB, angleC)
            perim = Triangle.perimTriCalc(sideA, sideB, sideC)

            angleA = Geo.formatAngle(angleA)
            sideB = Geo.formatFloat(sideB)
            sideC = Geo.formatFloat(sideC)

            allSASValues = Triangle.triValuesList(area, perim, sideA, sideB, sideC, angleA, angleB, angleC)

            return allSASValues
        
        # catch exception if cannot be calculated
        except ValueError:
            area = "Error:\n" + "Calculation/Conversion Error" + "Verify only numbers were entered"
            return allSASValues

    '''
        asaCalc(A1, S, A2):
            This function finds the area, perimeter, and all side/angles 
            of a triangle given two sides with an angle between them. 
            If greater than or equal to 180 It will return an error 
            message to be displayed if any of the following occur:
                - If anything other than a number is entered
                - If either angle entered is less than or equal to zero
                - If either angle greater than or equal to 180
                - If the sum of the two angles is greater than or equal to 180
                - If the side is less than or equal to zero

            Otherwise, it will return the calculated area and perimeter
        
        @param: A1, S, A2 (two angles and a side input by user)
        @return string (string of all triangle values)

        NOTE: For all sides using ASA - https://www.mathsisfun.com/algebra/trig-solving-asa-triangles.html

    '''
    def asaCalc(A1, S, A2):
                       
        try:        
            angleA = float(A1)
            sideC = float(S)
            angleB = float(A2)
            
            if(angleA <= 0 or angleA >= 180 or angleB <= 0 or angleB >= 180):
                allASAValues = "Error:\n" + "Angles must be greater than 0 and less than 180"
                return allASAValues
            elif(angleA + angleB >= 180):
                allASAValues = "Error:\n" + "The sum of angles A and B must be less than 180"
                return allASAValues
            elif(sideC <= 0):
                allASAValues = "Error:\n" + "Side C must be greater than 0"
                return allASAValues


            # Calculate remaining angle
            angleC = 180 - (angleA + angleB)

            # Calculate remaining sides
            sideA = (sideC * math.sin(math.radians(angleA)))/math.sin(math.radians(angleC))
            sideB = (sideA * math.sin(math.radians(angleB)))/math.sin(math.radians(angleA))
            sideA = Geo.formatFloat(sideA)
            sideB = Geo.formatFloat(sideB)

           # Calculate area and perimeter
            area = Triangle.areaTriCalc(sideA, sideB, angleC)
            perim = Triangle.perimTriCalc(sideA, sideB, sideC)

            angleA = Geo.formatAngle(angleA)
            angleB = Geo.formatAngle(angleB)
            angleC = Geo.formatAngle(angleC)
            sideC = Geo.formatFloat(sideC)

            allASAValues = Triangle.triValuesList(area, perim, sideA, sideB, sideC, angleA, angleB, angleC)
            
            return allASAValues
        
        # catch exception if cannot be calculated
        except ValueError:
            allASAValues = "Error:\n" + "Calculation/Conversion error\n" + "Verify only numbers were entered"
            return allASAValues

    '''
        ssaCalc(S1, S2, A1)
            This function finds the area, perimeter, and all sides/angles 
            of a triangle given two sides with an angle between them. 
            If greater than or equal to 180 It will return an error message 
            to be displayed if any of the following occur:
                - If anything other than a number is entered
                - If either angle entered is less than or equal to zero
                - If either angle greater than or equal to 180
                - If the side is less than or equal to zero

            Otherwise, it will return the calculated area and perimeter
        
        @param: S1, S2, A1 (two sides and an angle input by user)
        @return string (string of all triangle values)

        NOTE: For all sides using ASA - https://www.mathsisfun.com/algebra/trig-solving-ssa-triangles.html
        
    '''
    def ssaCalc(S1, S2, A1):

        try:        
            sideA = float(S1)
            angleA = float(A1)
            sideB = float(S2)
            
            if(angleA <= 0 or angleA >= 180):
                ssaValues = "Error:\n" + "Angle A must be greater than 0 and less than 180"
                return ssaValues
            elif(sideA <= 0 or sideB <= 0):
                ssaValues = "Error:\n" + "Sides must be greater than 0"
                return ssaValues
            
            # Get remaining angles
            temp = (sideB * math.sin(math.radians(angleA)))/sideA
            angleB = math.degrees(math.asin(temp))
            angleB = Geo.formatAngle(angleB)
            angleB = float(angleB)
            angleC = 180 - (angleA + angleB)

            # Get final side
            sideC = (sideA * math.sin(math.radians(angleC)))/math.sin(math.radians(angleA))
            sideC = Geo.formatFloat(sideC)
            angleC = Geo.formatAngle(angleC)
            
            # Calculate area and perimeter
            area = Triangle.areaTriCalc(sideA, sideB, angleC)
            perim = Triangle.perimTriCalc(sideA, sideB, sideC)

            angleA = Geo.formatAngle(angleA)
            sideA = Geo.formatFloat(sideA)
            sideB = Geo.formatFloat(sideB)

            ssaValues = Triangle.triValuesList(area, perim, sideA, sideB, sideC, angleA, angleB, angleC)
            return ssaValues
        
        # catch exception if cannot be calculated
        except ValueError:
            ssaValues = "Error:\n" + "Calculation/Conversion error\n" + "Verify only numbers were entered"
            return ssaValues

    '''
        aasCalc(A1, A2, S)
            This function finds the area, perimeter, and all sides/angles
            of a triangle given two sides with an angle between them. 
            If greater than or equal to 180 It will return an error message 
            to be displayed if any of the following occur:
                - If anything other than a number is entered
                - If either angle entered is less than or equal to zero
                - If either angle greater than or equal to 180
                - If the sum of the two angles is greater than or equal to 180
                - If the side is less than or equal to zero

            Otherwise, it will return the calculated area and perimeter
        
        @param: A1, A2, S (two angles and a side input by user)
        @return string (string of all triangle values)

        NOTE: For all sides using AAS - https://www.mathsisfun.com/algebra/trig-solving-aas-triangles.html
    '''
    def aasCalc(A1, A2, S):
        
        try:        
            angleA = float(A1)
            sideA = float(S)
            angleB = float(A2)
            
            if(angleA <= 0 or angleA >= 180 or angleB <= 0 or angleB >= 180):
                allAASValues = "Error:\n" + "Angles must be greater than 0 and less than 180"
                return allAASValues
            elif(angleA + angleB >= 180):
                allAASValues = "Error:\n" + "The sum of angles A and B must be less than 180"
                return allAASValues
            elif(sideA <= 0):
                allAASValues = "Error:\n" + "Side A must be greater than 0"
                return allAASValues

            # Calculate remaining angle
            angleC = 180 - (angleA + angleB)
            
            # Calculate remaining sides
            sideC = (sideA * math.sin(math.radians(angleC)))/math.sin(math.radians(angleA))
            sideB = (sideA * math.sin(math.radians(angleB)))/math.sin(math.radians(angleA))
            sideC = Geo.formatFloat(sideC)
            sideB = Geo.formatFloat(sideB)
            angleC= Geo.formatAngle(angleC)

            # Calculate area and perimeter
            area = Triangle.areaTriCalc(sideA, sideB, angleC)
            perim = Triangle.perimTriCalc(sideA, sideB, sideC)

            angleA = Geo.formatAngle(angleA)
            angleB = Geo.formatAngle(angleB)
            sideA = Geo.formatFloat(sideA)
            
            ssaValues = Triangle.triValuesList(area, perim, sideA, sideB, sideC, angleA, angleB, angleC)
            return ssaValues
        
        # catch exception if cannot be calculated
        except ValueError:
            allAASValues = "Error:\n" + "Calculation/Conversion error\n" + "Verify only numbers were entered"
            return allAASValues
    
    '''
        cosineRule()
            This function takes in a side, angle, and side to 
            calculate the final side. Checks are done to verify
            that each side is greater than 0. Also verifies the
            given angle is greater than 0 and less than 180. Then 
            the remaining side is calculated, formatted to five
            decimal places, then converted to float to be returned
            
        @param side, angle, side
        @return side (the remaining side not given)
      '''
    def cosineRule(SA, AB, SC):
        sideA = float(SA)
        angleB = float(AB)
        sideC = float(SC)
        
        if(angleB <= 0 or angleB >= 180 or sideA <= 0 or sideC <= 0 ):
            sideB = "Error - Check Values"
            return sideB
        
        temp1 = sideA**2 + sideC**2
        temp2 = 2*sideA*sideC
        
        sideB = sqrt(temp1 - temp2 * math.cos(math.radians(angleB)))
        sideB = Geo.formatFloat(sideB)
        sideB = float(sideB)
        
        return sideB
    '''
        lawOfCos()
            This function calculates an angle when given three sides, 
            which are greater than 0 (otherwise return error) using the 
            Law of Cosine. The function will then format the floating 
            point to 5 decimal places then convert back to a float. 
            The result is then returned. 
        
        @para side, side, side
        @return angle 
    '''
    def lawOfCos(SA, SB, SC):
        sideA = float(SA)
        sideB = float(SB)
        sideC = float(SC)
        
        if(sideA <= 0 or sideB <= 0 or sideC <= 0):
            sideB = "Error - Check Values"
            return sideB
        
        top = (sideA**2 - (sideB**2 + sideC**2))
        bottom = (-2)*(sideB)*(sideC)
        angleA = math.degrees(math.acos(top/bottom))
        angleA = Geo.formatFloat(angleA)
        angleA = float(angleA)
        
        return angleA

    """
        areaTriCalc()
        
        This function calculates the area of a triangle given two sides and 
            an angle. First converts parameters to floats (if they weren't 
            already) then verifies that 0 < angleC < 180. Once complete, the
            area is then calculated with A = (1/2)(a)(b)(sin(c)). The result
            is then formatted by Geo.formatFloat(). Area is finally returned.
            
        @param side, side, angle
        @return area
    """
    def areaTriCalc(sideA, sideB, angleC):
        
        # verify variables are floats and meet requirements
        sideA = float(sideA)
        sideB = float(sideB)
        angleC = float(angleC)
        
        if(angleC <= 0 or angleC >= 180 or sideA <= 0 or sideB <= 0 ):
            area = "Error - Check Values"
            return area
        
        area = (0.5) * sideA * sideB * (math.sin(math.radians(angleC)))
        area = Geo.formatFloat(area)
        return area
    
    """
        perimTriCalc

        This function calculates the perim of a triangle given all sides
            First converts parameters to floats (if they weren't already) 
            then verifies that all sides are greater than zero. Once complete, 
            the perimeter is then calculated by adding all sides together. The 
            result is then formatted by Geo.formatFloat(). perim is finally returned.
            
        @param sideA, sideB, sideC
        @return perim
    """
    def perimTriCalc(sideA, sideB, sideC):
        
        # verify variables are floats and meet requirements
        sideA = float(sideA)
        sideB = float(sideB)
        sideC = float(sideC)
        
        if(sideA <= 0 or sideB <= 0 or sideC <= 0):
            perim = "Error - Check Values"
            return perim
        
        perim = sideA + sideB + sideC
        perim = Geo.formatFloat(perim)
        return perim

    '''
        triValuesList
            This function takes in eight perameters that are then formatted.
            Once each value is added to the final string, the function then
            passes the string back to be displayed on the screen.

        @param: area, perim, sideA, sideB, sideC, angleA, angleB, angleC
        @return allValues (formatted string with passed in values)
    
    '''
    def triValuesList(area, perim, sideA, sideB, sideC, angleA, angleB, angleC):

        area = "     Area = " + str(area) + " units²\n"
        perim = "     Perimeter = " + str(perim) + " units\n\n"
        sideA = "     Side a = " + str(sideA) + " units\n"
        sideB = "     Side b = " + str(sideB) + " units\n"
        sideC = "     Side c = " + str(sideC) + " units\n\n"
        angleA = "     Angle A = " + str(angleA) + " degrees\n"
        angleB = "     Angle B = " + str(angleB) + " degrees\n"
        angleC = "     Angle C = " + str(angleC) + " degrees\n"

        allValues = "The values of the Triangle are: \n\n" + area + perim + sideA + sideB + sideC + angleA + angleB + angleC
        return allValues
class Circle():
    def __init__(self):
        super().__init__()

    '''
        calcCircle
            This function takes in four parameters which are then 
            added to a list. It first determines if a number or 
            character were entered. If not the function scans 
            through the list to find which value was entered.
            Once the value is found, it will find the path to 
            its specific branch and calculate the other values.
            (i.e. radius = 6 was entered, function will go to 
            the first if and find diameter, area, and circumference)

        @param radius, diameter, area, circumference
        @ return r, d, a, c (radius, diameter, area, circumference)

    '''
    def calcCircle(radius, diameter, area, circumference):

        circValList = [radius, diameter, area, circumference]

        try:

            for s in circValList:
                if s.isdigit() and s != '0' or Geo.checkFloat(s) == True and s != '0':
                    foundVal = circValList.index(s)
                    if(foundVal == 0): # if input is the radius

                        r = float(s)
                        d = r*2
                        a = math.pi*(r**2)
                        c = 2*math.pi*r
                        r = Geo.formatFloat(r)
                        d = Geo.formatFloat(d)
                        a = Geo.formatFloat(a)
                        c = Geo.formatFloat(c)
                        
                        return r, d, a, c
                    elif(foundVal == 1): # if input is the diameter

                        d = float(s)
                        r = d/2
                        a = a = math.pi*(r**2)
                        c = 2*math.pi*r
                        r = Geo.formatFloat(r)
                        d = Geo.formatFloat(d)
                        a = Geo.formatFloat(a)
                        c = Geo.formatFloat(c)

                        return r, d, a, c
                    elif(foundVal == 2): # if input is the area

                        a = float(s)
                        r = sqrt(a/math.pi)
                        c = 2*math.pi*r
                        d = 2*r
                        r = Geo.formatFloat(r)
                        d = Geo.formatFloat(d)
                        a = Geo.formatFloat(a)
                        c = Geo.formatFloat(c)

                        return r, d, a, c
                    elif(foundVal == 3): # if the input is the circumference
                        
                        c = float(s)
                        r = c/(2*math.pi)
                        d = 2*r
                        a = math.pi*(r**2)
                        r = Geo.formatFloat(r)
                        d = Geo.formatFloat(d)
                        a = Geo.formatFloat(a)
                        c = Geo.formatFloat(c)

                        return r, d, a, c
                    else: # shouldnt be needed
                        print("ERROR SOMEWHERE; ENTER A VALUE?")
                else: # shouldnt be needed
                    print("ENTER A VAL > 0")
        except:
            print("ERROR TRY")

        print(circValList)
        r = "Check Input"
        d = "Check Input"
        a = "Check Input"
        c = "Check Input"
        return r, d, a, c
class Quadrilateral():
    def __init__(self):
        super().__init__()

    '''
        squareCalc
            This function takes in a single side of a square.
            It then checks that the value entered is greater
            than zero. Once verified, area, perimeter, and the
            diagonal will be calculated. Then each value will be 
            formatted and passed into quadValuesList for all 
            values to be formatted into a single string. That 
            string is then returned to be displayed.

        @param SA (side A)
        @return allSquareValues (string)
    
    ''' 
    def squareCalc(SA):
        try:        
            sideA = float(SA)
            
            if(sideA <= 0):
                allSquareValues = "Error:\n" + "The side must be greater than 0"
                return allSquareValues

            area = sideA * sideA
            perimeter = sideA*4
            diagonal = sqrt(2)*sideA

            area = Geo.formatFloat(area)
            perimeter = Geo.formatFloat(perimeter)
            diagonal = Geo.formatFloat(diagonal)
            allSquareValues = Quadrilateral.quadValuesList(area, perimeter, diagonal, "Square")
            
            return allSquareValues
        
        # catch exception if cannot be calculated
        except ValueError:
            allSquareValues = "Error:\n" + "Calculation/Conversion error\n" + "Verify only numbers were entered"
            return allSquareValues

    '''
        rectCalc
            This function takes in a length and width from the user.
            After the length and width are converted to floats and
            verified that they are greater than zero they will then
            be used to calculate the area, perimeter, and diagonal of
            the rectangle. Each result will be formatted then passed 
            into 'quadValuesList' to be formatted into a single string.
            Once that is complete, the string (allRectValues) will be 
            returned to be displayed on the screen.
        
        @param L, W (length, width)
        @return allRectValues (string)    
    ''' 
    def rectCalc(L, W):
        try:        
            length = float(L)
            width = float(W)
            
            if(length <= 0 or width <= 0):
                allRectValues = "Error:\n" + "Length and Width must be greater than 0"
                return allRectValues

            area = length * width
            perimeter = (length*2) + (width*2)
            diagonal = sqrt((length**2)+(width**2))
            
            area = Geo.formatFloat(area)
            perimeter = Geo.formatFloat(perimeter)
            diagonal = Geo.formatFloat(diagonal)
            allRectValues = Quadrilateral.quadValuesList(area, perimeter, diagonal, "Rectangle")
            
            return allRectValues
        
        # catch exception if cannot be calculated
        except ValueError:
            allRectValues = "Error:\n" + "Calculation/Conversion error\n" + "Verify only numbers were entered"
            return allRectValues

    '''
        rhombusCalc
            This function takes in a side and height from the user.
            After the side and height are converted to floats and
            verified that they are greater than zero they will then
            be used to calculate the area and perimeter of the rhomus. 
            Each result will be formatted then passed into 'quadValuesList'
            to be formatted into a single string. Once that is complete, 
            the string (allRhomValues) will be returned to be displayed 
            on the screen.
        
        @param sideA, height 
        @return allRhomValues (string) 
    '''
    def rhombusCalc(sideA, height):
        try:        
            sideA = float(sideA)
            height = float(height)
            
            if(sideA <= 0 or height <= 0):
                allRhomValues = "Error:\n" + "Sides and Height must be greater than 0"
                return allRhomValues

            area = sideA * height
            perimeter = sideA*4
            
            area = Geo.formatFloat(area)
            perimeter = Geo.formatFloat(perimeter)

            allRhomValues = Quadrilateral.quadValuesList(area, perimeter, 0, "Rhombus")
            
            return allRhomValues
        
        # catch exception if cannot be calculated
        except ValueError:
            allRhomValues = "Error:\n" + "Calculation/Conversion error\n" + "Verify only numbers were entered"
            return allRhomValues
    
    '''
        parallelogramCalc
            This function takes in two sides (A and B) as well as a height 
            from the user. After the sides and height are converted to floats
            and verified that they are greater than zero they will then
            be used to calculate the area and perimeter of the parallelogram. 
            Each result will be formatted then passed into 'quadValuesList'
            to be formatted into a single string. Once that is complete, 
            the string (allPGValues) will be returned to be displayed 
            on the screen.
        
        @param sideA, sideB, height 
        @return allPGValues (string) 
    '''
    def parallelogramCalc(sideA, sideB, height):
        try:   
            sideA = float(sideA)
            sideB = float(sideB)
            height = float(height)
            if(sideA <= 0 or sideB <= 0 or height <= 0):
                allPGValues = "Error:\n" + "Sides and Height must be greater than 0"
                return allPGValues

            area = sideB * height
            perimeter = (sideA*2) + (sideB*2)

            area = Geo.formatFloat(area)
            perimeter = Geo.formatFloat(perimeter)
            allPGValues = Quadrilateral.quadValuesList(area, perimeter, 0, "Parallelogram")
            
            return allPGValues
        
        # catch exception if cannot be calculated
        except ValueError:
            allPGValues = "Error:\n" + "Calculation/Conversion error\n" + "Verify only numbers were entered"
            return allPGValues

    '''
        trapezoidCalc
            This function takes in four sides (A, B, C and D) as well as a height 
            from the user. After the sides and height are converted to floats
            and verified that they are greater than zero they will then
            be used to calculate the area and perimeter of the trapezoid. 
            Each result will be formatted then passed into 'quadValuesList'
            to be formatted into a single string. Once that is complete, 
            the string (allTrapValues) will be returned to be displayed 
            on the screen.
        
        @param sideA, sideB, sideC, sideD, height 
        @return allTrapValues (string) 
    '''
    def trapezoidCalc(sideA, sideB, sideC, sideD, height):
        try:   
            sideA = float(sideA)
            sideB = float(sideB)
            sideC = float(sideC)
            sideD = float(sideD)
            height = float(height)
            if(sideA <= 0 or sideB <= 0 or sideC <= 0 or sideD <= 0 or height <= 0):
                allTrapValues = "Error:\n" + "Sides and Height must be greater than 0"
                return allTrapValues

            area = 0.5*(height)*(sideA + sideB)
            perimeter = sideA + sideB + sideC + sideD
            
            area = Geo.formatFloat(area)
            perimeter = Geo.formatFloat(perimeter)
            allTrapValues = Quadrilateral.quadValuesList(area, perimeter, 0, "Trapezoid")
            
            return allTrapValues
        
        # catch exception if cannot be calculated
        except ValueError:
            allTrapValues = "Error:\n" + "Calculation/Conversion error\n" + "Verify only numbers were entered"
            return allTrapValues
    
    '''
        quadValuesList
            This fucntion takes in a tuple of perameters to be returned.
            Square and Rectangle are exceptions as they have different
            values. The last parameter (shape) will determine which format
            to use. If 'shape' matches Rhombus, Trapezoid, or Parallelogram 
            then it will use the first format. Otherwise, it will use the 
            second format.

        @param: area, perim, diagonal, shape
        @return: allValues (formatted string describing shape)
    '''
    def quadValuesList(area, perim, diagonal, shape):
        
        area = "     Area = " + str(area) + " units²\n"
        perim = "     Perimeter = " + str(perim) + " units\n"
        diagonal = "     Diagonal (d) = " + str(diagonal) + " units\n"

        if(shape == "Rhombus" or shape == "Trapezoid" or shape == "Parallelogram"):
            allValues = "The values of the " + shape + " are: \n\n" + area + perim
        else:
            allValues = "The values of the " + shape + " are: \n\n" + area + perim + diagonal
        return allValues
