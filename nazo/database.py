import sqlite3

conn = sqlite3.connect('/UserData.db')
curs = conn.cursor()
# curs.execute('''CREATE TABLE UserData (nid int, username varchar(20), password varchar(20), current_level int)''')
# curs.execute('''INSERT INTO UserData VALUES(?,?,?,?)''',[1,'a','123',2])
curs.execute('''SELECT * FROM UserData where nid = 3''')
info = curs.fetchall()
if info == []:
	print('12')
conn.commit()
curs.close()
conn.close()