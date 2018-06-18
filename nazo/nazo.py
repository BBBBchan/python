from flask import Flask, render_template, request, redirect,g,jsonify,session,escape,url_for
from contextlib import closing
import sqlite3

app = Flask(__name__)
app.secret_key = 'bbchan'
app.debug = True

def connect_db():
    return sqlite3.connect('/UserData.db')

@app.before_request
def before_request():
    g.db = connect_db()
    g.db.row_factory = dict_factory

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
    g.db.close()

def dict_factory(cursor, row):  					#转换元组为字典类型
    d = {}
    for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]  
    return d

@app.route('/', methods=['GET'])
def index():
		return render_template('index.html')

@app.route('/levels/<int:current_level>', methods=['GET','POST'])
def levels(current_level):
	if 'username' in session:
		if request.method == 'GET':
			curs = g.db.cursor()
			curs.execute('''SELECT current_level FROM UserData where username=?''',[escape(session['username'])])
			user_level = curs.fetchall()
			user_level = user_level[0]['current_level']
			if user_level >= current_level:
				url = '/levels/'+str(current_level)+'.html'
				return render_template(url)
			else:
				url = '/levels/'+str(user_level)
				return redirect(url)

		elif request.method == 'POST':
			user_ans = request.form.get('ans')
			curs = g.db.cursor()
			curs.execute('''SELECT correct_ans FROM correct_ans where level = ?''',[current_level])
			correct_ans = curs.fetchall()
			correct_ans = correct_ans[0]['correct_ans']
			if user_ans == correct_ans:
				current_level += 1
				if current_level == 9:
					return redirect('http://www.bbbbchan.com')
				print(escape(session['username']))
				curs.execute('''UPDATE UserData SET current_level = ? where username = ?''',[current_level,escape(session['username'])])
				g.db.commit()
				url = 'levels/'+str(current_level)
				return redirect(url)
			else:
				url = '/levels/'+str(current_level)+'.html'
				return render_template(url,error='答案错误')
	else:
		return redirect('/wrong_login')


@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	elif request.method == 'POST':
		username = request.form.get('username')
		password = request.form.get('password')
		session['username'] = username
		print(escape(session['username']))
		curs = g.db.cursor()
		curs.execute('''SELECT nid,username,password,current_level FROM UserData where username = ? ''',[username])
		user_info = curs.fetchall()
		if password == user_info[0]['password']:
			url = '/levels/'+str(user_info[0]['current_level'])
			user_info = {1:user_info[0]}
			return redirect(url)
		else:
			return render_template('login.html', error='用户名或密码错误')

@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'GET':
		return render_template('register.html')
	elif request.method == 'POST':
		username = request.form.get('username')
		password = request.form.get('password')
		curs = g.db.cursor()
		curs.execute('''SELECT nid FROM UserData where username=?''',[username])
		check_nid = curs.fetchall()
		if check_nid == []:
			curs.execute('''SELECT nid FROM UserData where nid = (SELECT MAX(nid) FROM UserData)''')
			current_nid = curs.fetchall()
			current_nid = current_nid[0]['nid'] + 1
			curs.execute('''INSERT INTO UserData VALUES(?,?,?,?)''',[current_nid, username, password, 1])
			g.db.commit()
			return redirect('login')
		else:
			return render_template('register.html', error = '用户名重复')

@app.route('/wrong_login')
def wrong_login():
	return render_template('wrong_login.html')

if __name__ == '__main__':
	app.run()