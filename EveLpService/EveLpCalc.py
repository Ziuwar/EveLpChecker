###########################################
# Company: 		AS-Engineering
# File: 		EveLpCalc.py	
# Name: 		Andreas Schroeder
# Date: 		24.12.2017
#
# Description: 	Calls all the functions that are needed for the LP effiency calculations
# Revision: 	R00
###########################################

import mysql.connector
import DbOps
import EveDataMath
from copy import deepcopy

def Calculator(MineralPrice, MineralNeed, LpStoreItemPrice, SellPriceJita, LpStoreLpCost):
	
	Calculated = {}

	MineralTotal = EveDataMath.MineralPriceCalc(MineralPrice, MineralNeed)
	PriceTotal = EveDataMath.TotalPrice(LpStoreItemPrice, MineralTotal)
	Profit = EveDataMath.ItemProfit(SellPriceJita, PriceTotal)
	ProfitLp = EveDataMath.LpEfficiency(Profit['ISK'], LpStoreLpCost)

	#print('Mineral total price : %.2f' % (MineralTotal))
	#print('Total price from BP: %.2f' % (PriceTotal))
	#print('Total profit in ISK: %.2f' % (Profit['ISK']))
	#print('Total profit in percent: %.2f' % (Profit['Percent']))
	#print('Efficiency (Profit/LP): %.2f' % (ProfitLp))
    
	Calculated.update({"MaterialPrice": MineralTotal,"ItemTotalPrice": PriceTotal,"Profit": Profit['ISK'],"ProfitPercent":Profit['Percent'],"Efficiency":ProfitLp})

	return Calculated
 
#Open mySQL connection
evedata = mysql.connector.connect(user='pi', password='pi', host='127.0.0.1', database='evedata') 
#Create a database cursor                                                                                                                  
cursor = evedata.cursor();

##1. Step: 	Get the item meta data from the database, so mineral need, Lp store ISK price, Lp Store Lp
## 			cost and the sell price in Jita
CalcData = DbOps.SelectCalcData(cursor)
#print CalcData
##2. Step:	Get the mineral prices from the database
MineralPrice = DbOps.MineralsAndPrice(cursor)
#print MineralPrice
'''!!! The following steps must be done per ItemUid in CalcData !!!'''
for ItemUid in CalcData:
	
	MineralNeed = deepcopy(CalcData [ItemUid])
	del(MineralNeed['IskPrice'],MineralNeed['LpPoints'],MineralNeed['SellPriceJita'])
	#print MineralNeed
	
	##3. Step: Calculate stuff
	Calculated = Calculator(MineralPrice,MineralNeed,CalcData[ItemUid]['IskPrice'],CalcData[ItemUid]['SellPriceJita'],CalcData[ItemUid]['LpPoints'])
	print Calculated
	
	##4. Step: Write the calculated values into the database




#Close the mySQL connection
cursor.close()
evedata.close()

## The End
