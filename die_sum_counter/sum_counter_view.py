from graphics import *

from msdie import MultiSidedDie

class SumCounter:
    
    def __init__( self, win, centerPt, targetValue):
        
        self.text = Text( centerPt, "")
        self.text.draw( win )
        self.targetValue = targetValue
        self.targetValueCount = 0 #default of my count
        self.setText()
        
    def setText(self): # This populates the die counter on the right side of the graphic
        self.text.setText("Total of {value} counted {valueCount} times".format( value=self.targetValue, valueCount=self.targetValueCount))
    def handleRoll(self): #this increments the count  if the sum argument matches the sum a `SumCounterView` object is counting 
        self.targetValueCount += 1