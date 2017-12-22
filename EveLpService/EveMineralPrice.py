###########################################
# Company: 		AS-Engineering
# File: 		EveMineralPrice.py	
# Name: 		Andreas Schroeder
# Date: 		22.12.2017
#
# Description: 	Updates the eve mineral prices in the database
# Revision: 	R00 Tested
###########################################

#Library import
import mysql.connector
import requests
import json
import DbOps

#Variables
FuzzUrl = 'https://market.fuzzwork.co.uk/aggregates/?region=60003760&types='
#Used SQL commands
#SqlComSelItemUid = ("SELECT ItemUid FROM evedata.EveMineralPrice WHERE Mineral = '%s'") # EveMinerals
SqlComUpdMinPrice = ("UPDATE evedata.EveMineralPrice SET ItemPrice = '%.2f' WHERE Mineral = '%s'") #ItemPrice, EveMinerals

#Open mySQL connection
evedata = mysql.connector.connect(user='pi', password='pi', host='127.0.0.1', database='evedata') 
#Create a database cursor                                                                                                                  
cursor = evedata.cursor();

#Get the minerals from the database
#EveMinerals = 

#Iterate over the Minerals stored in the EveMinerals variable
#for i in range(0,len(EveMinerals),1):
## Step 1 Read the ItemUid from the database
#	cursor.execute(SqlComSelItemUid % EveMinerals[i])
#	ItemUid = str(cursor.fetchone()[0])

MineralUid = DbOps.MineralUid(cursor, DbOps.EveMinerals(cursor))

## Step 2 get the current price for the ItemUid from Fuzzwork
FinalUrl = FuzzUrl+MineralUid[0]
PageResponse = requests.get(FinalUrl)
if PageResponse.status_code != 200: print ("!!An HTML error occured!!")
JsonPageOutput = PageResponse.text
PhytonPageOutput = json.loads(JsonPageOutput)
ItemPrice = float(PhytonPageOutput [MineralUid[0]]['sell']['min'])

## Step 3 update the current price into the database
cursor.execute(SqlComUpdMinPrice % (ItemPrice, MineralUid[0]))
evedata.commit()

#Close the mySQL connection
cursor.close()
evedata.close()

