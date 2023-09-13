import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect('climate.db')
c = conn.cursor()

c.execute('SELECT co2 FROM ClimateData;')
co2_data = c.fetchall()

c.execute('SELECT temperature FROM ClimateData;')
temp_data = c.fetchall()

c.execute('SELECT year FROM ClimateData;')
years_data = c.fetchall()

conn.close()

years = []
co2 = []
temp = []

for i in range(len(co2_data)):
    co2.append(co2_data[i][0])
    temp.append(temp_data[i][0])
    years.append(years_data[i][0])

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_1.png") 
