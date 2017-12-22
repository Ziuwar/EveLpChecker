###########################################
# Company: 		AS-Engineering
# File: 		DbOps.py	
# Name: 		Andreas Schroeder
# Date: 		22.12.2017
#
# Description: 	Database functions for the EveLpProject
# Revision: 	R00 - Not tested
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
