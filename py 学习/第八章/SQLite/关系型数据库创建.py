import sqlite3
conn = sqlite3.connect('enterprise.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE zoo				
(critter VARCHAR(20)PRIMARY KEY,
count INT,
damages FLOAT)''')						#多次创建会报错

cur.close()
conn.close()