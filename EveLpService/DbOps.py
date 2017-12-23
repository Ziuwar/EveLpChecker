###########################################
# Company: 		AS-Engineering
# File: 		DbOps.py	
# Name: 		Andreas Schroeder
# Date: 		22.12.2017
#
# Description: 	Database functions for the EveLpProject
# Revision: 	R00 - Tested
###########################################

import mysql.connector

def EveMinerals(cursor):
	"Get all minerals stored in the database"

	SqlCommand = 'select Mineral from EveMineralPrice order by ItemUid;'
	EveMineral = []

	cursor.execute(SqlCommand)

	fetch = cursor.fetchall()

	for row in fetch:
		EveMineral.append(str(row[0]))
 
	return EveMineral

def MineralUid(cursor, EveMinerals):
	"Get the mineral Uid per mineral in the database"
	
	SqlComSelItemUid = ("SELECT ItemUid FROM evedata.EveMineralPrice WHERE Mineral = '%s'") # EveMinerals
	ItemUid = []
	
	#Iterate over the Minerals stored in the EveMinerals variable
	for i in range(0,len(EveMinerals),1):
		## Step 1 Read the ItemUid from the database
		cursor.execute(SqlComSelItemUid % EveMinerals[i])
		ItemUid.append(str(cursor.fetchone()[0]))

	return ItemUid

def UpdateMinerals(cursor, evedata, UidAndPrice):
	"Updates the mineral prices for all minerals."
	
	SqlComUpdMinPrice = ("UPDATE evedata.EveMineralPrice SET ItemPrice = '%.2f' WHERE ItemUid = '%s'") #ItemPrice, EveMinerals

	for Item in UidAndPrice:
		
		cursor.execute(SqlComUpdMinPrice % (UidAndPrice[Item], str(Item)))
		evedata.commit()
	
	MineralsUpdated = 'All minerals updated!'
	return MineralsUpdated
	
def LpItemUid(cursor):
	"Get the item Uid per item in the database"
	
	SqlComSelItemUid = ("SELECT ItemUid FROM evedata.EveItemData")
	ItemUid = []
		
	cursor.execute(SqlComSelItemUid)
	
	DbItemUid = cursor.fetchall()
	
	for row in DbItemUid:
		ItemUid.append(str(row[0]))

	return ItemUid	

def UpdateLpJitaPrice(cursor, evedata, UidAndPrice):
	"Update the Jita max sell price for all items."
	
	SqlComUpdMaxBuy = ("UPDATE evedata.EveItemData SET SellPriceJita = '%.2f' WHERE ItemUid = '%s'") #ItemPrice, EveMinerals

	for Item in UidAndPrice:
		
		cursor.execute(SqlComUpdMaxBuy % (UidAndPrice[Item], str(Item)))
		evedata.commit()
	
	LpUpdated = 'All minerals updated!'
	return LpUpdated	
	
def SelectCalcData(cursor):
	"Select all the data needed for the calculation task"

	SqlCommand = 'SELECT ItemUid, IskPrice, LpPoints, SellPriceJita, Tritanium, Pyerite, Mexallon, Isogen, Nocxium, Zydrine, Megacyte FROM EveItemData ORDER BY ItemUid;'
	EveMineral = []

	cursor.execute(SqlCommand)

	fetch = cursor.fetchall()

	for row in fetch:
		EveMineral.append(str(row[0]))
 
	return EveMineral 

	
