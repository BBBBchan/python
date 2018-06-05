import sqlite3

def dict_factory(cursor, row):  					#转换元组为字典类型
    d = {}  
    for idx, col in enumerate(cursor.description):  
        d[col[0]] = row[idx]  
    return d
 

conn = sqlite3.connect('enterprise.db')
conn.row_factory = dict_factory
curs = conn.cursor()

curs.execute('INSERT INTO zoo VALUES("duck", 5, 0.0)')				#插入两行信息
curs.execute('INSERT INTO zoo VALUES("ber", 5, 1000.0)')
curs.execute('''UPDATE zoo SET count = ?, critter = ? where damages = ?''',[1,'bear',1000.0])
ins = 'INSERT INTO zoo (critter, count, damages) VALUES(?, ?, ?)'	#使用三个问号代表要插入三个值，并把他们作为一个列表传入函数execute() 可以防止SQL注入
curs.execute(ins, ('weasel', 1, 2000.0))

#使用SQL命令获取信息
curs.execute('SELECT count FROM zoo WHERE count = ? AND critter = ?', [1,'bear'])
rows = curs.fetchall()
print(rows)
if rows == True:
	print(rows[0])

# #按照count升序排序
# curs.execute('SELECT * FROM zoo ORDER BY count')
# rows = curs.fetchall()
# print(rows)

# #按照count降序排序
# curs.execute('SELECT * FROM zoo ORDER BY count DESC')
# rows = curs.fetchall()
# print(rows)


# #寻找damages的最大值对应信息
# curs.execute('''SELECT * FROM zoo WHERE damages = (SELECT MAX(damages) FROM zoo)''')
# rows = curs.fetchall()
# print(rows)
curs.close()
conn.close()
