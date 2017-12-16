###########################################
# Company: 		AS-Engineering
# File: 		EveDataGrabb.py	
# Name: 		Andreas Schröder
# Date: 		16.12.2017
#
# Description: 	Gets the EvE Online item ID from the local database
# Revision: 	R00 Not-tested
###########################################

#Connector library import
import mysql.connector

#Open mySQL connection
cnx = mysql.connector.connect(user='pi', password='pi',
                              host='127.0.0.1',
                              database='') 
                              
#Create a database cursor                                                                                                                  
cur = cnx.cursor();

cur.execute("INSERT INTO TABLE EveMineralPrice  ")

#Close the mySQL connection#
cur.close()
cnx.close()
print("Fuck You Roally")
