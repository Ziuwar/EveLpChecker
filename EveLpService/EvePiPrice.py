############################################
# Company: 		AS-Engineering
# File: 		EvePiPrice.py
# Name: 		Andreas Schroeder
# Date: 		03.02.2018
#
# Description: 	Updates the eve pi prices in the database
# Revision: 	R00 - Not Tested
############################################

# Library import
import mysql.connector
import DbOps
import WwwOps


def update_pi_meta_data():
    """Update of the mineral prices"""

    # Open mySQL connection
    evecalc = mysql.connector.connect(user='remote', password='remote00Long', host='127.0.0.1', database='evecalc')
    # Create a database cursor
    cursor = evecalc.cursor()
    # # Step 1 get the pi item UID´s
    pi_uid = DbOps.pi_uid(cursor)
    # print MineralUid
    # # Step 2 get the current price for the ItemUid from Fuzzwork
    uid_and_price = WwwOps.item_price(pi_uid, 'sell', 'min')
    # print UidAndPrice
    # # Step 3 update the current price into the database
    pi_return = DbOps.update_pi(cursor, evecalc, uid_and_price)
    # print Return
    # Close the mySQL connection
    cursor.close()
    evecalc.close()

    print(pi_return)

    return pi_return

