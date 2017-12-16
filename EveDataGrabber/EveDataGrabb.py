###########################################
# Company: 		AS-Engineering
# File: 		EveDataGrabb.py	
# Name: 		Andreas Schroeder
# Date: 		16.12.2017
#
# Description: 	Gets the EvE Online item ID from the local database
# Revision: 	R00 Not-tested
###########################################

#Connector library import
import mysql.connector

#Open mySQL connection
cnx = mysql.connector.connect(user='pi', password='pi', host='127.0.0.1', database='evedata') 
#Create a database cursor                                                                                                                  
cursor = cnx.cursor();

SqlCommand = ("SELECT ItemPrice FROM EveMineralPrice WHERE Mineral = 'Tritanium'")
cursor.execute(SqlCommand)
fname = cursor.fetchone()[0]
#fname = cursor.fetchall()
print fname

#cursor.fetchall()

#cur.execute("INSERT INTO TABLE EveMineralPrice VALUES '66' WHERE Mineral IS 'Tritanium'")

#Close the mySQL connection
cursor.close()
cnx.close()
print("Fuck You Roally")
