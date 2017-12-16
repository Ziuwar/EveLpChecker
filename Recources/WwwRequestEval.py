###########################################
# Company: 		AS-Engineering
# File: 		EveMarketData.py	
# Name: 		Andreas Schröder
# Date: 		16.12.2017
#
# Description: 	Evaluation of getting the EvE Online market prices from the fuzzwork.co.uk api
# Revision: 	R00
###########################################

#requests (installed with pip (very nice, open Python programmer library access) does the data collection)  
import requests

#BeautifulSuop is a lib to parse and organize the html and xml data, not so much json (installed with pip)
#from bs4 import BeautifulSoup

#json knows and handels json style formating (comes with Python3)
import json

#URL to read, in this case fuzzworks api
#url = 'https://www.fuzzwork.co.uk/api/typeid.php?typename=Tritanium'       #TypeID
#url = 'https://www.fuzzwork.co.uk/api/typeid.php?typename='                #TypeID
url = 'https://market.fuzzwork.co.uk/aggregates/?region=60003760&types='    #Market price data in Jita 

#The Item (Mineral) name must be querried from the database
Item = '34'
#Total easy way to join strings, yeah
FinalUrl = url+Item

#The requests.get method reads the data from the URL 
page = requests.get(FinalUrl)
#The attribute .status_code gives 200 for OK, 400 and 500 are errors (see HTML status code definition)
print(page.status_code)
#The attribute .text holds the text based content of the request 
#print(page.text)

#In order to use the json.loads method, the text attribute content needs to be stored in a variable
JsonOutput = page.text

#################################

#soup = BeautifulSoup(page.text, 'html.parser')
#print (soup.prettify())

#################################

#The json.loads method converts the JSON in Python value(object) format
JsonToPython = json.loads(JsonOutput)

#Redout of the needed values like that
BuyMax = JsonToPython[Item]['buy']['max']

print(BuyMax)
