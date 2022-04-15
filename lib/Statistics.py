from sympy import Symbol, expand, simplify, symbols, factor, solve
from Operations import Checks
from array import *
import statistics
from Calculus import Calculus
from Geometry import Geo

# CSV Reading: https://www.geeksforgeeks.org/read-a-csv-into-list-of-lists-in-python/

class StatsCalc():
    def __init__(self):
        super().__init__()

    def mainStats(numberSet):

        try:
            setList = str(numberSet).split(",") 
            intList = StatsCalc.listToInt(setList)

            setCount = len(setList) # Count
            setMin = min(setList) # Min
            setMax = max(setList) # Max
            setRange = setMin + " - " + setMax # Range
            setMedian = statistics.median(intList) # Median
            setMean = statistics.mean(intList) # Mean
            setPSD = statistics.pstdev(intList) # Population Standard Deviation
            setPSD = Geo.formatFloat(setPSD)
            setSSD = statistics.stdev(intList) # Sample Standard Deviation
            setSSD = Geo.formatFloat(setSSD)
            return StatsCalc.statsFormat(setCount, setMin, setMax, setRange, setMedian, setMean, setPSD, setSSD)
        
        except:
            return "Error: Unable to Analyze Set"


    def listToInt(sList):

        iList = [int(i) for i in sList]

        return iList


    def statsFormat(setCount, setMin, setMax, setRange, setMedian, setMean, setPSD, setSSD):

        statsFormatted = '''
            Count: {count}
                
            Minimum: {min}
            Maximum: {max}
            Range:  {range}
                
            Median: {median}
            Mean: {mean}
                
            Standard Deviation:
                    Poplulation: {PSD}
                    Sample: {SSD}
        
        '''.format(count=setCount, min=setMin, max=setMax, 
                   range=setRange, median=setMedian, 
                   mean=setMean, PSD=setPSD, SSD=setSSD)
        
        return statsFormatted

