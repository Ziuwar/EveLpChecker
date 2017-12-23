###########################################
# Company: 		AS-Engineering
# File: 		EveLpCalc.py	
# Name: 		Andreas Schroeder
# Date: 		16.12.2017
#
# Description: 	Calls all the functions that are needed for the LP effiency calculations
# Revision: 	R00
###########################################

import mysql.connector
import DbOps
import EveDataMath

MineralPrice = {'Tritanium' : 4.35, 'Pyerite' : 4.7, 'Mexallon' : 62, 'Isogen' : 50, 'Nocxium' : 110, 'Zydrine' : 500, 'Megacyte' : 800, 'Morphite' : 1200}
MineralNeed = {'Tritanium' : 24022, 'Pyerite' : 8044, 'Mexallon' : 2822, 'Isogen' : 467, 'Nocxium' : 40, 'Zydrine' : 18, 'Megacyte' : 4, 'Morphite' : 0}
LpStoreItemPrice = 15000000.00
LpStoreLpCost = 30000
SellPriceJita = 62300000.00

#Open mySQL connection
evedata = mysql.connector.connect(user='pi', password='pi', host='127.0.0.1', database='evedata') 
#Create a database cursor                                                                                                                  
cursor = evedata.cursor();

##1. Step: 	Get the item meta data from the database, so mineral need, Lp store ISK price, Lp Store Lp
## 			cost and the sell price in Jita
CalcData = DbOps.SelectCalcData(cursor)
print CalcData
##2. Step:	Get the mineral prices from the database

##3. Step: Calculate stuff
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

##4. Step: Write the calculated values into the database








#Close the mySQL connection
cursor.close()
evedata.close()
## The End
