import sqlite3
import csv
import os

DB_FILENAME = 'new.db'
DB_FILEPATH = os.path.join(os.getcwd(), DB_FILENAME)
#csv download
CSV_FILENAME = 'day_on_fin.csv'
CSV_FILEPATH = os.path.join(os.getcwd(), CSV_FILENAME)

con = sqlite3.connect(DB_FILENAME)
cur = con.cursor()

create_table = """CREATE TABLE SubwayOn (id INT PRIMARY KEY,
										 Year INT, Month INT, Day INT,
										 Line INT, St_num INT, b_six INT,
										 t6am INT, t7am INT, t8am INT, t9am INT, t10am INT, t11am INT, noon INT, t1pm INT, t2pm INT, t3pm INT, t4pm INT, t5pm INT, t6pm INT, t7pm INT, t8pm INT,
           								 t9pm INT, t10pm INT, t11pm INT, a_mid INT, total INT, avgTa FLOAT, minTa FLOAT, maxTa FLOAT,
       									 sumRn FLOAT, day_info INT, bus_cnt INT);"""
cur.execute("DROP TABLE IF EXISTS SubwayOn;")
cur.execute(create_table)
cur.close()


count = 0
data = []
col = []
with open(CSV_FILEPATH, 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    for line in csv_reader:
        if count == 0:
            col.append(line)
        else:
            data.append(line)
        count+=1

c=con.cursor()
for i in data:
    c.execute(f"""INSERT INTO SubwayOn (
        		id, Year, Month, Day, Line, St_num, b_six,
                t6am, t7am, t8am, t9am, t10am,
                t11am, noon, t1pm, t2pm, t3pm,
                t4pm, t5pm, t6pm, t7pm, t8pm,
                t9pm, t10pm, t11pm, a_mid, total,
                avgTa, minTa, maxTa,
       			sumRn, day_info, bus_cnt)
          		VALUES
            	({int(i[0])}, {int(i[1][:4])}, {int(i[1][5:7])}, {int(i[1][-2:])}, {int(i[2])}, {int(i[3])}, {int(i[4])},
            	{int(i[5])}, {int(i[6])}, {int(i[7])}, {int(i[8])}, {int(i[9])},
            	{int(i[10])}, {int(i[11])}, {int(i[12])}, {int(i[13])}, {int(i[14])},
             	{int(i[15])}, {int(i[16])}, {int(i[17])}, {int(i[18])}, {int(i[19])},
              	{int(i[20])}, {int(i[21])}, {int(i[22])}, {int(i[23])}, {int(i[24])},
              	{float(i[25])}, {float(i[26])}, {float(i[27])},
               	{float(i[28])}, {int(i[29])}, {int(i[30])}); """)

con.commit()
c.close()
con.close()

