icon = input("What stock do you want to sell?: ")
tshare = int(input("Total shares owned?: "))
stprice = int(input("share price? : "))
endamount = int(input("End share price? : "))
sellshare = int(input("How many shares are you selling?: "))

class StockHolding:
    
    def __init__( self, icon, tshare, stprice ):
        self.icon = icon
        self.tshare = tshare
        self.stprice = stprice
    
    def getNumShares(self):
        return self.tshare
    
    def getstprice(self):
        return self.stprice
    
    def sellShares(self, sellshare ):
        self.sellshare = sellshare
        if self.tshare - sellshare >= 0:
            self.tshare = self.tshare - sellshare
            print("Your remaining shares are: {}".format( self.tshare ))
        else:
            raise ValueError("You don't have that many stocks. Please run this program again.")
        
    def estimatedProfit(self, endamount, sellshare):
        estimatedProfit = (endamount - self.stprice) * sellshare
        if estimatedProfit > 1000:
            print("Profit for selling {0} your shares is {1}".format( sellshare, estimatedProfit ))
        else:
            print("Keep your stocks boy or girl, your estimated profit is less than 1000. Taxes will kill you")
        return estimatedProfit


def main():
    testStockHolding = StockHolding( icon, tshare, stprice )
    testStockHolding.sellShares( sellshare )
    testStockHolding.estimatedProfit( endamount, sellshare)

main()


