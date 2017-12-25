
import mysql.connector


evedata = mysql.connector.connect(user='remote', password='remote',
                                  host='192.168.178.25',
                                  database='evedata')

cursor = evedata.cursor()

cursor.execute('select * from EveItemData;')

fetch = cursor.fetchall()

print(fetch)

cursor.close()
evedata.close()
