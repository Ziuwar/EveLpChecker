###########################################
# Company: 		AS-Engineering
# File: 		MySqlDbConf.py	
# Name: 		Andreas Schroeder
# Date: 		16.12.2017
#
# Description: 	Configuration of the MySql database used in the EvE Data Project
# Revision: 	R00 - Tested
###########################################

#Connector library import
import mysql.connector

#Open mySQL connection
cnx = mysql.connector.connect(user='pi', password='pi',
                              host='127.0.0.1',
                              database='evecalc')
                              
#Create a database cursor                                                                                                                  
cur = cnx.cursor();

#DANGER !!! Database evecalc creation script !!! Use with brain enabled !!!

# DROP and CREATE DATABASE
#cur.execute("DROP DATABASE evecalc;")
#cur.execute("CREATE DATABASE evecalc;")

#DROP Tables
#cur.execute("DROP TABLE evecalc.EveItemData;")
#cur.execute("DROP TABLE evecalc.EvePriceHistory;")
#cur.execute("DROP TABLE evecalc.EveMineralPrice;")

#CREATE Tables
cur.execute("CREATE TABLE evecalc.EveMineralPrice ( Mineral varchar(50) NOT NULL PRIMARY KEY, ItemUid int, ItemPrice float);")
cur.execute("CREATE TABLE evecalc.EvePriceHistory ( Ident int AUTO_INCREMENT NOT NULL PRIMARY KEY, EveItemId int, PriceTimestamp date);")
cur.execute("CREATE TABLE evecalc.EveItemData ( ItemUid int NOT NULL PRIMARY KEY, ItemName varchar (100), IskPrice float, LpPoints int, MaterialPrice float, ItemTotalPrice float, SellPriceJita float, SellTaxes float, Profit float, ProfitPercent float, Efficiency float, Tritanium int, Pyerite int, Mexallon int, Isogen int, Nocxium int, Zydrine int, Megacyte int);")

#Fill tables

cur.execute("INSERT INTO evecalc.EveMineralPrice VALUES ('Tritanium','34', '4.79'), ('Pyerite','35', '5.20'), ('Mexallon','36', '63.80'), ('Isogen', '37', '70.00'), ('Nocxium', '38', '416.99'), ('Zydrine', '39', '1309.89'), ('Megacyte', '40', '1090.00');")
cur.execute("INSERT INTO evecalc.EveItemData VALUES ('33468','Astero','15000000.00','30000','387669.41','15387669.41','62300000.00','1.5','46912330.59','404.87','1400.00','24022','8044','2822','467','40','18','4'), ('33470','Stratios','30000000.00','120000','8916771.51','38916771.51','200000000.00','1.5','161083228.49','513.92','1250.00','614356','154233','39907','9687','2387','1202','356');")

cnx.commit()

#Close the mySQL connection
cur.close()
cnx.close()
print("Fuck You Roally")
