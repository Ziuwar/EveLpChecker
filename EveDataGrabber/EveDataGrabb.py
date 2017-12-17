###########################################
# Company: 		AS-Engineering
# File: 		EveDataGrabb.py	
# Name: 		Andreas Schroeder
# Date: 		16.12.2017
#
# Description: 	Gets the EvE Online item ID from the local database
# Revision: 	R00 Not-tested
###########################################

#Library import
import mysql.connector
import requests
import json

#Variables
FuzzUrl = 'https://market.fuzzwork.co.uk/aggregates/?region=60003760&types='
EveMinerals = "'Tritanium'", "Pyerite" , "Isogen", "Mexallon", "Nocxium", "Megacyte", "Zydrine"
#Used SQL commands
SqlComSelItemUid = ("SELECT ItemUid FROM EveMineralPrice WHERE Mineral = %s") # EveMinerals
SqlComExeMinePrice = ("INSERT INTO TABLE EveMineralPrice VALUES %s WHERE Mineral IS %s") #ItemPrice, EveMinerals

#Open mySQL connection
cnx = mysql.connector.connect(user='pi', password='pi', host='127.0.0.1', database='evedata') 
#Create a database cursor                                                                                                                  
cursor = cnx.cursor();

## Step 1 Read the ItemUid from the database
cursor.execute(SqlComSelItemUid % EveMinerals[0])
ItemUid = str(cursor.fetchone()[0])
#fname = cursor.fetchall()

## Step 2 get the current price for the ItemUid from Fuzzwork
FinalUrl = FuzzUrl+ItemUid
PageResponse = requests.get(FinalUrl)
print PageResponse.status_code
JsonPageOutput = PageResponse.text
PhytonPageOutput = json.loads(JsonPageOutput)
ItemPrice = PhytonPageOutput [ItemUid]['sell']['min']

## Step 3 insert the current price into the database



#cur.execute("INSERT INTO TABLE EveMineralPrice VALUES '66' WHERE Mineral IS 'Tritanium'")


#Close the mySQL connection
cursor.close()
cnx.close()
print("Fuck You Roally")
