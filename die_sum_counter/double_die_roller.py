from button import Button
from die_view import DieView
from sum_counter_view import *
from graphics import *


def main(): #my graph window
    win = GraphWin("Double_Die_Roller", 425, 200)
    win.setBackground( 'dark red' )
    dieview1 = DieView( win, Point( 50, 60 ), 80 )
    dieview2 = DieView( win, Point( 150, 60 ), 80 )
    
    #my sums
    counter = {10: SumCounter( win, Point( 300, 50), 10), 4: SumCounter( win, Point( 300, 75), 4), 2: SumCounter( win, Point( 300, 100), 2), 11: SumCounter( win, Point( 300, 125), 11)}
    
    rollButton = Button( win, Point( 100, 160), 100, 40, "Roll!" )
    while True:
        mouseClick = win.getMouse()
        if rollButton.wasClickedIn( mouseClick ):
            dieview1.roll()
            dieview2.roll()
            sum=dieview1.getValue() + dieview2.getValue() #adds together each dice roll
            
            if sum in counter: # if the sum of the rolls equal a number in the counter, it keeps a tally
                counter[sum].handleRoll()
                counter[sum].setText()
            
main()