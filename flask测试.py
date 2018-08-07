from flask import Flask, render_template, request, redirect,g,jsonify,session,escape,url_for
from contextlib import closing
import sqlite3

app = Flask(__name__)
app.debug = True

@app.route('/index', methods=['POST'])
def index():
	data = request.json
	pic_id = data.get('pic_id')
	for i in range(0,len(pic_id)):
		print(pic_id[i])
	return jsonify({'message':'successful'})

if __name__ == '__main__':
	app.run()