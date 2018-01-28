
import mysql.connector

sql_command = 'SELECT ItemName,IskPrice,LpPoints,MaterialPrice,ItemTotalPrice,SellPriceJita,Profit,ProfitPercent,' \
              'Efficiency FROM evedata.EveItemData ORDER BY Efficiency DESC;'

# Open mySQL connection
evecalc = mysql.connector.connect(user='root', password='root00Long', host='h2759962.stratoserver.net', database='evecalc')
# Create a database cursor
cursor = evecalc.cursor()

cursor.execute(sql_command)
grid_data_fetch = cursor.fetchall()

# Close the mySQL connection
cursor.close()
evecalc.close()


for row in grid_data_fetch:
    for item in row:
        print(item)

