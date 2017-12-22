###########################################
# Company: 		AS-Engineering
# File: 		EveMarketData.py	
# Name: 		Andreas Schroeder
# Date: 		23.12.2017
#
# Description: 	Functions needed for the WWW communication
# Revision: 	R00 - Tested
###########################################

import requests
import json

#Using the very nice Fuzzwork API
FuzzUrl = 'https://market.fuzzwork.co.uk/aggregates/?region=60003760&types='
UidAndPrice = {}

def MineralPrice(MineralUid):
	"Gets the market data for the given UID, has do be reworked for all items and data items"

	for Item in MineralUid:
		FinalUrl = FuzzUrl+Item
		PageResponse = requests.get(FinalUrl)
		
		#Check if the HTML message is 200, has to be reworked for error handling
		if PageResponse.status_code != 200: print ("!!An HTML error occured!!")
		
		#Json to dict and get the desired data item
		JsonPageOutput = PageResponse.text
		PhytonPageOutput = json.loads(JsonPageOutput)
		ItemPrice = float(PhytonPageOutput [Item]['sell']['min'])
		#Build a dict with item UID:Price
		UidAndPrice.update({Item:ItemPrice})
	
	return UidAndPrice
