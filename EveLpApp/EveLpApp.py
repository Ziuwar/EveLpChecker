
import mysql.connector

sql_command = 'SELECT ItemName,IskPrice,LpPoints,MaterialPrice,ItemTotalPrice,SellPriceJita,Profit,ProfitPercent,' \
              'Efficiency FROM evedata.EveItemData ORDER BY Efficiency DESC;'

# Open mySQL connection
evedata = mysql.connector.connect(user='remote', password='remote', host='192.168.178.25', database='evedata')
# Create a database cursor
cursor = evedata.cursor()

cursor.execute(sql_command)
grid_data_fetch = cursor.fetchall()

# Close the mySQL connection
cursor.close()
evedata.close()


for row in grid_data_fetch:
    for item in row:
        print(item)

