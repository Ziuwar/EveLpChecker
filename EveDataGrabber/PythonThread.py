
#! C:\Users\Andreas.Schroeder\source\repos\PythonApplication2\PythonApplication2
# The mighty OS thread generator station

import threading, time
import EveDataMath

MineralPrice = {'Tritanium' : 4.35, 'Pyerite' : 4.7, 'Mexallon' : 62, 'Isogen' : 50, 'Nocxium' : 110, 'Zydrine' : 500, 'Megacyte' : 800, 'Morphite' : 1200}
MineralNeed = {'Tritanium' : 24022, 'Pyerite' : 8044, 'Mexallon' : 2822, 'Isogen' : 467, 'Nocxium' : 40, 'Zydrine' : 18, 'Megacyte' : 4, 'Morphite' : 0}
LpStoreItemPrice = 15000000.00
LpStoreLpCost = 30000
SellPriceJita = 62300000.00

ExitFlag = 0

def Calculator():

    MineralTotal = EveDataMath.MineralPriceCalc(MineralPrice, MineralNeed)
    PriceTotal = EveDataMath.TotalPrice(LpStoreItemPrice, MineralTotal)
    Profit = EveDataMath.ItemProfit(SellPriceJita, PriceTotal)
    ProfitLp = EveDataMath.LpEfficiency(Profit['ISK'], LpStoreLpCost)

    print('Mineral total price Astero: %.2f' % (MineralTotal))
    print('Total price of Astero from BP: %.2f' % (PriceTotal))
    print('Total profit in ISK: %.2f' % (Profit['ISK']))
    print('Total profit in percent: %.2f' % (Profit['Percent']))
    print('Efficiency (Profit/LP): %.2f' % (ProfitLp))

    return

class CalcThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("Starting " + self.name)
        print_time(self.name, 5, self.counter)
        print("Exiting " + self.name)

def print_time(threadName, counter, delay):
    while counter:
        if ExitFlag:
            threadName.exit()
        time.sleep(delay)
        Calculator()
        print("\n\n%s: %s\n\n" % (threadName, time.ctime()))
        #counter -= 1

#Create new threads
Calc1 = CalcThread(1,'CalcOne',10)

#Start new Thread
Calc1.start()

print("Exiting Main Thread")









