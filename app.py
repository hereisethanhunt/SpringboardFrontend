from flask import Flask , render_template,url_for,redirect,request,flash,session
import json

app = Flask(__name__)
app.secret_key = 'hereisethanhunt'


@app.route('/')
def index():
	return render_template('index.html')




# @app.route('/login',methods=['POST'])
# def login():
# 	name=request.form['name']
# 	session['username'] = name
	
# 	#session.pop('username', None)  // for logout session
# 	if(name=='admin'):
# 		flash('You were successfully logged in')
# 		return redirect(url_for('hello_admin'))
# 	else:
# 		flash('You were successfully logged in')
# 		return redirect(url_for('hello_guest',guest = name))


# @app.route('/hello_admin')
# def hello_admin():
# 	return render_template('admin.html')


# @app.route('/hello_guest/<guest>')
# def hello_guest(guest):
# 	return render_template('guest.html', name = guest) 


# @app.route('/marks/<guest>' , methods=['POST'])
# def marks(guest):
# 	phy=request.form['phy']
# 	che=request.form['che']
# 	com=request.form['com']
# 	mat=request.form['mat']
# 	eng=request.form['eng']
# 	name=request.form['name']
# 	arr=[phy,che,com,mat,eng]
# 	#arr=[1,2,3,4,5]
# 	return render_template('marks.html',name=name,data=arr)


if __name__ == '__main__':
	app.run(debug = True)
