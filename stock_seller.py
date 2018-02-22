class StockHolding:
    
    def __init__( self, icon, tshare, startingpri ):
        self.icon = icon
        self.tshare = tshare
        self.startingpri = startingpri
        
    def geticon(self):
        return self.icon
    
    def getNumShares(self):
        return self.tshare
    
    def getstartingpri(self):
        return self.startingpri
    
    def sellShares(self, sellshare ):
        self.sellshare = sellshare
        if self.tshare - sellshare >= 0:
            self.tshare = self.tshare - sellshare
            print("Your remaining shares are: {}".format( self.tshare ))
        else:
            raise ValueError("You don't have that many.")
        return self.tshare, sellshare
        
    def estimatedProfit(self, endamount, sellshare):
        estimatedProfit = (endamount - self.startingpri) * sellshare
        if estimatedProfit > 0:
            print("Profit for selling {0} {1} shares is {2}".format( sellshare, self.icon, estimatedProfit ))
        else:
            print("Keep your stocks boy")
        return estimatedProfit
                          
        
def getInputs():
    icon = input("What stock do you want to sell?: ")
    tshare = int(input("Total shares owned?: "))
    startingpri = float(input("share price? : "))
    endamount = float(input("End share price? : "))
    sellshare = float(input("How many shares are you selling?: "))
    return icon, tshare, startingpri, endamount, sellshare


def main():
    icon,tshare, startingpri, endamount, sellshare = getInputs()
    testStockHolding = StockHolding( icon, tshare, startingpri )
    testStockHolding.sellShares( sellshare )
    testStockHolding.estimatedProfit( endamount, sellshare)

main()


