###########################################
# Company: 		AS-Engineering
# File: 		EveDataGrabb.py	
# Name: 		Andreas Schroeder
# Date: 		17.12.2017
#
# Description: 	Updates the eve mineral prices in the database
# Revision: 	R00 Tested
###########################################

#Library import
import mysql.connector
import requests
import json

#Variables
FuzzUrl = 'https://market.fuzzwork.co.uk/aggregates/?region=60003760&types='
EveMinerals = "Tritanium","Pyerite" ,"Isogen","Mexallon","Nocxium","Megacyte","Zydrine"
#Used SQL commands
SqlComSelItemUid = ("SELECT ItemUid FROM evedata.EveMineralPrice WHERE Mineral = '%s'") # EveMinerals
SqlComUpdMinPrice = ("UPDATE evedata.EveMineralPrice SET ItemPrice = '%.2f' WHERE Mineral = '%s'") #ItemPrice, EveMinerals

#Open mySQL connection
evedata = mysql.connector.connect(user='pi', password='pi', host='127.0.0.1', database='evedata') 
#Create a database cursor                                                                                                                  
cursor = evedata.cursor();

#Iterate over the Minerals stored in the EveMinerals variable
for i in range(0,len(EveMinerals),1):
## Step 1 Read the ItemUid from the database
	cursor.execute(SqlComSelItemUid % EveMinerals[i])
	ItemUid = str(cursor.fetchone()[0])
#fname = cursor.fetchall()

## Step 2 get the current price for the ItemUid from Fuzzwork
	FinalUrl = FuzzUrl+ItemUid
	PageResponse = requests.get(FinalUrl)
	if PageResponse.status_code != 200: print ("!!An HTML error occured!!")
	JsonPageOutput = PageResponse.text
	PhytonPageOutput = json.loads(JsonPageOutput)
	ItemPrice = float(PhytonPageOutput [ItemUid]['sell']['min'])

## Step 3 update the current price into the database
	cursor.execute(SqlComUpdMinPrice % (ItemPrice, EveMinerals[i]))
	evedata.commit()

#Close the mySQL connection
cursor.close()
evedata.close()

