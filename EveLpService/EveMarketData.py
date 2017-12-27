###########################################
# Company: 		AS-Engineering
# File: 		EveMarketData.py	
# Name: 		Andreas Schroeder
# Date: 		23.12.2017
#
# Description:  Getting the LP store item related market prices from the fuzzwork.co.uk api
# Revision: 	R00 - Not tested
###########################################

import mysql.connector
import WwwOps, DbOps

def UpdateJitaMaxSell():

	#Open mySQL connection
	evedata = mysql.connector.connect(user='pi', password='pi', host='127.0.0.1', database='evedata') 
	#Create a database cursor                                                                                                                  
	cursor = evedata.cursor();

	##Step 1: Get the Lp Item Uids from the database
	LpItemUid = DbOps.LpItemUid(cursor)
	#print LpItemUid
	##Step 2: Get the max buy price in Jita from Fuzzwork
	UidAndPrice = WwwOps.item_price(LpItemUid, 'buy', 'max')
	#print UidAndPrice
	##Step 3: Update the new price for the Lp store items in the database
	Result = DbOps.UpdateLpJitaPrice(cursor, evedata, UidAndPrice)
	print(Result)

	#Close the mySQL connection
	cursor.close()
	evedata.close()
	return Result
	
