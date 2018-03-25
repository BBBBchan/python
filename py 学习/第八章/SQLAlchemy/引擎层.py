import sqlalchemy as sa
conn = sa.create_engine('sqlite://')
conn.execute('''CREATE TABLE zoo
	(critter VARCHAR(20) PRIMARY KEY, count INT, damages FLOAT)''')
ins = 'INSERT INTO zoo (critter, count, damages) VALUES (?, ?, ?)'
conn.execute(ins, 'duck', 10, 0.0)
conn.execute(ins, 'bear', 2, 1000.0)
conn.execute(ins, 'weasel', 1, 2000.0)

rows = conn.execute('SELECT * FROM zoo')
print(rows)								#无法直接打印信息

for row in rows:						#可迭代
	print(row)