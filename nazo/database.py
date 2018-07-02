import sqlite3

def dict_factory(cursor, row):  					#转换元组为字典类型
    d = {}
    for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]  
    return d
conn = sqlite3.connect('/UserData.db')
conn.row_factory = dict_factory
curs = conn.cursor()
# curs.execute('''CREATE TABLE correct_ans (level int, correct_ans varchar(20))''')
# curs.execute('''INSERT INTO correct_ans VALUES(?,?)''',[6,"key<XDU1sG0od>"])
# curs.execute('''INSERT INTO correct_ans VALUES(?,?)''',[7,"key<thealpha>"])
# curs.execute('''INSERT INTO correct_ans VALUES(?,?)''',[8,"key<st3g0_saurus_wr3cks>"])
curs.execute('''SELECT * FROM UserData ''')
info = curs.fetchall()
print(info)
conn.commit()
curs.close()
conn.close()