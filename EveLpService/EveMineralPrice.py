############################################
# Company: 		AS-Engineering
# File: 		EveMineralPrice.py	
# Name: 		Andreas Schroeder
# Date: 		22.12.2017
#
# Description: 	Updates the eve mineral prices in the database
# Revision: 	R01 Tested
############################################

#Library import
import mysql.connector
import DbOps
import WwwOps

def UpdateMineralMetaData():
	"Update of the mineral prices"
	
	#Open mySQL connection
	evecalc = mysql.connector.connect(user='root', password='root00Long', host='127.0.0.1', database='evecalc')
	#Create a database cursor                                                                                                                  
	cursor = evecalc.cursor();
	##Step 1 get the minerals and cross check that every mineral has a UID
	MineralUid = DbOps.MineralUid(cursor, DbOps.EveMinerals(cursor))
	# print MineralUid
	## Step 2 get the current price for the ItemUid from Fuzzwork
	UidAndPrice = WwwOps.item_price(MineralUid, 'sell', 'min')
	# print UidAndPrice
	## Step 3 update the current price into the database
	Return = DbOps.UpdateMinerals(cursor, evecalc, UidAndPrice)
	# print Return
	#Close the mySQL connection
	cursor.close()
	evecalc.close()
	
	print(Return)
	
	return Return
