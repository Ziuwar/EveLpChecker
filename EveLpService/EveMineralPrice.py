###########################################
# Company: 		AS-Engineering
# File: 		EveMineralPrice.py	
# Name: 		Andreas Schroeder
# Date: 		22.12.2017
#
# Description: 	Updates the eve mineral prices in the database
# Revision: 	R01 Tested
###########################################

#Library import
import mysql.connector
import DbOps
import WwwOps

def UpdateMineralMetaData():
	"Update of the mineral prices"
	
	#Open mySQL connection
	evedata = mysql.connector.connect(user='pi', password='pi', host='127.0.0.1', database='evedata') 
	#Create a database cursor                                                                                                                  
	cursor = evedata.cursor();
	##Step 1 get the minerals and cross check that every mineral has a UID
	MineralUid = DbOps.MineralUid(cursor, DbOps.EveMinerals(cursor))
	#print MineralUid
	## Step 2 get the current price for the ItemUid from Fuzzwork
	UidAndPrice = WwwOps.ItemPrice(MineralUid, 'sell', 'min')
	#print UidAndPrice
	## Step 3 update the current price into the database
	Return = DbOps.UpdateMinerals(cursor, evedata, UidAndPrice)
	#print Return
	#Close the mySQL connection
	cursor.close()
	evedata.close()
	
	print(Return)
	
	return Return

