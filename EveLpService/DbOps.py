###########################################
# Company: 		AS-Engineering
# File: 		DbOps.py	
# Name: 		Andreas Schroeder
# Date: 		22.12.2017
#
# Description: 	Database functions for the EveLpProject
# Revision: 	R00 - Tested
###########################################


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

    SqlComSelItemUid = ("SELECT ItemUid FROM evecalc.EveMineralPrice WHERE Mineral = '%s'")  # EveMinerals
    ItemUid = []

    # Iterate over the Minerals stored in the EveMinerals variable
    for i in range(0, len(EveMinerals), 1):
        ## Step 1 Read the ItemUid from the database
        cursor.execute(SqlComSelItemUid % EveMinerals[i])
        ItemUid.append(str(cursor.fetchone()[0]))

    return ItemUid


def UpdateMinerals(cursor, evecalc, UidAndPriceM):
    "Updates the mineral prices for all minerals."

    SqlComUpdMinPrice = (
    "UPDATE evecalc.EveMineralPrice SET ItemPrice = '%.2f' WHERE ItemUid = '%s'")  # ItemPrice, EveMinerals

    for Item in UidAndPriceM:
        cursor.execute(SqlComUpdMinPrice % (UidAndPriceM[Item], str(Item)))

    evecalc.commit()

    MineralsUpdated = '### - ' + str(len(UidAndPriceM)) + ' minerals updated! - ###\n'
    return MineralsUpdated


def LpItemUid(cursor):
    "Get the item Uid per item in the database"

    SqlComSelItemUid = ("SELECT ItemUid FROM evecalc.EveItemData")
    ItemUid = []

    cursor.execute(SqlComSelItemUid)

    DbItemUid = cursor.fetchall()

    for row in DbItemUid:
        ItemUid.append(str(row[0]))

    return ItemUid


def UpdateLpJitaPrice(cursor, evecalc, UidAndPriceJ):
    "Update the Jita max sell price for all items."

    SqlComUpdMaxBuy = (
    "UPDATE evecalc.EveItemData SET SellPriceJita = '%.2f' WHERE ItemUid = '%s'")  # ItemPrice, EveMinerals
    Count = 0

    for Item in UidAndPriceJ:
        cursor.execute(SqlComUpdMaxBuy % (UidAndPriceJ[Item], str(Item)))
        Count = Count + 1

        evecalc.commit()

    LpUpdated = '### - ' + str(Count) + ' Jita item prices updated! - ###\n'
    return LpUpdated


def SelectCalcData(cursor):
    "Select the data needed for the calculation task for one given item"

    SqlCommand = 'SELECT ItemUid, IskPrice, LpPoints, SellPriceJita, Tritanium, Pyerite, Mexallon, Isogen, Nocxium, Zydrine, Megacyte FROM EveItemData ORDER BY ItemUid;'
    EveCalcData = {}
    RowCount = 0

    cursor.execute(SqlCommand)
    fetch = cursor.fetchall()

    for row in fetch:  # Generates a dict with {ItemUid{Items}}

        EveCalcData.update({fetch[RowCount][0]: {"IskPrice": fetch[RowCount][1], "LpPoints": fetch[RowCount][2],
                                                 "SellPriceJita": fetch[RowCount][3],
                                                 "Tritanium": fetch[RowCount][4], "Pyerite": fetch[RowCount][5],
                                                 "Mexallon": fetch[RowCount][6], "Isogen": fetch[RowCount][7],
                                                 "Nocxium": fetch[RowCount][8], "Zydrine": fetch[RowCount][9],
                                                 "Megacyte": fetch[RowCount][10]}})
        RowCount = RowCount + 1

    return EveCalcData


def MineralsAndPrice(cursor):
    "Get all minerals with prices from the database in a dict"

    SqlCommand = 'select Mineral,ItemPrice from EveMineralPrice order by ItemUid;'
    MineralAndPrice = {}

    cursor.execute(SqlCommand)
    fetch = cursor.fetchall()

    for row in fetch:
        MineralAndPrice.update({str(row[0]): row[1]})

    return MineralAndPrice


def UpdateItemData(cursor, evecalc, ItemUid, Calculated):
    "Update the Jita max sell price for all items."

    SqlComUpdMaxBuy = ("UPDATE evecalc.EveItemData SET %s = '%.2f' WHERE ItemUid = '%s'")  # ColName, Value, UidValue

    for Item in Calculated:
        cursor.execute(SqlComUpdMaxBuy % (Item, Calculated[Item], str(ItemUid)))

        evecalc.commit()

    ItemsUpdated = 'Item data updated'
    return ItemsUpdated


def pi_uid(cursor):
    """Get the mineral Uid per mineral in the database"""

    sql_com_sel_item_uid = "SELECT uid FROM evecalc.pi_prices"  # EveMinerals
    item_uid = []

    cursor.execute(sql_com_sel_item_uid)
    pi_item_uid = cursor.fetchall()

    for row in pi_item_uid:
        item_uid.append(str(row[0]))

    return item_uid


def update_pi(cursor, evecalc, uid_and_price):
    """Updates the mineral prices for all minerals."""

    sql_com_upd_min_price = "UPDATE evecalc.pi_prices SET price = '%.2f', updated_at = NOW() WHERE uid = '%s'"  # ItemPrice, EveMinerals

    for Item in uid_and_price:
        cursor.execute(sql_com_upd_min_price % (uid_and_price[Item], str(Item)))

    evecalc.commit()

    pi_items_updated = '### - ' + str(len(uid_and_price)) + ' PI items updated! - ###\n'
    return pi_items_updated
