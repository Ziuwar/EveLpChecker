###########################################
# Company: 		AS-Engineering
# File: 		EveMarketData.py	
# Name: 		Andreas Schroeder
# Date: 		27.12.2017
#
# Description: 	Functions needed for the WWW communication
# Revision: 	R00 - Tested
###########################################

import requests
import json

# Using the very nice Fuzzwork API
# url = 'https://www.fuzzwork.co.uk/api/typeid.php?typename=Tritanium'             # TypeID
# uid_url = 'https://www.fuzzwork.co.uk/api/typeid.php?typename='                  # TypeID
# market_url = 'https://market.fuzzwork.co.uk/aggregates/?region=60003760&types='


def item_price(item_id, sell_buy, data_field):
    """"Gets the market data for the given UID, has do be reworked for multiple items"""

    # item_uid is a string in a list like: ['34']
    # sell_buy is a single string, possible strings are only 'sell' and 'buy'
    # data_field is the value needed in the requests data like: 'max' or 'min'

    market_url = 'https://market.fuzzwork.co.uk/aggregates/?region=60003760&types='
    uid_and_price = {}

    for Item in item_id:
        final_url = market_url+Item
        page_response = requests.get(final_url)

        # Check if the HTML message is 200, has to be reworked for error handling
        if page_response.status_code != 200:
            print("!!An HTML error occurred!!")

        # Json to dict and get the desired data item
        json_page_output = page_response.text
        python_page_output = json.loads(json_page_output)
        item_data = float(python_page_output[Item][sell_buy][data_field])
        # Build a dict with item UID:Price
        uid_and_price.update({Item: item_data})

    # Returns a dict like this : {'34': 690.0}

    return uid_and_price


def item_uid(item_name):
    """Gets the uid for the give item names, item_name is expected as list like: ['Tritanium']"""

    uid_url = 'https://www.fuzzwork.co.uk/api/typeid.php?typename='  # TypeID

    for item in item_name:
        final_url = uid_url + item
        page_request = requests.get(final_url)

        # Check if the HTML message is 200, has to be reworked for error handling
        if page_request.status_code != 200:
            print("!!An HTML error occurred!!")

        # Convert json to python list
        json_page_output = page_request.text
        www_item_uid = json.loads(json_page_output)

    # Comes as dict {'typeID': 0, 'typeName': 'bad item'} for bad input
    # and {'typeID': 34, 'typeName': 'Tritanium'} for a valid item

    return www_item_uid
